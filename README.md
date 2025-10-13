# 🚀 ChatGPT Analytics Pro

**Reporte Interactivo Ultra Avanzado para tus Datos de ChatGPT**

Un análisis completo y visual de tu actividad con ChatGPT, con gráficos estilo GitHub, análisis de sentimientos, laboratorio interactivo y efectos visuales impresionantes.

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

## ✨ Características Principales

### 🎨 Estética Ultra Avanzada
- **Diseño Hacker/Trippy**: Efectos neon, partículas animadas, gradientes psicodélicos
- **Efectos Glitch**: Animaciones de glitch en títulos y elementos especiales
- **Partículas Dinámicas**: 80+ partículas flotantes con diferentes tamaños y velocidades
- **Gradientes Pulsantes**: Fondos animados con múltiples capas de efectos
- **Paleta Neon Completa**: Verde, azul, púrpura, rosa, amarillo, naranja y cian neón

### 📊 Análisis Avanzados
- **Análisis de Sentimientos**: Clasificación automática de mensajes positivos, negativos y neutrales
- **Heatmap de Actividad**: Visualización día vs hora con colores dinámicos
- **Timeline Interactivo**: Evolución temporal con los días más activos
- **Correlaciones**: Análisis de relaciones entre diferentes métricas
- **Patrones de Comportamiento**: Detección de hábitos de uso y patrones de interacción

### 📈 Visualizaciones Creativas
- **Gráfico Estilo GitHub**: Actividad diaria por año (2022-2025) con cuadraditos más grandes
- **Heatmap de Actividad**: Visualización día vs hora con cuadraditos más pequeños
- **Gráfico de Evolución Acumulada**: Progresión temporal de conversaciones totales
- **Gráficos Interactivos**: Barras, líneas, donas, radar, polar y scatter plots
- **Nube de Palabras**: Visualización dinámica con tamaños y colores variables
- **Análisis de Contenido**: Lenguajes de programación, términos técnicos, temas
- **Métricas de Productividad**: Conversaciones por día, palabras por día, etc.

### 🧪 Laboratorio Interactivo
- **Audio Aleatorio**: Reproduce archivos de audio reales de tus conversaciones
- **Conversación Aleatoria**: Muestra toda una conversación completa con todos los mensajes ordenados cronológicamente
- **Conversación Completa**: Lee toda una conversación con todos los mensajes ordenados cronológicamente
- **Primeros 10 Audios**: Busca y reproduce tus primeros 10 mensajes de voz enviados (si están disponibles en el export)
- **Estadísticas en Tiempo Real**: Contador de experimentos realizados, audios reproducidos y conversaciones revisadas

## 🚀 Instalación y Uso

### Opción 1: Setup Automático (Recomendado)

1. **Descarga tu exportación de ChatGPT**
   - Ve a [chat.openai.com](https://chat.openai.com)
   - Settings → Data controls → Export data
   - Descarga el archivo ZIP

2. **Clona o descarga este repositorio**
   ```bash
   git clone https://github.com/tu-usuario/chatgpt-analytics-pro.git
   cd chatgpt-analytics-pro
   ```

3. **Coloca el archivo ZIP en el directorio del proyecto**

4. **Ejecuta el setup automático**
   ```bash
   python3 setup.py
   ```

5. **¡Listo! El reporte se abrirá automáticamente**

### Opción 2: Instalación Manual

1. **Instala dependencias**
   ```bash
   pip install -r requirements.txt
   ```

2. **Descarga datos de NLTK**
   ```bash
   python3 -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

3. **Extrae tu archivo ZIP de ChatGPT**

4. **Genera estadísticas**
   ```bash
   python3 chatgpt_parser.py
   ```

5. **Inicia el servidor**
   ```bash
   python3 server.py
   ```

6. **Abre el reporte**: http://localhost:8001/advanced_report.html

## 📁 Estructura del Proyecto

```
chatgpt-analytics-pro/
├── setup.py                 # Setup automático
├── chatgpt_parser.py        # Parser generalizado
├── server.py                # Servidor web
├── requirements.txt         # Dependencias
├── README.md               # Este archivo
├── advanced_report.html    # Reporte principal
├── report.html            # Reporte básico
├── .gitignore            # Archivos a ignorar
└── example/              # Datos de ejemplo (opcional)
    ├── conversations.json
    └── user.json
```

## 🔧 Configuración Avanzada

### Personalizar Colores
Edita las variables CSS en `advanced_report.html`:
```css
:root {
    --neon-green: #00ff41;
    --neon-blue: #00d4ff;
    --neon-purple: #b300ff;
    --neon-pink: #ff0080;
    --neon-yellow: #ffff00;
}
```

### Modificar Análisis
Edita `chatgpt_parser.py` para agregar nuevas métricas:
```python
# Agregar nueva estadística
stats['nueva_metrica'] = calcular_nueva_metrica()
```

### Agregar Visualizaciones
Modifica `advanced_report.html` para incluir nuevos gráficos:
```javascript
// Nuevo gráfico
function createNuevoGrafico() {
    // Tu código aquí
}
```

## 📊 Datos Analizados

### Estadísticas Básicas
- Total de conversaciones
- Total de mensajes enviados
- Total de palabras escritas
- Total de caracteres
- Promedio de mensajes por conversación
- Longitud promedio de mensajes
- Día más activo y hora más activa

### Análisis Temporal
- Actividad diaria (gráfico estilo GitHub con 5 niveles)
- Actividad por hora del día (24 horas)
- Actividad mensual y semanal
- Heatmap día vs hora (7x24)
- Timeline interactivo con días más activos
- Períodos pico de uso
- Tendencias de uso a lo largo del tiempo

### Análisis de Sentimientos
- Clasificación automática de mensajes (positivos, negativos, neutrales)
- Evolución del sentimiento a lo largo del tiempo
- Distribución de sentimientos por conversación
- Correlaciones entre sentimiento y longitud de mensaje
- Análisis de calidad de conversaciones

### Análisis de Contenido
- Palabras más frecuentes (top 100)
- Temas más comunes (top 50)
- Lenguajes de programación detectados
- Términos técnicos más usados
- Patrones de interacción (gratitud, cortesía, ayuda, etc.)
- Detección de código y URLs compartidas
- Emojis más utilizados

### Métricas Avanzadas
- Conversaciones por día
- Mensajes por día
- Palabras por día
- Análisis de gaps entre conversaciones
- Complejidad de conversaciones
- Patrones de comportamiento
- Correlaciones entre métricas

### Análisis de Días Activos/Inactivos
- **Días activos**: Total de días con al menos una conversación
- **Días inactivos**: Total de días sin actividad
- **Porcentaje de actividad**: % de días activos vs total
- **Rachas de actividad**: Días consecutivos con/sin actividad
- **Racha más larga**: Máximo de días consecutivos activos
- **Promedio de rachas**: Estadísticas de consistencia

## 🎨 Características Visuales

### Efectos de Fondo
- Partículas flotantes animadas
- Gradientes radiales pulsantes
- Efectos de brillo en el header

### Gráfico Estilo GitHub
- **Gráficos por año**: Un gráfico separado para cada año (2022, 2023, 2024, 2025)
- **Estructura por semanas**: Cada columna representa una semana completa
- **Días de la semana**: Cada fila representa un día específico (Dom, Lun, Mar, Mié, Jue, Vie, Sáb)
- **5 niveles de intensidad**: Desde sin actividad hasta máxima actividad
- **Cuadraditos más grandes**: Tamaño aumentado para mejor visualización
- **Tooltips avanzados**: Información detallada al hacer hover
- **Efectos de glow**: Animaciones al interactuar con los cuadraditos
- **Diseño responsive**: Se adapta a diferentes tamaños de pantalla

### Animaciones
- Fade-in escalonado para las tarjetas
- Efectos de hover con transformaciones
- Transiciones suaves en todos los elementos
- Partículas de fondo en movimiento constante

### Paleta de Colores
- **Verde Neón**: `#00ff41` - Color principal
- **Azul Neón**: `#00d4ff` - Acentos secundarios
- **Púrpura Neón**: `#b300ff` - Elementos especiales
- **Rosa Neón**: `#ff0080` - Destacados
- **Amarillo Neón**: `#ffff00` - Acentos finales

## 🐛 Solución de Problemas

### Error: "No module named 'textblob'"
```bash
pip install textblob nltk
```

### Error: "externally-managed-environment"
```bash
pip install --break-system-packages -r requirements.txt
```

### Servidor no responde
```bash
# Usar servidor alternativo
python3 server.py --port 8002
```

### Archivo ZIP no encontrado
- Verifica que el archivo esté en el directorio correcto
- Asegúrate de que sea un export válido de ChatGPT

### Puerto ocupado
- El servidor automáticamente probará el siguiente puerto disponible
- O especifica un puerto diferente: `python3 server.py --port 8080`

## 🤝 Contribuciones

¿Tienes ideas para mejorar el proyecto?

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🆘 Soporte

Si tienes problemas:

1. Revisa la sección de solución de problemas
2. Verifica que todos los archivos estén presentes
3. Asegúrate de tener Python 3.6+
4. Prueba con el setup automático
5. Abre un [issue](https://github.com/tu-usuario/chatgpt-analytics-pro/issues) en GitHub

## 🎯 Casos de Uso

### Para Desarrolladores
- Analizar patrones de uso de ChatGPT
- Identificar temas más consultados
- Optimizar flujo de trabajo con IA

### Para Investigadores
- Estudiar interacción humano-IA
- Analizar patrones de comunicación
- Investigar uso de lenguaje técnico

### Para Usuarios Curiosos
- Descubrir insights sobre tu uso
- Revivir conversaciones pasadas
- Explorar datos de manera interactiva

## 📈 Roadmap

- [ ] Exportar gráficos como imágenes
- [ ] Filtros por fecha
- [ ] Análisis de sentimientos mejorado
- [ ] Comparativas temporales
- [ ] Modo oscuro/claro
- [ ] Más tipos de gráficos
- [ ] API REST para datos
- [ ] Dashboard en tiempo real
- [ ] Análisis de múltiples usuarios
- [ ] Integración con otros servicios de IA

---

**¡Disfruta explorando tus datos de ChatGPT! 🚀**

*Desarrollado con ❤️ para la comunidad de usuarios de ChatGPT*