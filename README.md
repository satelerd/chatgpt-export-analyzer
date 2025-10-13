# ChatGPT Data Explorer 🚀

Un analizador visual interactivo para tus datos de exportación de ChatGPT. Genera reportes hermosos y detallados con gráficos estilo GitHub, análisis de actividad y estadísticas avanzadas.

![ChatGPT Data Explorer](https://img.shields.io/badge/ChatGPT-Data%20Explorer-purple?style=for-the-badge&logo=openai)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask)


## 🚀 Instalación Rápida

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Método 1: Instalación Automática (Recomendado)

```bash
# 1. Clona el repositorio
git clone https://github.com/satelerd/chatgpt-export-analyzer.git
cd chatgpt-export-analyzer

# 2. Ejecuta la configuración automática
python setup.py

# 3. Ejecuta el servidor
python run.py
```

### Método 2: Instalación Manual

```bash
# 1. Clona el repositorio
git clone https://github.com/satelerd/chatgpt-export-analyzer.git
cd chatgpt-export-analyzer

# 2. Instala las dependencias
pip install -r requirements.txt

# 3. Descarga datos de NLTK
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# 4. Ejecuta el servidor
python app.py
```

### Abre tu navegador
```
http://localhost:5001
```

¡Eso es todo! 🎉

## 📁 Cómo obtener tus datos de ChatGPT

### Paso 1: Exportar desde ChatGPT
1. Ve a [ChatGPT](https://chat.openai.com)
2. Haz clic en tu perfil (esquina superior derecha)
3. Selecciona **"Settings"** → **"Data controls"**
4. Haz clic en **"Export"**
5. Descarga el archivo ZIP que recibirás por email

### Paso 2: Subir al analizador
1. Abre `http://localhost:5001`
2. Arrastra tu archivo ZIP al área de carga
3. Espera a que se procese (puede tomar unos minutos)
4. ¡Disfruta tu reporte personalizado!

## 🛠️ Configuración Avanzada

### Variables de Entorno
Crea un archivo `.env` para configuraciones personalizadas:

```env
# Puerto del servidor (por defecto: 5001)
PORT=5001

# Tamaño máximo de archivo en MB (por defecto: 500)
MAX_FILE_SIZE=500

# Modo debug (por defecto: False)
DEBUG=False
```

## 📊 Ejemplo de Salida

Tu reporte incluirá:

```
📈 Resumen General
├── Total Conversaciones: 6,353
├── Total Mensajes: 76,245
├── Total Palabras: 13.8M
├── Días Activos: 702/729 (96.3%)
└── Racha Más Larga: 45 días

📊 Gráficos Interactivos
├── Actividad Diaria (GitHub Style)
├── Conversaciones Diarias
├── Actividad por Hora del Día
└── Actividad Mensual

🎵 Funciones Multimedia
├── Audio Aleatorio
├── Primeros 10 Audios
├── Conversación Aleatoria
└── Conversación Completa
```

### Sistemas Operativos Soportados
- ✅ **macOS** (10.14+)
- ✅ **Linux** (Ubuntu 18.04+, CentOS 7+)
- ✅ **Windows** (10+)
- ✅ **WSL** (Windows Subsystem for Linux)

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! 

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Ideas para contribuir
- Nuevos tipos de gráficos
- Análisis de sentimientos mejorado
- Exportación de reportes en PDF
- Temas visuales adicionales


---


### Todo el código (menos esta línea de texto) fue generado por "Cheetah" en Cursor... es un modelo que actualmente está disponible en modo stealth, no sé de qué proveedor es... pero está weno weno.