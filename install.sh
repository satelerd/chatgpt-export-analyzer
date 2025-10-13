#!/bin/bash

# ChatGPT Export Analyzer - Script de Instalación
echo "🚀 Instalando ChatGPT Export Analyzer..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado. Por favor instala Python 3.8 o superior."
    exit 1
fi

# Verificar pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 no está instalado. Por favor instala pip3."
    exit 1
fi

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip3 install -r requirements.txt

# Hacer ejecutables los scripts
chmod +x main.py
chmod +x simple_server.py
chmod +x example.py

# Crear directorio de salida
mkdir -p output

echo "✅ Instalación completada!"
echo ""
echo "📋 Para usar el analizador:"
echo "   1. Descarga tu export de ChatGPT desde https://chat.openai.com/settings"
echo "   2. Ejecuta: python3 main.py tu-export.zip"
echo "   3. Abre: python3 simple_server.py"
echo "   4. Ve a: http://localhost:8001/report.html"
echo ""
echo "🧪 Para probar con datos de ejemplo:"
echo "   python3 example.py"
echo ""
echo "📚 Para más información, lee README.md"
