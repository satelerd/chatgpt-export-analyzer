# 🎤 ChatGPT Export Analyzer

Un analizador visual ultra avanzado para exports de ChatGPT que genera reportes interactivos con gráficos estilo GitHub, análisis de sentimientos, visualizaciones temporales y mucho más.

## ✨ Características

### 📊 Visualizaciones Avanzadas
- **Gráfico estilo GitHub**: Actividad diaria con cuadrados de colores por intensidad
- **Gráficos por año**: Visualización separada para cada año (2022, 2023, 2024, 2025)
- **Heatmap de actividad**: Patrones de uso por día y hora
- **Gráfico acumulativo**: Evolución temporal de conversaciones
- **Análisis de días activos**: Estadísticas de días con/sin actividad

### 🧪 Laboratorio Interactivo
- **Audio Aleatorio**: Reproduce audios de tus conversaciones
- **Conversación Aleatoria**: Muestra conversaciones completas
- **Primeros 10 Audios**: Tus primeros mensajes de voz
- **Estadísticas en tiempo real**: Contadores de experimentos

### 📈 Análisis Completo
- **Estadísticas básicas**: Conversaciones, mensajes, palabras, caracteres
- **Análisis temporal**: Actividad por día, hora, mes, año
- **Análisis de contenido**: Lenguajes, términos técnicos, temas
- **Análisis de sentimientos**: Clasificación positiva/negativa/neutral
- **Métricas de productividad**: Conversaciones por día, palabras por día
- **Análisis avanzado**: Patrones de uso, tendencias, correlaciones

## 🚀 Instalación y Uso

### 1. Descargar el Export de ChatGPT
1. Ve a [ChatGPT Settings](https://chat.openai.com/settings)
2. Haz clic en "Data Export"
3. Selecciona "Export data"
4. Descarga el archivo ZIP cuando esté listo

### 2. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/chatgpt-export-analyzer.git
cd chatgpt-export-analyzer
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el Analizador
```bash
python3 main.py tu-export-chatgpt.zip
```

### 5. Ver el Reporte
```bash
python3 simple_server.py
```
Luego abre: http://localhost:8001/report.html

## 📋 Opciones Avanzadas

### Especificar Directorio de Salida
```bash
python3 main.py tu-export-chatgpt.zip -o mi-reporte
```

### Cambiar Puerto del Servidor
```bash
python3 simple_server.py --port 8080
```

### Análisis Completo con Opciones
```bash
python3 main.py tu-export-chatgpt.zip -o output --port 8001
```

## 📁 Estructura del Proyecto

```
chatgpt-export-analyzer/
├── main.py                 # Script principal
├── parser.py              # Analizador de datos
├── simple_server.py       # Servidor web
├── template_report.html   # Template del reporte
├── requirements.txt       # Dependencias
└── README.md             # Este archivo
```

## 🎨 Características del Reporte

### Diseño Visual
- **Estética hacker**: Colores neón y efectos visuales
- **Animaciones**: Transiciones suaves y efectos de hover
- **Responsive**: Se adapta a diferentes tamaños de pantalla
- **Interactivo**: Tooltips, gráficos dinámicos, controles de audio

### Gráficos Incluidos
- **Barras**: Estadísticas básicas y métricas
- **Líneas**: Evolución temporal y tendencias
- **Donas**: Distribución de datos categóricos
- **Radar**: Análisis multidimensional
- **Scatter**: Correlaciones entre variables
- **Heatmap**: Patrones de actividad temporal

## 🔧 Personalización

### Modificar Colores
Edita las variables CSS en `template_report.html`:
```css
:root {
    --neon-green: #00ff41;
    --neon-blue: #00d4ff;
    --neon-pink: #ff0080;
    --neon-purple: #b300ff;
    --neon-yellow: #ffff00;
    --neon-orange: #ff6b35;
}
```

### Agregar Nuevas Estadísticas
Modifica `parser.py` para incluir nuevos análisis:
```python
def analyze_custom_metric(data):
    # Tu análisis personalizado aquí
    return custom_stats
```

## 🐛 Solución de Problemas

### Error: "No se encontró conversations.json"
- Verifica que el ZIP sea un export válido de ChatGPT
- Asegúrate de que el archivo no esté corrupto

### Error: "ModuleNotFoundError: No module named 'textblob'"
```bash
pip install --break-system-packages textblob nltk
```

### Error: "Puerto ya en uso"
```bash
python3 simple_server.py --port 8080
```

### El reporte no carga
- Verifica que el servidor esté ejecutándose
- Revisa la consola del navegador para errores
- Asegúrate de que todos los archivos estén en el directorio correcto

## 📊 Ejemplo de Salida

El analizador genera:
- `chatgpt_stats.json`: Estadísticas completas en JSON
- `report.html`: Reporte visual interactivo
- `audio/`: Archivos de audio copiados (si existen)

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 🙏 Agradecimientos

- OpenAI por ChatGPT
- La comunidad de desarrolladores de Python
- Contribuidores de librerías de visualización

---

**¡Disfruta explorando tus conversaciones con ChatGPT de una manera completamente nueva!** 🚀
