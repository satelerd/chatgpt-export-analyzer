"""
Configuración del ChatGPT Export Analyzer
"""

# Configuración de colores del tema
THEME_COLORS = {
    'neon_green': '#00ff41',
    'neon_blue': '#00d4ff',
    'neon_pink': '#ff0080',
    'neon_purple': '#b300ff',
    'neon_yellow': '#ffff00',
    'neon_orange': '#ff6b35',
    'neon_cyan': '#4ecdc4',
    'primary_bg': '#0a0a0a',
    'secondary_bg': '#111111',
    'accent_bg': '#1a1a1a',
    'card_bg': '#1e1e1e',
    'text_primary': '#ffffff',
    'text_secondary': '#cccccc',
    'text_muted': '#888888',
    'border_color': '#333333'
}

# Configuración del servidor
SERVER_CONFIG = {
    'default_port': 8001,
    'host': 'localhost',
    'cors_headers': {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
}

# Configuración de análisis
ANALYSIS_CONFIG = {
    'min_conversation_length': 1,
    'max_top_words': 100,
    'sentiment_threshold': 0.1,
    'peak_usage_multiplier': 1.5,
    'github_chart_levels': 5,
    'heatmap_hours': 24,
    'heatmap_days': 7
}

# Configuración de archivos
FILE_CONFIG = {
    'supported_formats': ['.wav', '.mp3', '.m4a'],
    'max_file_size_mb': 100,
    'temp_dir_prefix': 'chatgpt_analyzer_',
    'output_dir_default': 'output'
}

# Configuración de visualizaciones
VISUALIZATION_CONFIG = {
    'chart_colors': [
        '#00ff41', '#00d4ff', '#ff0080', '#b300ff', 
        '#ffff00', '#ff6b35', '#4ecdc4', '#ff6b6b'
    ],
    'animation_duration': 300,
    'hover_scale': 1.05,
    'github_square_size': 16,
    'github_gap': 4
}

# Mensajes del sistema
MESSAGES = {
    'welcome': '🚀 ChatGPT Export Analyzer',
    'processing': '📊 Procesando datos...',
    'complete': '✅ Análisis completado',
    'error': '❌ Error en el procesamiento',
    'no_data': '⚠️ No se encontraron datos válidos',
    'server_start': '🌐 Servidor iniciado en http://localhost:{port}',
    'server_stop': '🛑 Servidor detenido'
}
