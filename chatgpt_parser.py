#!/usr/bin/env python3
"""
ChatGPT Analytics Pro - Parser Generalizado
Parser avanzado para extraer estadísticas del export de ChatGPT
Compatible con cualquier usuario y estructura de datos
"""

import json
import re
import os
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import calendar
import math
import statistics
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Importaciones opcionales para análisis avanzado
try:
    from textblob import TextBlob
    TEXTBLOB_AVAILABLE = True
except ImportError:
    TEXTBLOB_AVAILABLE = False
    print("⚠️  TextBlob no disponible. El análisis de sentimientos estará limitado.")

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    
    # Descargar recursos de NLTK si no están disponibles
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)
    
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False
    print("⚠️  NLTK no disponible. El análisis de texto estará limitado.")

class ChatGPTParser:
    """Parser generalizado para datos de ChatGPT"""
    
    def __init__(self, data_dir="."):
        self.data_dir = Path(data_dir)
        self.stats = self._initialize_stats()
    
    def parse_and_analyze(self, conversations_file, user_file=None):
        """Método principal para parsear y analizar datos"""
        print(f"📂 Cargando conversaciones desde: {conversations_file}")
        
        # Guardar rutas de archivos
        self.conversations_file = conversations_file
        self.data_dir = Path(conversations_file).parent
        if user_file:
            self.user_file = user_file
        
        # Procesar conversaciones
        print("⚙️ Procesando conversaciones...")
        self.process_conversations()
        
        # Convertir defaultdicts a dicts normales para JSON
        print("🔄 Convirtiendo estadísticas para JSON...")
        return self._convert_stats_for_json()
    
    def _convert_stats_for_json(self):
        """Convierte defaultdicts a dicts normales para serialización JSON"""
        converted_stats = {}
        for key, value in self.stats.items():
            if isinstance(value, defaultdict):
                converted_stats[key] = dict(value)
            elif isinstance(value, dict):
                converted_stats[key] = {}
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, defaultdict):
                        converted_stats[key][sub_key] = dict(sub_value)
                    else:
                        converted_stats[key][sub_key] = sub_value
            else:
                converted_stats[key] = value
        return converted_stats
        
    def _initialize_stats(self):
        """Inicializa la estructura de estadísticas"""
        return {
            # Estadísticas básicas
            'total_conversations': 0,
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
            'correlation_data': defaultdict(float),
            
            # Análisis de días activos/inactivos
            'days_analysis': {},
            'cumulative_data': []
        }
    
    def find_conversations_file(self):
        """Busca el archivo conversations.json en el directorio"""
        conversations_file = self.data_dir / "conversations.json"
        if conversations_file.exists():
            return conversations_file
        
        # Buscar en subdirectorios
        for file_path in self.data_dir.rglob("conversations.json"):
            return file_path
        
        return None
    
    def load_conversations(self):
        """Carga las conversaciones desde el archivo JSON"""
        # Si tenemos la ruta directa del archivo, usarla
        if hasattr(self, 'conversations_file') and self.conversations_file:
            conversations_file = self.conversations_file
        else:
            conversations_file = self.find_conversations_file()
            if not conversations_file:
                raise FileNotFoundError("No se encontró conversations.json")
        
        print(f"📂 Cargando conversaciones desde: {conversations_file}")
        
        # Verificar tamaño del archivo
        file_size = os.path.getsize(conversations_file)
        print(f"📊 Tamaño del archivo: {file_size / (1024*1024):.2f} MB")
        
        # Si el archivo es muy grande, usar lectura por chunks
        if file_size > 100 * 1024 * 1024:  # 100MB
            print("⚠️ Archivo muy grande, usando lectura optimizada...")
            return self._load_conversations_chunked(conversations_file)
        
        with open(conversations_file, 'r', encoding='utf-8') as f:
            conversations = json.load(f)
        
        print(f"✅ {len(conversations)} conversaciones cargadas")
        return conversations
    
    def _load_conversations_chunked(self, conversations_file):
        """Carga conversaciones por chunks para archivos grandes"""
        print("📦 Iniciando carga por chunks...")
        
        conversations = []
        chunk_size = 1000  # Procesar de a 1000 conversaciones
        
        try:
            with open(conversations_file, 'r', encoding='utf-8') as f:
                # Leer el archivo completo pero procesar por chunks
                data = json.load(f)
                
                if isinstance(data, list):
                    total = len(data)
                    print(f"📊 Total de conversaciones encontradas: {total}")
                    
                    # Procesar todas las conversaciones (sin límite artificial)
                    conversations = data
                    print(f"📊 Procesando todas las {total} conversaciones")
                else:
                    conversations = [data] if data else []
            
            print(f"✅ {len(conversations)} conversaciones cargadas (optimizado)")
            return conversations
            
        except Exception as e:
            print(f"❌ Error cargando conversaciones: {str(e)}")
            # Fallback: intentar cargar solo las primeras líneas
            return self._load_conversations_fallback(conversations_file)
    
    def _load_conversations_fallback(self, conversations_file):
        """Fallback para cargar conversaciones cuando falla la carga normal"""
        print("🔄 Intentando carga de emergencia...")
        
        try:
            # Leer solo las primeras líneas del archivo
            with open(conversations_file, 'r', encoding='utf-8') as f:
                lines = []
                for i, line in enumerate(f):
                    if i >= 10000:  # Máximo 10k líneas
                        break
                    lines.append(line)
            
            # Intentar parsear como JSON
            content = ''.join(lines)
            if content.strip().startswith('['):
                # Es una lista, buscar el cierre
                if not content.strip().endswith(']'):
                    content = content.rstrip(',\n') + ']'
            
            conversations = json.loads(content)
            print(f"✅ {len(conversations)} conversaciones cargadas (fallback)")
            return conversations
            
        except Exception as e:
            print(f"❌ Error en fallback: {str(e)}")
            return []
    
    def extract_text_content(self, content):
        """Extrae texto del contenido de un mensaje"""
        if isinstance(content, str):
            return content
        elif isinstance(content, dict):
            if 'parts' in content and content['parts']:
                return content['parts'][0] if isinstance(content['parts'][0], str) else str(content['parts'][0])
            elif 'text' in content:
                return content['text']
        return str(content)
    
    def analyze_sentiment(self, text):
        """Analiza el sentimiento del texto (optimizado)"""
        if not TEXTBLOB_AVAILABLE or not text.strip() or len(text) < 20:
            return 0.0
        
        try:
            blob = TextBlob(text)
            return blob.sentiment.polarity
        except:
            return 0.0
    
    def analyze_content_advanced(self, text, stats):
        """Análisis avanzado del contenido del texto (optimizado)"""
        if not text or len(text) < 10:  # Skip textos muy cortos
            return
            
        text_lower = text.lower()
        
        # Términos técnicos (solo los más comunes para mejor rendimiento)
        tech_terms = ['python', 'javascript', 'api', 'database', 'function', 'code']
        
        for term in tech_terms:
            if term in text_lower:
                stats['technical_terms'][term] += 1
        
        # Lenguajes de programación (solo los principales)
        prog_langs = ['python', 'javascript', 'java', 'html', 'css', 'sql']
        
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
    
    def get_activity_level(self, count):
        """Determina el nivel de actividad basado en el conteo"""
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
    
    def generate_github_style_data(self, daily_activity):
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
                    'level': self.get_activity_level(count),
                    'special_level': special_level
                })
                
                current_date += timedelta(days=1)
        
        return github_data
    
    def analyze_active_days(self, daily_activity, first_date, last_date):
        """Analiza días activos vs inactivos"""
        if not first_date or not last_date:
            return {}
        
        total_days = (last_date - first_date).days + 1
        active_days = len(daily_activity)
        inactive_days = total_days - active_days
        
        active_percentage = (active_days / total_days) * 100 if total_days > 0 else 0
        inactive_percentage = (inactive_days / total_days) * 100 if total_days > 0 else 0
        
        return {
            'total_days': total_days,
            'active_days': active_days,
            'inactive_days': inactive_days,
            'active_percentage': round(active_percentage, 2),
            'inactive_percentage': round(inactive_percentage, 2)
        }
    
    def generate_cumulative_data(self, daily_activity):
        """Genera datos acumulados para gráfico de evolución"""
        if not daily_activity:
            return []
        
        sorted_dates = sorted(daily_activity.keys())
        
        cumulative_data = []
        cumulative_conversations = 0
        
        for date_str in sorted_dates:
            daily_count = daily_activity[date_str]
            cumulative_conversations += daily_count
            
            cumulative_data.append({
                'date': date_str,
                'daily_conversations': daily_count,
                'cumulative_conversations': cumulative_conversations,
            })
        
        return cumulative_data
    
    def process_conversations(self):
        """Procesa todas las conversaciones y genera estadísticas"""
        conversations = self.load_conversations()
        
        all_dates = []
        all_message_lengths = []
        all_sentiment_scores = []
        
        print("⚙️  Procesando conversaciones...")
        
        import time
        start_time = time.time()
        
        # Procesar todas las conversaciones
        total_conversations = len(conversations)
        print(f"📊 Procesando {total_conversations} conversaciones")
        
        for i, conversation in enumerate(conversations):
            if i % 1000 == 0 and i > 0:
                elapsed = time.time() - start_time
                print(f"   Procesadas {i}/{total_conversations} conversaciones... ({elapsed:.1f}s)")
            
            # Información básica de la conversación
            conv_id = conversation.get('id', f'conv_{i}')
            create_time = conversation.get('create_time', 0)
            title = conversation.get('title', 'Sin título')
            
            if create_time:
                conv_date = datetime.fromtimestamp(create_time)
                date_str = conv_date.strftime('%Y-%m-%d')
                hour = conv_date.hour
                month = conv_date.strftime('%Y-%m')
                weekday = conv_date.strftime('%A')
                year = conv_date.year
                
                all_dates.append(conv_date)
                
                # Actividad temporal
                self.stats['daily_activity'][date_str] += 1
                self.stats['hourly_activity'][hour] += 1
                self.stats['monthly_activity'][month] += 1
                self.stats['weekly_activity'][weekday] += 1
                self.stats['yearly_activity'][year] += 1
                
                # Heatmap data
                self.stats['heatmap_data'][weekday][hour] += 1
            
            # Procesar mensajes
            mapping = conversation.get('mapping', {})
            message_count = 0
            
            for msg_id, msg_data in mapping.items():
                if msg_data.get('message'):
                    message = msg_data['message']
                    content = message.get('content', {})
                    role = message.get('author', {}).get('role', 'unknown')
                    
                    # Extraer texto
                    text = self.extract_text_content(content)
                    if text:
                        message_count += 1
                        self.stats['total_messages'] += 1
                        
                        # Análisis de texto
                        words = text.split()
                        self.stats['total_words'] += len(words)
                        self.stats['total_characters'] += len(text)
                        
                        all_message_lengths.append(len(text))
                        
                        # Frecuencia de palabras
                        if NLTK_AVAILABLE:
                            try:
                                tokens = word_tokenize(text.lower())
                                stop_words = set(stopwords.words('spanish') + stopwords.words('english'))
                                filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
                                self.stats['word_frequency'].update(filtered_tokens)
                            except:
                                # Fallback simple
                                words_lower = [word.lower() for word in words if word.isalpha()]
                                self.stats['word_frequency'].update(words_lower)
                        
                        # Análisis de sentimientos
                        sentiment = self.analyze_sentiment(text)
                        all_sentiment_scores.append(sentiment)
                        
                        if sentiment > 0.1:
                            self.stats['positive_messages'] += 1
                        elif sentiment < -0.1:
                            self.stats['negative_messages'] += 1
                        else:
                            self.stats['neutral_messages'] += 1
                        
                        # Análisis avanzado
                        self.analyze_content_advanced(text, self.stats)
                        
                        # Patrones de pregunta
                        if text.strip().endswith('?'):
                            self.stats['question_patterns']['preguntas'] += 1
                        
                        # Código y URLs
                        if '```' in text:
                            self.stats['code_blocks'] += 1
                        if 'http' in text.lower():
                            self.stats['urls_shared'] += 1
            
            # Estadísticas de conversación
            self.stats['conversation_lengths'].append(message_count)
            self.stats['conversation_titles'].append(title)
            
            if message_count > self.stats['longest_conversation']:
                self.stats['longest_conversation'] = message_count
            if message_count < self.stats['shortest_conversation']:
                self.stats['shortest_conversation'] = message_count
        
        # Calcular estadísticas finales
        self._calculate_final_stats(all_dates, all_message_lengths, all_sentiment_scores)
        
        total_time = time.time() - start_time
        print(f"✅ Procesamiento completado en {total_time:.2f} segundos")
        return self.stats
    
    def _calculate_final_stats(self, all_dates, all_message_lengths, all_sentiment_scores):
        """Calcula estadísticas finales"""
        # Estadísticas básicas
        self.stats['total_conversations'] = len(self.stats['conversation_lengths'])
        
        if all_message_lengths:
            self.stats['avg_message_length'] = statistics.mean(all_message_lengths)
            self.stats['longest_message'] = max(all_message_lengths)
            self.stats['shortest_message'] = min(all_message_lengths)
            self.stats['avg_words_per_message'] = self.stats['total_words'] / len(all_message_lengths)
        
        if all_dates:
            self.stats['first_conversation'] = min(all_dates).strftime('%Y-%m-%d')
            self.stats['last_conversation'] = max(all_dates).strftime('%Y-%m-%d')
            
            # Análisis de días activos/inactivos
            self.stats['days_analysis'] = self.analyze_active_days(
                self.stats['daily_activity'], min(all_dates), max(all_dates)
            )
            
            # Datos acumulados
            self.stats['cumulative_data'] = self.generate_cumulative_data(self.stats['daily_activity'])
            
            # Métricas de productividad
            date_range = (max(all_dates) - min(all_dates)).days
            if date_range > 0:
                self.stats['conversations_per_day'] = self.stats['total_conversations'] / date_range
                self.stats['messages_per_day'] = self.stats['total_messages'] / date_range
                self.stats['words_per_day'] = self.stats['total_words'] / date_range
        
        if self.stats['conversation_lengths']:
            self.stats['avg_conversation_length'] = statistics.mean(self.stats['conversation_lengths'])
        
        # Encontrar períodos más activos
        if self.stats['daily_activity']:
            self.stats['most_active_day'] = max(self.stats['daily_activity'], key=self.stats['daily_activity'].get)
        if self.stats['hourly_activity']:
            self.stats['most_active_hour'] = max(self.stats['hourly_activity'], key=self.stats['hourly_activity'].get)
        if self.stats['monthly_activity']:
            self.stats['most_active_month'] = max(self.stats['monthly_activity'], key=self.stats['monthly_activity'].get)
    
    def save_stats(self, output_file="chatgpt_stats.json"):
        """Guarda las estadísticas en un archivo JSON"""
        output_path = self.data_dir / output_file
        
        # Convertir defaultdict y Counter a dict/list para JSON
        stats_json = {}
        for key, value in self.stats.items():
            if isinstance(value, defaultdict):
                stats_json[key] = dict(value)
            elif isinstance(value, Counter):
                stats_json[key] = dict(value)
            else:
                stats_json[key] = value
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(stats_json, f, ensure_ascii=False, indent=2, default=str)
        
        print(f"💾 Estadísticas guardadas en: {output_path}")
        return output_path

def main():
    """Función principal para ejecutar el parser"""
    import argparse
    
    parser = argparse.ArgumentParser(description="ChatGPT Analytics Pro - Parser")
    parser.add_argument("--data-dir", default=".", help="Directorio con los datos de ChatGPT")
    parser.add_argument("--output", default="chatgpt_stats.json", help="Archivo de salida")
    
    args = parser.parse_args()
    
    print("🚀 ChatGPT Analytics Pro - Parser")
    print("=" * 50)
    
    try:
        # Crear parser
        chatgpt_parser = ChatGPTParser(args.data_dir)
        
        # Procesar conversaciones
        stats = chatgpt_parser.process_conversations()
        
        # Guardar estadísticas
        output_path = chatgpt_parser.save_stats(args.output)
        
        print("\n✅ Procesamiento completado exitosamente")
        print(f"📊 Estadísticas generadas: {stats['total_conversations']} conversaciones")
        print(f"💬 Total de mensajes: {stats['total_messages']}")
        print(f"📝 Total de palabras: {stats['total_words']}")
        print(f"💾 Archivo guardado: {output_path}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
