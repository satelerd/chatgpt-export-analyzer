# ChatGPT Analytics Pro - Configuración de Ejemplo
# Copia este archivo a config.py y ajusta los valores según necesites

# Configuración del servidor
SERVER_CONFIG = {
    'port': 8001,
    'auto_open_browser': True,
    'host': 'localhost'
}

# Configuración de análisis
ANALYSIS_CONFIG = {
    'enable_sentiment_analysis': True,
    'enable_advanced_analysis': True,
    'enable_audio_analysis': True,
    'max_conversations': None,  # None para procesar todas
    'chunk_size': 1000  # Procesar en chunks para datasets grandes
}

# Configuración de visualizaciones
VISUALIZATION_CONFIG = {
    'chart_animation_duration': 1000,
    'particle_count': 80,
    'background_effects': True,
    'neon_intensity': 1.0,
    'glitch_effects': True
}

# Configuración de archivos
FILE_CONFIG = {
    'data_dir': '.',
    'output_file': 'chatgpt_stats.json',
    'backup_stats': True,
    'compress_output': False
}

# Configuración de logging
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'chatgpt_analytics.log'
}
