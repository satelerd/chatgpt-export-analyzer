#!/bin/bash

echo "🚀 Instalando ChatGPT Export Analyzer..."

# Instalar dependencias
pip3 install --break-system-packages -r requirements.txt

echo "✅ Instalación completada!"
echo ""
echo "📋 Para usar:"
echo "   1. python3 main.py tu-export.zip"
echo "   2. python3 simple_server.py"
echo "   3. Abrir: http://localhost:8001/report.html"