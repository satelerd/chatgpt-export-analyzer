#!/usr/bin/env python3
"""
ChatGPT Data Explorer - Servidor Flask para Vercel
"""

import os
import json
import zipfile
import tempfile
import shutil
from datetime import datetime
from flask import Flask, request, jsonify, send_file, render_template_string
from werkzeug.utils import secure_filename
import uuid

# Importar nuestro parser
from chatgpt_parser import ChatGPTParser

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max

# Directorio temporal para procesar archivos
TEMP_DIR = tempfile.mkdtemp()

# Almacenamiento en memoria para sesiones (en producción usar Redis)
sessions = {}

@app.route('/')
def index():
    """Servir la landing page"""
    return send_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Procesar archivo ZIP subido"""
    print("🚀 Iniciando upload de archivo...")
    
    try:
        if 'file' not in request.files:
            print("❌ No se encontró archivo en la request")
            return jsonify({'success': False, 'error': 'No se encontró archivo'})
        
        file = request.files['file']
        if file.filename == '':
            print("❌ No se seleccionó archivo")
            return jsonify({'success': False, 'error': 'No se seleccionó archivo'})
        
        if not file.filename.lower().endswith('.zip'):
            print("❌ Archivo no es .zip")
            return jsonify({'success': False, 'error': 'El archivo debe ser un ZIP'})
        
        print(f"📁 Archivo recibido: {file.filename}")
        
        # Generar ID único para la sesión
        session_id = str(uuid.uuid4())
        session_dir = os.path.join(TEMP_DIR, session_id)
        os.makedirs(session_dir, exist_ok=True)
        print(f"📂 Directorio temporal creado: {session_dir}")
        
        # Guardar archivo temporalmente
        zip_path = os.path.join(session_dir, 'chatgpt_export.zip')
        print(f"💾 Guardando archivo en: {zip_path}")
        file.save(zip_path)
        
        # Verificar tamaño del archivo
        file_size = os.path.getsize(zip_path)
        print(f"📊 Tamaño del archivo: {file_size / (1024*1024):.2f} MB")
        
        # Extraer ZIP
        extract_dir = os.path.join(session_dir, 'extracted')
        os.makedirs(extract_dir, exist_ok=True)
        print(f"📦 Extrayendo ZIP a: {extract_dir}")
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        
        print("✅ ZIP extraído exitosamente")
        
        # Buscar archivos necesarios
        conversations_file = None
        user_file = None
        
        print("🔍 Buscando archivos de conversaciones...")
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                if file == 'conversations.json':
                    conversations_file = os.path.join(root, file)
                    print(f"✅ Encontrado conversations.json: {conversations_file}")
                elif file == 'user.json':
                    user_file = os.path.join(root, file)
                    print(f"✅ Encontrado user.json: {user_file}")
        
        if not conversations_file:
            print("❌ No se encontró conversations.json")
            return jsonify({'success': False, 'error': 'No se encontró conversations.json en el ZIP'})
        
        # Verificar tamaño de conversations.json
        conv_size = os.path.getsize(conversations_file)
        print(f"📊 Tamaño de conversations.json: {conv_size / (1024*1024):.2f} MB")
        
        # Procesar datos
        print("⚙️ Iniciando procesamiento de datos...")
        parser = ChatGPTParser()
        
        import time
        start_time = time.time()
        stats = parser.parse_and_analyze(conversations_file, user_file)
        end_time = time.time()
        
        print(f"✅ Procesamiento completado en {end_time - start_time:.2f} segundos")
        
        # Guardar estadísticas en la sesión
        stats_file = os.path.join(session_dir, 'stats.json')
        print(f"💾 Guardando estadísticas en: {stats_file}")
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        
        # Copiar archivos necesarios para el reporte
        print("📄 Copiando reporte HTML...")
        shutil.copy2('advanced_report.html', os.path.join(session_dir, 'report.html'))
        
        # Guardar información de la sesión
        sessions[session_id] = {
            'created_at': datetime.now().isoformat(),
            'stats_file': stats_file,
            'report_file': os.path.join(session_dir, 'report.html'),
            'extract_dir': extract_dir
        }
        
        print(f"🎉 Upload completado exitosamente. Session ID: {session_id}")
        
        return jsonify({
            'success': True, 
            'session_id': session_id,
            'message': 'Archivo procesado exitosamente'
        })
        
    except Exception as e:
        print(f"❌ Error procesando archivo: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': f'Error interno: {str(e)}'})

@app.route('/report')
def serve_report():
    """Servir el reporte generado"""
    session_id = request.args.get('session_id')
    
    if not session_id or session_id not in sessions:
        return jsonify({'error': 'Sesión no válida'}), 400
    
    session = sessions[session_id]
    return send_file(session['report_file'])

@app.route('/api/stats')
def get_stats():
    """Obtener estadísticas de la sesión"""
    session_id = request.args.get('session_id')
    
    if not session_id or session_id not in sessions:
        return jsonify({'error': 'Sesión no válida'}), 400
    
    session = sessions[session_id]
    
    try:
        with open(session['stats_file'], 'r', encoding='utf-8') as f:
            stats = json.load(f)
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': f'Error cargando estadísticas: {str(e)}'}), 500

@app.route('/api/audio/<path:filename>')
def serve_audio(filename):
    """Servir archivos de audio"""
    session_id = request.args.get('session_id')
    
    if not session_id or session_id not in sessions:
        return jsonify({'error': 'Sesión no válida'}), 400
    
    session = sessions[session_id]
    audio_path = os.path.join(session['extract_dir'], filename)
    
    if os.path.exists(audio_path):
        return send_file(audio_path)
    else:
        return jsonify({'error': 'Archivo de audio no encontrado'}), 404

@app.route('/api/conversations')
def get_conversations():
    """Obtener conversaciones completas"""
    session_id = request.args.get('session_id')
    
    if not session_id or session_id not in sessions:
        return jsonify({'error': 'Sesión no válida'}), 400
    
    session = sessions[session_id]
    conversations_file = os.path.join(session['extract_dir'], 'conversations.json')
    
    try:
        with open(conversations_file, 'r', encoding='utf-8') as f:
            conversations = json.load(f)
        return jsonify(conversations)
    except Exception as e:
        return jsonify({'error': f'Error cargando conversaciones: {str(e)}'}), 500

@app.route('/health')
def health_check():
    """Health check para Vercel"""
    return jsonify({'status': 'ok', 'timestamp': datetime.now().isoformat()})

# Limpieza automática de sesiones antiguas
def cleanup_old_sessions():
    """Limpiar sesiones más antiguas de 1 hora"""
    current_time = datetime.now()
    to_remove = []
    
    for session_id, session_data in sessions.items():
        created_at = datetime.fromisoformat(session_data['created_at'])
        if (current_time - created_at).seconds > 3600:  # 1 hora
            to_remove.append(session_id)
    
    for session_id in to_remove:
        try:
            session_dir = os.path.join(TEMP_DIR, session_id)
            if os.path.exists(session_dir):
                shutil.rmtree(session_dir)
            del sessions[session_id]
        except Exception as e:
            print(f"Error limpiando sesión {session_id}: {str(e)}")

# Ejecutar limpieza al inicio
cleanup_old_sessions()

if __name__ == '__main__':
    # Para desarrollo local
    app.run(debug=True, host='0.0.0.0', port=5001)
else:
    # Para Vercel
    pass
