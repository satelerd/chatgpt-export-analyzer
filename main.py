#!/usr/bin/env python3
"""
ChatGPT Export Analyzer
Analiza y genera reportes visuales de exports de ChatGPT
"""

import os
import sys
import json
import shutil
import zipfile
import argparse
from pathlib import Path
from datetime import datetime

def extract_zip(zip_path, extract_to):
    """Extrae el archivo ZIP del export de ChatGPT"""
    print(f"📦 Extrayendo {zip_path}...")
    
    if not os.path.exists(zip_path):
        print(f"❌ Error: No se encontró el archivo {zip_path}")
        return False
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"✅ Extracción completada en {extract_to}")
        return True
    except Exception as e:
        print(f"❌ Error al extraer: {e}")
        return False

def find_conversations_file(extract_dir):
    """Busca el archivo conversations.json en el directorio extraído"""
    conversations_path = None
    
    for root, dirs, files in os.walk(extract_dir):
        if 'conversations.json' in files:
            conversations_path = os.path.join(root, 'conversations.json')
            break
    
    if conversations_path:
        print(f"✅ Archivo conversations.json encontrado: {conversations_path}")
        return conversations_path
    else:
        print("❌ Error: No se encontró conversations.json en el export")
        return None

def generate_report(conversations_path, output_dir):
    """Genera el reporte HTML usando el parser"""
    print("📊 Generando estadísticas...")
    
    # Importar y ejecutar el parser
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from parser import parse_conversations
    
    try:
        stats = parse_conversations(conversations_path)
        
        # Guardar estadísticas
        stats_file = os.path.join(output_dir, 'chatgpt_stats.json')
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, default=str, ensure_ascii=False)
        
        print(f"✅ Estadísticas guardadas en {stats_file}")
        return stats_file
    except Exception as e:
        print(f"❌ Error al generar estadísticas: {e}")
        return None

def create_report_html(stats_file, output_dir):
    """Crea el reporte HTML personalizado"""
    print("🎨 Generando reporte HTML...")
    
    if not os.path.exists(stats_file):
        print("❌ Error: No se encontró el archivo de estadísticas")
        return None
    
    # Leer estadísticas
    with open(stats_file, 'r', encoding='utf-8') as f:
        stats = json.load(f)
    
    # Leer template
    template_path = os.path.join(os.path.dirname(__file__), 'template_report.html')
    if not os.path.exists(template_path):
        print("❌ Error: No se encontró template_report.html")
        return None
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Reemplazar datos en el template
    report_html = template.replace(
        'let statsData = null;',
        f'let statsData = {json.dumps(stats, default=str, ensure_ascii=False)};'
    )
    
    # Guardar reporte
    report_path = os.path.join(output_dir, 'report.html')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_html)
    
    print(f"✅ Reporte HTML generado: {report_path}")
    return report_path

def copy_audio_files(extract_dir, output_dir):
    """Copia archivos de audio al directorio de salida"""
    print("🎵 Copiando archivos de audio...")
    
    audio_dir = os.path.join(output_dir, 'audio')
    os.makedirs(audio_dir, exist_ok=True)
    
    audio_count = 0
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            if file.endswith('.wav'):
                src = os.path.join(root, file)
                dst = os.path.join(audio_dir, file)
                shutil.copy2(src, dst)
                audio_count += 1
    
    print(f"✅ {audio_count} archivos de audio copiados")
    return audio_count > 0

def main():
    parser = argparse.ArgumentParser(description='Analiza exports de ChatGPT y genera reportes visuales')
    parser.add_argument('zip_file', help='Archivo ZIP del export de ChatGPT')
    parser.add_argument('-o', '--output', default='output', help='Directorio de salida (default: output)')
    parser.add_argument('--port', type=int, default=8001, help='Puerto para el servidor (default: 8001)')
    
    args = parser.parse_args()
    
    print("🚀 ChatGPT Export Analyzer")
    print("=" * 50)
    
    # Crear directorio de salida
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)
    
    # Directorio temporal para extracción
    temp_dir = output_dir / 'temp_extract'
    temp_dir.mkdir(exist_ok=True)
    
    try:
        # 1. Extraer ZIP
        if not extract_zip(args.zip_file, temp_dir):
            return 1
        
        # 2. Buscar conversations.json
        conversations_path = find_conversations_file(temp_dir)
        if not conversations_path:
            return 1
        
        # 3. Generar estadísticas
        stats_file = generate_report(conversations_path, output_dir)
        if not stats_file:
            return 1
        
        # 4. Crear reporte HTML
        report_path = create_report_html(stats_file, output_dir)
        if not report_path:
            return 1
        
        # 5. Copiar archivos de audio
        copy_audio_files(temp_dir, output_dir)
        
        # 6. Limpiar directorio temporal
        shutil.rmtree(temp_dir)
        
        print("\n" + "=" * 50)
        print("✅ Proceso completado exitosamente!")
        print(f"📁 Reporte generado en: {output_dir}")
        print(f"🌐 Para ver el reporte, ejecuta:")
        print(f"   python3 simple_server.py --port {args.port}")
        print(f"   Luego abre: http://localhost:{args.port}/report.html")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n❌ Proceso cancelado por el usuario")
        return 1
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        return 1
    finally:
        # Limpiar directorio temporal si existe
        if temp_dir.exists():
            shutil.rmtree(temp_dir)

if __name__ == '__main__':
    sys.exit(main())
