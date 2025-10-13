# 🎤 ChatGPT Export Analyzer

Analiza tus exports de ChatGPT y genera reportes visuales interactivos con gráficos estilo GitHub, análisis de sentimientos y mucho más.

## 🚀 Uso Rápido

### 1. Descargar el Export de ChatGPT
1. Ve a [ChatGPT Settings](https://chat.openai.com/settings)
2. Haz clic en "Data Export"
3. Selecciona "Export data"
4. Descarga el archivo ZIP cuando esté listo

### 2. Instalar y Ejecutar
```bash
# Clonar el repositorio
git clone https://github.com/satelerd/chatgpt-export-analyzer.git
cd chatgpt-export-analyzer

# Instalar dependencias
pip3 install --break-system-packages -r requirements.txt

# Procesar tu export
python3 main.py tu-export-chatgpt.zip

# Ver el reporte
python3 simple_server.py
```

### 3. Abrir el Reporte
Abre tu navegador y ve a: http://localhost:8001/report.html

## ✨ Características

- **Gráfico estilo GitHub**: Actividad diaria con cuadrados de colores
- **Gráficos por año**: Visualización separada para cada año
- **Heatmap de actividad**: Patrones de uso por día y hora
- **Laboratorio interactivo**: Audio aleatorio, conversaciones completas
- **Análisis completo**: Estadísticas, sentimientos, tendencias

## 🐛 Solución de Problemas

**Error: "externally-managed-environment"**
```bash
pip3 install --break-system-packages -r requirements.txt
```

**Error: "No se encontró conversations.json"**
- Verifica que el ZIP sea un export válido de ChatGPT

**Error: "Puerto ya en uso"**
```bash
python3 simple_server.py --port 8080
```

## 📄 Licencia

MIT License - Ver `LICENSE` para más detalles.

---

**¡Disfruta explorando tus conversaciones con ChatGPT!** 🚀