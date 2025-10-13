#!/usr/bin/env python3
"""
ChatGPT Data Explorer - Script de configuración automática
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Ejecutar comando con manejo de errores"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}: {e}")
        print(f"   Salida: {e.stdout}")
        print(f"   Error: {e.stderr}")
        return False

def check_python_version():
    """Verificar versión de Python"""
    print("🐍 Verificando versión de Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python {version.major}.{version.minor} detectado")
        print("   Se requiere Python 3.8 o superior")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detectado")
    return True

def install_dependencies():
    """Instalar dependencias"""
    print("📦 Instalando dependencias...")
    
    # Comando de pip según el sistema
    if platform.system() == "Linux":
        pip_cmd = "pip3 install --break-system-packages"
    else:
        pip_cmd = "pip install"
    
    return run_command(f"{pip_cmd} -r requirements.txt", "Instalación de dependencias")

def download_nltk_data():
    """Descargar datos de NLTK"""
    print("📚 Descargando datos de NLTK...")
    
    nltk_script = """
import nltk
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    print("✅ Datos de NLTK descargados")
except Exception as e:
    print(f"⚠️ Advertencia: No se pudieron descargar datos de NLTK: {e}")
    print("   El análisis de texto funcionará con funcionalidad limitada")
"""
    
    return run_command(f'python3 -c "{nltk_script}"', "Descarga de datos NLTK")

def create_env_file():
    """Crear archivo .env de ejemplo"""
    env_content = """# ChatGPT Data Explorer - Configuración
# Puerto del servidor (por defecto: 5001)
PORT=5001

# Tamaño máximo de archivo en MB (por defecto: 500)
MAX_FILE_SIZE=500

# Modo debug (por defecto: False)
DEBUG=False
"""
    
    if not os.path.exists('.env'):
        print("📝 Creando archivo .env de ejemplo...")
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ Archivo .env creado")
    else:
        print("ℹ️ Archivo .env ya existe")

def main():
    """Función principal de configuración"""
    print("🚀 ChatGPT Data Explorer - Configuración Automática")
    print("=" * 50)
    
    # Verificar Python
    if not check_python_version():
        sys.exit(1)
    
    # Instalar dependencias
    if not install_dependencies():
        print("❌ Error instalando dependencias")
        sys.exit(1)
    
    # Descargar datos NLTK
    download_nltk_data()
    
    # Crear archivo .env
    create_env_file()
    
    print("\n🎉 ¡Configuración completada!")
    print("\n📋 Próximos pasos:")
    print("1. Ejecuta: python app.py")
    print("2. Abre: http://localhost:5001")
    print("3. Sube tu archivo ZIP de ChatGPT")
    print("4. ¡Disfruta tu reporte!")
    
    print("\n💡 Consejos:")
    print("- Para obtener tus datos: ChatGPT → Settings → Data controls → Export")
    print("- El procesamiento puede tomar unos minutos para archivos grandes")
    print("- Todo funciona localmente, tus datos están seguros")

if __name__ == "__main__":
    main()