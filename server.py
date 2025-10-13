#!/usr/bin/env python3
"""
Servidor simple para servir el reporte HTML
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar headers para evitar problemas de CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    """Inicia el servidor HTTP"""
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🚀 Servidor iniciado en http://localhost:{PORT}")
            print(f"📊 Abriendo reporte en el navegador...")
            
            # Abrir navegador automáticamente
            webbrowser.open(f'http://localhost:{PORT}/report.html')
            
            print("Presiona Ctrl+C para detener el servidor")
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Puerto {PORT} ya está en uso. Probando puerto {PORT + 1}...")
            global PORT
            PORT += 1
            start_server()
        else:
            print(f"❌ Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    start_server()
