#!/usr/bin/env python3
"""
ChatGPT Data Explorer - Configuración de ejemplo
Copia este archivo a config.py y ajusta los valores según necesites
"""

import os

class Config:
    """Configuración base"""
    
    # Servidor
    PORT = int(os.environ.get('PORT', 5001))
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    HOST = os.environ.get('HOST', '0.0.0.0')
    
    # Archivos
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_FILE_SIZE', 500)) * 1024 * 1024  # MB a bytes
    TEMP_DIR = os.environ.get('TEMP_DIR', '/tmp')
    
    # Análisis
    ENABLE_SENTIMENT_ANALYSIS = os.environ.get('ENABLE_SENTIMENT_ANALYSIS', 'True').lower() == 'true'
    ENABLE_ADVANCED_STATS = os.environ.get('ENABLE_ADVANCED_STATS', 'True').lower() == 'true'
    MAX_CONVERSATIONS_LIMIT = int(os.environ.get('MAX_CONVERSATIONS_LIMIT', 10000))
    
    # Sesiones
    SESSION_TIMEOUT = int(os.environ.get('SESSION_TIMEOUT', 3600))  # 1 hora
    
    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    
    # Directorios
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    LOG_LEVEL = 'WARNING'

class TestingConfig(Config):
    """Configuración para testing"""
    TESTING = True
    DEBUG = True
    MAX_CONVERSATIONS_LIMIT = 100  # Límite bajo para tests

# Configuración por defecto
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}