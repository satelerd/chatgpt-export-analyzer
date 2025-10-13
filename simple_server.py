#!/usr/bin/env python3
"""
Servidor HTTP simple para servir el reporte avanzado
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

PORT = 8001

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar headers para evitar problemas de CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def do_GET(self):
        # Redirigir a advanced_report.html por defecto
        if self.path == '/' or self.path == '/index.html':
            self.path = '/advanced_report.html'
        return super().do_GET()

def start_server():
    """Inicia el servidor HTTP"""
    global PORT
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🚀 Servidor avanzado iniciado en http://localhost:{PORT}")
            print(f"📊 Reporte disponible en: http://localhost:{PORT}/advanced_report.html")
            print(f"📈 Reporte básico disponible en: http://localhost:{PORT}/report.html")
            print(f"📁 Archivos estáticos disponibles en: http://localhost:{PORT}/")
            print("Presiona Ctrl+C para detener el servidor")
            
            # Abrir navegador automáticamente después de un breve delay
            def open_browser():
                time.sleep(2)
                webbrowser.open(f'http://localhost:{PORT}/advanced_report.html')
            
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.daemon = True
            browser_thread.start()
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Puerto {PORT} ya está en uso. Probando puerto {PORT + 1}...")
            PORT += 1
            start_server()
        else:
            print(f"❌ Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    start_server()
