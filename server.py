#!/usr/bin/env python3
"""
ChatGPT Analytics Pro - Servidor Web Generalizado
Servidor HTTP para servir el reporte interactivo
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time
from pathlib import Path

class ChatGPTHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handler HTTP personalizado para ChatGPT Analytics Pro"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def end_headers(self):
        """Agregar headers para evitar problemas de CORS"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()
    
    def do_GET(self):
        """Manejar requests GET"""
        # Redirigir a advanced_report.html por defecto
        if self.path == '/' or self.path == '/index.html':
            self.path = '/advanced_report.html'
        return super().do_GET()
    
    def log_message(self, format, *args):
        """Personalizar logs del servidor"""
        # Solo mostrar logs importantes
        if any(keyword in args[0] for keyword in ['.html', '.json', '.css', '.js']):
            super().log_message(format, *args)

class ChatGPTServer:
    """Servidor web para ChatGPT Analytics Pro"""
    
    def __init__(self, port=8001, auto_open=True):
        self.port = port
        self.auto_open = auto_open
        self.server = None
    
    def find_available_port(self):
        """Encuentra un puerto disponible"""
        import socket
        
        for port in range(self.port, self.port + 10):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(('', port))
                    return port
            except OSError:
                continue
        
        raise OSError("No se encontró un puerto disponible")
    
    def open_browser(self):
        """Abre el navegador automáticamente"""
        if self.auto_open:
            time.sleep(2)
            webbrowser.open(f'http://localhost:{self.port}/advanced_report.html')
    
    def start(self):
        """Inicia el servidor"""
        try:
            # Encontrar puerto disponible
            self.port = self.find_available_port()
            
            # Crear servidor
            self.server = socketserver.TCPServer(("", self.port), ChatGPTHTTPRequestHandler)
            
            print("=" * 80)
            print("🚀 ChatGPT Analytics Pro - Servidor Web")
            print("=" * 80)
            print(f"🌐 Servidor iniciado en: http://localhost:{self.port}")
            print(f"📊 Reporte avanzado: http://localhost:{self.port}/advanced_report.html")
            print(f"📈 Reporte básico: http://localhost:{self.port}/report.html")
            print("=" * 80)
            print("Presiona Ctrl+C para detener el servidor")
            print("=" * 80)
            
            # Abrir navegador en un hilo separado
            if self.auto_open:
                browser_thread = threading.Thread(target=self.open_browser)
                browser_thread.daemon = True
                browser_thread.start()
            
            # Iniciar servidor
            self.server.serve_forever()
            
        except KeyboardInterrupt:
            self.stop()
        except OSError as e:
            print(f"❌ Error iniciando servidor: {e}")
            sys.exit(1)
    
    def stop(self):
        """Detiene el servidor"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
        print("\n🛑 Servidor detenido")

def main():
    """Función principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description="ChatGPT Analytics Pro - Servidor Web")
    parser.add_argument("--port", type=int, default=8001, help="Puerto del servidor")
    parser.add_argument("--no-browser", action="store_true", help="No abrir navegador automáticamente")
    
    args = parser.parse_args()
    
    # Verificar que existan los archivos necesarios
    required_files = ["advanced_report.html"]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Archivos faltantes: {', '.join(missing_files)}")
        print("💡 Ejecuta primero: python3 setup.py")
        sys.exit(1)
    
    # Crear y iniciar servidor
    server = ChatGPTServer(port=args.port, auto_open=not args.no_browser)
    server.start()

if __name__ == "__main__":
    main()