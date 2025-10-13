#!/usr/bin/env python3
"""
ChatGPT Analytics Pro - Setup Automático
Configuración automática para cualquier usuario
"""

import os
import sys
import json
import zipfile
import shutil
import subprocess
import webbrowser
import time
import threading
from pathlib import Path

def print_banner():
    """Muestra el banner de bienvenida"""
    print("=" * 80)
    print("🚀 ChatGPT Analytics Pro - Setup Automático")
    print("=" * 80)
    print("📊 Reporte interactivo ultra avanzado para tus datos de ChatGPT")
    print("🎨 Diseño hacker/trippy con efectos neon y visualizaciones creativas")
    print("=" * 80)

def check_python_version():
    """Verifica la versión de Python"""
    if sys.version_info < (3, 6):
        print("❌ Error: Se requiere Python 3.6 o superior")
        print(f"   Versión actual: {sys.version}")
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]} detectado")

def install_dependencies():
    """Instala las dependencias necesarias"""
    print("\n📦 Instalando dependencias...")
    
    try:
        # Intentar instalar normalmente primero
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependencias instaladas correctamente")
    except subprocess.CalledProcessError:
        print("⚠️  Instalación normal falló, intentando con --break-system-packages...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", 
                "--break-system-packages", "-r", "requirements.txt"
            ])
            print("✅ Dependencias instaladas con --break-system-packages")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error instalando dependencias: {e}")
            print("💡 Intenta instalar manualmente:")
            print("   pip install textblob nltk")
            return False
    
    # Descargar recursos de NLTK
    print("📚 Descargando recursos de NLTK...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("✅ Recursos de NLTK descargados")
    except Exception as e:
        print(f"⚠️  Error descargando recursos NLTK: {e}")
    
    return True

def find_chatgpt_zip():
    """Busca el archivo ZIP de ChatGPT en el directorio actual"""
    zip_files = list(Path(".").glob("*.zip"))
    
    if not zip_files:
        print("\n❌ No se encontró ningún archivo ZIP de ChatGPT")
        print("📥 Para obtener tu export de ChatGPT:")
        print("   1. Ve a https://chat.openai.com")
        print("   2. Settings → Data controls → Export data")
        print("   3. Descarga el archivo ZIP")
        print("   4. Colócalo en este directorio")
        return None
    
    if len(zip_files) == 1:
        return zip_files[0]
    
    print("\n📁 Se encontraron múltiples archivos ZIP:")
    for i, zip_file in enumerate(zip_files, 1):
        print(f"   {i}. {zip_file.name}")
    
    while True:
        try:
            choice = input(f"\nSelecciona el archivo (1-{len(zip_files)}): ")
            index = int(choice) - 1
            if 0 <= index < len(zip_files):
                return zip_files[index]
            else:
                print("❌ Selección inválida")
        except ValueError:
            print("❌ Por favor ingresa un número válido")

def extract_chatgpt_data(zip_path):
    """Extrae los datos del archivo ZIP de ChatGPT"""
    print(f"\n📂 Extrayendo datos de {zip_path.name}...")
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")
        print("✅ Datos extraídos correctamente")
        return True
    except Exception as e:
        print(f"❌ Error extrayendo datos: {e}")
        return False

def verify_extracted_data():
    """Verifica que los datos se hayan extraído correctamente"""
    required_files = ["conversations.json"]
    optional_files = ["user.json", "message_feedback.json"]
    
    print("\n🔍 Verificando datos extraídos...")
    
    missing_required = []
    for file in required_files:
        if not os.path.exists(file):
            missing_required.append(file)
    
    if missing_required:
        print(f"❌ Archivos requeridos faltantes: {', '.join(missing_required)}")
        return False
    
    print("✅ Archivos requeridos encontrados")
    
    missing_optional = []
    for file in optional_files:
        if not os.path.exists(file):
            missing_optional.append(file)
    
    if missing_optional:
        print(f"⚠️  Archivos opcionales faltantes: {', '.join(missing_optional)}")
    
    return True

def process_data():
    """Procesa los datos y genera estadísticas"""
    print("\n⚙️  Procesando datos de ChatGPT...")
    
    try:
        # Importar y ejecutar el parser
        from parser import parse_conversations
        
        # Procesar conversaciones
        stats = parse_conversations("conversations.json")
        
        # Guardar estadísticas
        with open("chatgpt_stats.json", "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2, default=str)
        
        print("✅ Datos procesados correctamente")
        print(f"📊 Estadísticas generadas: {stats['total_conversations']} conversaciones")
        return True
        
    except Exception as e:
        print(f"❌ Error procesando datos: {e}")
        return False

def start_server():
    """Inicia el servidor web"""
    print("\n🌐 Iniciando servidor web...")
    
    try:
        # Importar y ejecutar el servidor
        from simple_server import start_server as server_start
        server_start()
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido por el usuario")
    except Exception as e:
        print(f"❌ Error iniciando servidor: {e}")

def main():
    """Función principal del setup"""
    print_banner()
    
    # Verificar Python
    check_python_version()
    
    # Instalar dependencias
    if not install_dependencies():
        print("\n❌ Setup falló en la instalación de dependencias")
        sys.exit(1)
    
    # Buscar archivo ZIP
    zip_path = find_chatgpt_zip()
    if not zip_path:
        print("\n❌ Setup falló: No se encontró archivo ZIP")
        sys.exit(1)
    
    # Extraer datos
    if not extract_chatgpt_data(zip_path):
        print("\n❌ Setup falló en la extracción de datos")
        sys.exit(1)
    
    # Verificar datos
    if not verify_extracted_data():
        print("\n❌ Setup falló en la verificación de datos")
        sys.exit(1)
    
    # Procesar datos
    if not process_data():
        print("\n❌ Setup falló en el procesamiento de datos")
        sys.exit(1)
    
    print("\n" + "=" * 80)
    print("🎉 ¡Setup completado exitosamente!")
    print("=" * 80)
    print("📊 Tu reporte interactivo está listo")
    print("🌐 El servidor se iniciará automáticamente")
    print("📱 El navegador se abrirá en unos segundos")
    print("=" * 80)
    
    # Iniciar servidor
    start_server()

if __name__ == "__main__":
    main()
