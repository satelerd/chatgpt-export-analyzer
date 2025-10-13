#!/usr/bin/env python3
"""
Parser avanzado para extraer estadísticas del export de ChatGPT
Genera datos para el reporte HTML interactivo ultra profesional
"""

import json
import re
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import calendar
import math
import statistics
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import warnings
warnings.filterwarnings('ignore')

# Descargar recursos de NLTK si no están disponibles
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

def parse_conversations(file_path):
    """Parsea el archivo conversations.json y extrae estadísticas avanzadas"""
    print(f"Procesando {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        conversations = json.load(f)
    
    stats = {
        # Estadísticas básicas
        'total_conversations': len(conversations),
        'total_messages': 0,
        'total_words': 0,
        'total_characters': 0,
        
        # Actividad temporal
        'daily_activity': defaultdict(int),
        'hourly_activity': defaultdict(int),
        'monthly_activity': defaultdict(int),
        'weekly_activity': defaultdict(int),
        'yearly_activity': defaultdict(int),
        
        # Análisis de contenido
        'word_frequency': Counter(),
        'conversation_lengths': [],
        'topics': Counter(),
        'languages': Counter(),
        'message_types': Counter(),
        'conversation_titles': [],
        
        # Análisis de sentimientos
        'sentiment_scores': [],
        'positive_messages': 0,
        'negative_messages': 0,
        'neutral_messages': 0,
        
        # Patrones de uso
        'avg_message_length': 0,
        'avg_words_per_message': 0,
        'longest_message': 0,
        'shortest_message': float('inf'),
        'conversation_gaps': [],
        
        # Estadísticas temporales
        'first_conversation': None,
        'last_conversation': None,
        'avg_conversation_length': 0,
        'longest_conversation': 0,
        'shortest_conversation': float('inf'),
        'most_active_day': None,
        'most_active_hour': None,
        'most_active_month': None,
        
        # Análisis avanzado
        'question_patterns': Counter(),
        'code_blocks': 0,
        'urls_shared': 0,
        'emojis_used': Counter(),
        'technical_terms': Counter(),
        'programming_languages': Counter(),
        
        # Métricas de productividad
        'conversations_per_day': 0,
        'messages_per_day': 0,
        'words_per_day': 0,
        'peak_usage_periods': [],
        'usage_trends': [],
        
        # Análisis de comportamiento
        'session_lengths': [],
        'break_patterns': [],
        'engagement_levels': [],
        'topic_evolution': defaultdict(list),
        
        # Estadísticas de archivos
        'files_shared': 0,
        'image_files': 0,
        'document_files': 0,
        'code_files': 0,
        
        # Análisis de calidad
        'message_quality_scores': [],
        'conversation_complexity': [],
        'interaction_patterns': defaultdict(int),
        
        # Datos para visualizaciones
        'heatmap_data': defaultdict(lambda: defaultdict(int)),
        'network_data': defaultdict(list),
        'timeline_data': [],
        'correlation_data': defaultdict(float)
    }
    
    first_date = None
    last_date = None
    prev_date = None
    
    # Listas para análisis temporal
    all_dates = []
    all_message_lengths = []
    all_sentiment_scores = []
    
    for conv in conversations:
        # Estadísticas básicas
        conv_id = conv.get('id', 'unknown')
        title = conv.get('title', 'Sin título')
        create_time = conv.get('create_time', 0)
        
        if create_time:
            date = datetime.fromtimestamp(create_time)
            all_dates.append(date)
            
            if not first_date or date < first_date:
                first_date = date
                stats['first_conversation'] = date.isoformat()
            if not last_date or date > last_date:
                last_date = date
                stats['last_conversation'] = date.isoformat()
            
            # Actividad temporal detallada
            stats['daily_activity'][date.strftime('%Y-%m-%d')] += 1
            stats['hourly_activity'][date.hour] += 1
            stats['monthly_activity'][date.strftime('%Y-%m')] += 1
            stats['weekly_activity'][date.strftime('%Y-W%U')] += 1
            stats['yearly_activity'][date.year] += 1
            
            # Heatmap data (día de la semana vs hora)
            stats['heatmap_data'][date.weekday()][date.hour] += 1
            
            # Análisis de gaps entre conversaciones
            if prev_date:
                gap = (date - prev_date).total_seconds() / 3600  # en horas
                stats['conversation_gaps'].append(gap)
            prev_date = date
        
        # Analizar mensajes con análisis avanzado
        mapping = conv.get('mapping', {})
        message_count = 0
        word_count = 0
        char_count = 0
        conv_words = []
        conv_sentiments = []
        conv_message_lengths = []
        
        for msg_id, msg_data in mapping.items():
            message = msg_data.get('message')
            if message and message.get('author', {}).get('role') == 'user':
                message_count += 1
                content = message.get('content', {})
                if content.get('content_type') == 'text':
                    parts = content.get('parts', [])
                    for part in parts:
                        if isinstance(part, str):
                            # Análisis básico
                            words = part.split()
                            word_count += len(words)
                            char_count += len(part)
                            conv_words.extend(words)
                            conv_message_lengths.append(len(part))
                            all_message_lengths.append(len(part))
                            
                            # Análisis de sentimientos
                            try:
                                blob = TextBlob(part)
                                sentiment = blob.sentiment.polarity
                                conv_sentiments.append(sentiment)
                                all_sentiment_scores.append(sentiment)
                                stats['sentiment_scores'].append(sentiment)
                                
                                if sentiment > 0.1:
                                    stats['positive_messages'] += 1
                                elif sentiment < -0.1:
                                    stats['negative_messages'] += 1
                                else:
                                    stats['neutral_messages'] += 1
                            except:
                                pass
                            
                            # Detectar idioma mejorado
                            if re.search(r'[áéíóúñü]', part.lower()):
                                stats['languages']['español'] += 1
                            else:
                                stats['languages']['inglés'] += 1
                            
                            # Análisis avanzado de contenido
                            analyze_content_advanced(part, stats)
                            
                            # Extraer palabras clave para temas
                            keywords = extract_keywords(part)
                            for keyword in keywords:
                                stats['topics'][keyword] += 1
                            
                            # Detectar patrones de preguntas
                            if '?' in part:
                                stats['question_patterns']['preguntas'] += 1
                            
                            # Detectar código
                            if '```' in part or 'def ' in part or 'function ' in part:
                                stats['code_blocks'] += 1
                            
                            # Detectar URLs
                            urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', part)
                            stats['urls_shared'] += len(urls)
                            
                            # Detectar emojis
                            emojis = re.findall(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]', part)
                            for emoji in emojis:
                                stats['emojis_used'][emoji] += 1
        
        # Actualizar estadísticas de la conversación
        stats['total_messages'] += message_count
        stats['total_words'] += word_count
        stats['total_characters'] += char_count
        stats['conversation_lengths'].append(message_count)
        stats['conversation_titles'].append(title)
        
        # Análisis de calidad de la conversación
        if conv_sentiments:
            avg_sentiment = statistics.mean(conv_sentiments)
            stats['conversation_complexity'].append({
                'title': title,
                'sentiment': avg_sentiment,
                'message_count': message_count,
                'word_count': word_count,
                'avg_message_length': statistics.mean(conv_message_lengths) if conv_message_lengths else 0
            })
        
        # Actualizar estadísticas de longitud
        if message_count > stats['longest_conversation']:
            stats['longest_conversation'] = message_count
        if message_count < stats['shortest_conversation']:
            stats['shortest_conversation'] = message_count
        
        # Contar palabras frecuentes con filtrado mejorado
        stop_words = set(stopwords.words('english') + stopwords.words('spanish'))
        for word in conv_words:
            clean_word = re.sub(r'[^\w]', '', word.lower())
            if len(clean_word) > 2 and clean_word not in stop_words:
                stats['word_frequency'][clean_word] += 1
    
    # Calcular estadísticas avanzadas
    calculate_advanced_stats(stats, all_dates, all_message_lengths, all_sentiment_scores)
    
    # Calcular promedios
    if stats['conversation_lengths']:
        stats['avg_conversation_length'] = sum(stats['conversation_lengths']) / len(stats['conversation_lengths'])
    
    if stats['shortest_conversation'] == float('inf'):
        stats['shortest_conversation'] = 0
    
    if all_message_lengths:
        stats['avg_message_length'] = statistics.mean(all_message_lengths)
        stats['avg_words_per_message'] = stats['total_words'] / stats['total_messages'] if stats['total_messages'] > 0 else 0
        stats['longest_message'] = max(all_message_lengths)
        stats['shortest_message'] = min(all_message_lengths)
    
    # Convertir defaultdicts a dicts normales para JSON
    stats['daily_activity'] = dict(stats['daily_activity'])
    stats['hourly_activity'] = dict(stats['hourly_activity'])
    stats['monthly_activity'] = dict(stats['monthly_activity'])
    stats['weekly_activity'] = dict(stats['weekly_activity'])
    stats['yearly_activity'] = dict(stats['yearly_activity'])
    stats['heatmap_data'] = {str(k): dict(v) for k, v in stats['heatmap_data'].items()}
    
    # Limpiar datos para JSON
    stats['word_frequency'] = dict(stats['word_frequency'].most_common(100))
    stats['topics'] = dict(stats['topics'].most_common(50))
    stats['languages'] = dict(stats['languages'])
    stats['emojis_used'] = dict(stats['emojis_used'].most_common(20))
    stats['technical_terms'] = dict(stats['technical_terms'].most_common(30))
    stats['programming_languages'] = dict(stats['programming_languages'].most_common(20))
    stats['question_patterns'] = dict(stats['question_patterns'])
    
    # Generar datos para visualizaciones avanzadas
    stats['github_style_data'] = generate_github_style_data(stats['daily_activity'])
    stats['timeline_data'] = generate_timeline_data(stats['daily_activity'])
    stats['correlation_data'] = calculate_correlations(stats)
    
    # Análisis de días activos/inactivos
    stats['days_analysis'] = analyze_active_days(stats['daily_activity'], first_date, last_date)
    
    # Datos acumulados para gráfico de evolución
    stats['cumulative_data'] = generate_cumulative_data(stats['daily_activity'])
    
    print(f"Procesadas {stats['total_conversations']} conversaciones")
    print(f"Total de mensajes: {stats['total_messages']}")
    print(f"Total de palabras: {stats['total_words']}")
    print(f"Total de caracteres: {stats['total_characters']}")
    print(f"Análisis de sentimientos completado")
    print(f"Datos avanzados generados")
    
    return stats

def analyze_content_advanced(text, stats):
    """Análisis avanzado del contenido del texto"""
    text_lower = text.lower()
    
    # Términos técnicos
    tech_terms = [
        'algorithm', 'database', 'api', 'framework', 'library', 'function',
        'variable', 'class', 'object', 'method', 'array', 'string',
        'integer', 'boolean', 'loop', 'condition', 'recursion', 'debugging',
        'testing', 'deployment', 'server', 'client', 'frontend', 'backend',
        'fullstack', 'devops', 'docker', 'kubernetes', 'aws', 'azure',
        'machine learning', 'artificial intelligence', 'neural network',
        'deep learning', 'data science', 'analytics', 'visualization'
    ]
    
    for term in tech_terms:
        if term in text_lower:
            stats['technical_terms'][term] += 1
    
    # Lenguajes de programación
    prog_langs = [
        'python', 'javascript', 'java', 'c++', 'c#', 'php', 'ruby',
        'go', 'rust', 'swift', 'kotlin', 'typescript', 'html', 'css',
        'sql', 'r', 'matlab', 'scala', 'perl', 'bash', 'powershell'
    ]
    
    for lang in prog_langs:
        if lang in text_lower:
            stats['programming_languages'][lang] += 1
    
    # Patrones de interacción
    if 'gracias' in text_lower or 'thank you' in text_lower:
        stats['interaction_patterns']['gratitud'] += 1
    if 'por favor' in text_lower or 'please' in text_lower:
        stats['interaction_patterns']['cortesía'] += 1
    if 'explica' in text_lower or 'explain' in text_lower:
        stats['interaction_patterns']['explicación'] += 1
    if 'ayuda' in text_lower or 'help' in text_lower:
        stats['interaction_patterns']['ayuda'] += 1

def calculate_advanced_stats(stats, all_dates, all_message_lengths, all_sentiment_scores):
    """Calcula estadísticas avanzadas"""
    if not all_dates:
        return
    
    # Encontrar períodos más activos
    if stats['daily_activity']:
        stats['most_active_day'] = max(stats['daily_activity'], key=stats['daily_activity'].get)
    
    if stats['hourly_activity']:
        stats['most_active_hour'] = max(stats['hourly_activity'], key=stats['hourly_activity'].get)
    
    if stats['monthly_activity']:
        stats['most_active_month'] = max(stats['monthly_activity'], key=stats['monthly_activity'].get)
    
    # Calcular métricas de productividad
    date_range = (max(all_dates) - min(all_dates)).days
    if date_range > 0:
        stats['conversations_per_day'] = stats['total_conversations'] / date_range
        stats['messages_per_day'] = stats['total_messages'] / date_range
        stats['words_per_day'] = stats['total_words'] / date_range
    
    # Análisis de tendencias
    if len(all_dates) > 1:
        # Calcular tendencia de uso
        dates_sorted = sorted(all_dates)
        conversations_by_month = defaultdict(int)
        for date in dates_sorted:
            month_key = date.strftime('%Y-%m')
            conversations_by_month[month_key] += 1
        
        stats['usage_trends'] = list(conversations_by_month.items())
        
        # Identificar períodos pico
        if conversations_by_month:
            avg_monthly = statistics.mean(conversations_by_month.values())
            peak_threshold = avg_monthly * 1.5
            
            for month, count in conversations_by_month.items():
                if count > peak_threshold:
                    stats['peak_usage_periods'].append({
                        'month': month,
                        'count': count,
                        'intensity': count / avg_monthly
                    })
    
    # Análisis de sentimientos
    if all_sentiment_scores:
        stats['avg_sentiment'] = statistics.mean(all_sentiment_scores)
        stats['sentiment_std'] = statistics.stdev(all_sentiment_scores) if len(all_sentiment_scores) > 1 else 0
        
        # Clasificar conversaciones por sentimiento
        positive_threshold = 0.1
        negative_threshold = -0.1
        
        for conv in stats['conversation_complexity']:
            sentiment = conv['sentiment']
            if sentiment > positive_threshold:
                conv['sentiment_category'] = 'positive'
            elif sentiment < negative_threshold:
                conv['sentiment_category'] = 'negative'
            else:
                conv['sentiment_category'] = 'neutral'

def generate_timeline_data(daily_activity):
    """Genera datos para visualización de timeline"""
    timeline = []
    for date_str, count in daily_activity.items():
        date = datetime.strptime(date_str, '%Y-%m-%d')
        timeline.append({
            'date': date_str,
            'count': count,
            'day_of_week': date.strftime('%A'),
            'month': date.strftime('%B'),
            'year': date.year,
            'week_of_year': date.isocalendar()[1]
        })
    return sorted(timeline, key=lambda x: x['date'])

def calculate_correlations(stats):
    """Calcula correlaciones entre diferentes métricas"""
    correlations = {}
    
    # Correlación entre longitud de mensaje y sentimiento
    if stats['conversation_complexity']:
        message_lengths = [conv['avg_message_length'] for conv in stats['conversation_complexity']]
        sentiments = [conv['sentiment'] for conv in stats['conversation_complexity']]
        
        if len(message_lengths) > 1 and len(sentiments) > 1:
            try:
                correlations['message_length_sentiment'] = statistics.correlation(message_lengths, sentiments)
            except:
                correlations['message_length_sentiment'] = 0
    
    # Correlación entre número de mensajes y complejidad
    if stats['conversation_complexity']:
        message_counts = [conv['message_count'] for conv in stats['conversation_complexity']]
        word_counts = [conv['word_count'] for conv in stats['conversation_complexity']]
        
        if len(message_counts) > 1 and len(word_counts) > 1:
            try:
                correlations['messages_words'] = statistics.correlation(message_counts, word_counts)
            except:
                correlations['messages_words'] = 0
    
    return correlations

def analyze_active_days(daily_activity, first_date, last_date):
    """Analiza días activos vs inactivos"""
    if not first_date or not last_date:
        return {}
    
    # Calcular todos los días en el rango
    total_days = (last_date - first_date).days + 1
    active_days = len(daily_activity)
    inactive_days = total_days - active_days
    
    # Calcular porcentajes
    active_percentage = (active_days / total_days) * 100 if total_days > 0 else 0
    inactive_percentage = (inactive_days / total_days) * 100 if total_days > 0 else 0
    
    # Encontrar rachas de días activos e inactivos
    streaks = calculate_streaks(daily_activity, first_date, last_date)
    
    return {
        'total_days': total_days,
        'active_days': active_days,
        'inactive_days': inactive_days,
        'active_percentage': round(active_percentage, 2),
        'inactive_percentage': round(inactive_percentage, 2),
        'longest_active_streak': streaks['longest_active'],
        'longest_inactive_streak': streaks['longest_inactive'],
        'average_active_streak': streaks['avg_active'],
        'average_inactive_streak': streaks['avg_inactive'],
        'streaks': streaks['all_streaks']
    }

def calculate_streaks(daily_activity, first_date, last_date):
    """Calcula rachas de días activos e inactivos"""
    streaks = []
    current_streak = 0
    current_type = None  # 'active' or 'inactive'
    
    current_date = first_date
    while current_date <= last_date:
        date_str = current_date.strftime('%Y-%m-%d')
        is_active = date_str in daily_activity
        
        if is_active:
            streak_type = 'active'
        else:
            streak_type = 'inactive'
        
        if current_type == streak_type:
            current_streak += 1
        else:
            if current_streak > 0:
                streaks.append({
                    'type': current_type,
                    'length': current_streak,
                    'start_date': (current_date - timedelta(days=current_streak)).strftime('%Y-%m-%d'),
                    'end_date': (current_date - timedelta(days=1)).strftime('%Y-%m-%d')
                })
            current_streak = 1
            current_type = streak_type
        
        current_date += timedelta(days=1)
    
    # Agregar la última racha
    if current_streak > 0:
        streaks.append({
            'type': current_type,
            'length': current_streak,
            'start_date': (current_date - timedelta(days=current_streak)).strftime('%Y-%m-%d'),
            'end_date': (current_date - timedelta(days=1)).strftime('%Y-%m-%d')
        })
    
    # Calcular estadísticas de rachas
    active_streaks = [s for s in streaks if s['type'] == 'active']
    inactive_streaks = [s for s in streaks if s['type'] == 'inactive']
    
    longest_active = max([s['length'] for s in active_streaks], default=0)
    longest_inactive = max([s['length'] for s in inactive_streaks], default=0)
    avg_active = sum([s['length'] for s in active_streaks]) / len(active_streaks) if active_streaks else 0
    avg_inactive = sum([s['length'] for s in inactive_streaks]) / len(inactive_streaks) if inactive_streaks else 0
    
    return {
        'longest_active': longest_active,
        'longest_inactive': longest_inactive,
        'avg_active': round(avg_active, 2),
        'avg_inactive': round(avg_inactive, 2),
        'all_streaks': streaks
    }

def generate_cumulative_data(daily_activity):
    """Genera datos acumulados para gráfico de evolución"""
    if not daily_activity:
        return []
    
    # Ordenar fechas
    sorted_dates = sorted(daily_activity.keys())
    
    cumulative_data = []
    cumulative_conversations = 0
    cumulative_messages = 0
    cumulative_words = 0
    
    for date_str in sorted_dates:
        # Aquí necesitaríamos acceso a más datos para calcular mensajes y palabras acumuladas
        # Por ahora solo calculamos conversaciones acumuladas
        daily_count = daily_activity[date_str]
        cumulative_conversations += daily_count
        
        cumulative_data.append({
            'date': date_str,
            'daily_conversations': daily_count,
            'cumulative_conversations': cumulative_conversations,
            'cumulative_messages': cumulative_messages,  # Se actualizaría con datos reales
            'cumulative_words': cumulative_words  # Se actualizaría con datos reales
        })
    
    return cumulative_data

def extract_keywords(text):
    """Extrae palabras clave del texto"""
    # Palabras técnicas comunes
    tech_keywords = [
        'python', 'javascript', 'react', 'node', 'api', 'database', 'sql',
        'html', 'css', 'git', 'github', 'docker', 'kubernetes', 'aws',
        'machine learning', 'ai', 'neural', 'algorithm', 'data',
        'frontend', 'backend', 'fullstack', 'devops', 'deployment'
    ]
    
    keywords = []
    text_lower = text.lower()
    
    for keyword in tech_keywords:
        if keyword in text_lower:
            keywords.append(keyword)
    
    return keywords

def generate_github_style_data(daily_activity):
    """Genera datos para el gráfico estilo GitHub con años completos"""
    if not daily_activity:
        return []
    
    # Encontrar rango de fechas
    dates = [datetime.strptime(date, '%Y-%m-%d') for date in daily_activity.keys()]
    start_date = min(dates)
    end_date = max(dates)
    
    # Expandir a años completos
    start_year = start_date.year
    end_year = end_date.year
    
    github_data = []
    
    for year in range(start_year, end_year + 1):
        # Para cada año, generar todos los días del año
        year_start = datetime(year, 1, 1)
        year_end = datetime(year, 12, 31)
        
        current_date = year_start
        while current_date <= year_end:
            date_str = current_date.strftime('%Y-%m-%d')
            count = daily_activity.get(date_str, 0)
            
            # Marcar el 30 de noviembre de 2022 (día que salió ChatGPT)
            special_level = None
            if date_str == '2022-11-30':
                special_level = 'launch'  # Nivel especial para el lanzamiento
            
            github_data.append({
                'date': date_str,
                'count': count,
                'level': get_activity_level(count),
                'special_level': special_level
            })
            
            current_date += timedelta(days=1)
    
    return github_data

def get_activity_level(count):
    """Determina el nivel de actividad para el color"""
    if count == 0:
        return 0
    elif count <= 2:
        return 1
    elif count <= 5:
        return 2
    elif count <= 10:
        return 3
    else:
        return 4

if __name__ == "__main__":
    # Procesar datos
    stats = parse_conversations('conversations.json')
    
    # Generar datos para gráfico GitHub
    github_data = generate_github_style_data(stats['daily_activity'])
    stats['github_style_data'] = github_data
    
    # Guardar estadísticas
    with open('chatgpt_stats.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    print("Estadísticas guardadas en chatgpt_stats.json")
