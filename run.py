#!/usr/bin/env python3
"""
ChatGPT Data Explorer - Script de ejecución simplificado
"""

import os
import sys
import argparse
import subprocess

def check_dependencies():
    """Verificar que las dependencias estén instaladas"""
    try:
        import flask
        import textblob
        import nltk
        print("✅ Todas las dependencias están instaladas")
        return True
    except ImportError as e:
        print(f"❌ Dependencia faltante: {e}")
        print("💡 Ejecuta: python setup.py")
        return False

def run_server(port=5001, debug=False):
    """Ejecutar el servidor"""
    print(f"🚀 Iniciando ChatGPT Data Explorer en puerto {port}")
    print(f"🌐 Abre tu navegador en: http://localhost:{port}")
    print("📁 Arrastra tu archivo ZIP de ChatGPT para comenzar")
    print("⏹️  Presiona Ctrl+C para detener el servidor")
    print("-" * 50)
    
    # Configurar variables de entorno
    os.environ['PORT'] = str(port)
    os.environ['DEBUG'] = str(debug)
    
    # Importar y ejecutar la app
    try:
        from app import app
        app.run(host='0.0.0.0', port=port, debug=debug)
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido")
    except Exception as e:
        print(f"❌ Error ejecutando el servidor: {e}")
        sys.exit(1)

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(description='ChatGPT Data Explorer')
    parser.add_argument('--port', '-p', type=int, default=5001, 
                       help='Puerto del servidor (por defecto: 5001)')
    parser.add_argument('--debug', '-d', action='store_true', 
                       help='Modo debug')
    parser.add_argument('--setup', '-s', action='store_true', 
                       help='Ejecutar configuración automática')
    
    args = parser.parse_args()
    
    print("🚀 ChatGPT Data Explorer")
    print("=" * 30)
    
    # Ejecutar setup si se solicita
    if args.setup:
        print("⚙️ Ejecutando configuración automática...")
        try:
            subprocess.run([sys.executable, 'setup.py'], check=True)
        except subprocess.CalledProcessError:
            print("❌ Error en la configuración")
            sys.exit(1)
    
    # Verificar dependencias
    if not check_dependencies():
        sys.exit(1)
    
    # Ejecutar servidor
    run_server(args.port, args.debug)

if __name__ == "__main__":
    main()
