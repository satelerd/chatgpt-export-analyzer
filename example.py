#!/usr/bin/env python3
"""
Script de ejemplo para probar el analizador con datos de muestra
"""

import json
import os
from datetime import datetime, timedelta
import random

def create_sample_data():
    """Crea datos de muestra para probar el analizador"""
    
    # Crear directorio de ejemplo
    os.makedirs('sample_data', exist_ok=True)
    
    # Generar conversaciones de muestra
    conversations = []
    start_date = datetime(2022, 12, 1)
    
    for i in range(100):  # 100 conversaciones de muestra
        conv_date = start_date + timedelta(days=random.randint(0, 800))
        
        conversation = {
            "id": f"sample_conv_{i:03d}",
            "title": f"Conversación de muestra {i+1}",
            "create_time": int(conv_date.timestamp()),
            "update_time": int(conv_date.timestamp()),
            "mapping": {}
        }
        
        # Agregar algunos mensajes de muestra
        for j in range(random.randint(2, 10)):
            msg_id = f"msg_{j}"
            msg_time = conv_date + timedelta(minutes=j*5)
            
            # Mensaje del usuario
            user_msg = {
                "id": f"{msg_id}_user",
                "author": {"role": "user"},
                "create_time": int(msg_time.timestamp()),
                "content": {
                    "content_type": "text",
                    "parts": [f"Este es un mensaje de muestra {j+1} del usuario."]
                }
            }
            
            # Mensaje de ChatGPT
            chatgpt_msg = {
                "id": f"{msg_id}_assistant",
                "author": {"role": "assistant"},
                "create_time": int((msg_time + timedelta(minutes=1)).timestamp()),
                "content": {
                    "content_type": "text",
                    "parts": [f"Esta es una respuesta de muestra {j+1} de ChatGPT."]
                }
            }
            
            conversation["mapping"][f"{msg_id}_user"] = {"message": user_msg}
            conversation["mapping"][f"{msg_id}_assistant"] = {"message": chatgpt_msg}
        
        conversations.append(conversation)
    
    # Guardar conversations.json
    with open('sample_data/conversations.json', 'w', encoding='utf-8') as f:
        json.dump(conversations, f, indent=2, ensure_ascii=False)
    
    # Crear user.json de muestra
    user_data = {
        "email": "usuario@ejemplo.com",
        "chatgpt_plus": True,
        "birth_year": 1990,
        "phone": "+1234567890"
    }
    
    with open('sample_data/user.json', 'w', encoding='utf-8') as f:
        json.dump(user_data, f, indent=2, ensure_ascii=False)
    
    # Crear message_feedback.json de muestra
    feedback_data = []
    for i in range(50):
        feedback_data.append({
            "message_id": f"msg_{i}_assistant",
            "rating": random.choice(["thumbs_up", "thumbs_down"]),
            "timestamp": int((start_date + timedelta(days=random.randint(0, 800))).timestamp())
        })
    
    with open('sample_data/message_feedback.json', 'w', encoding='utf-8') as f:
        json.dump(feedback_data, f, indent=2, ensure_ascii=False)
    
    print("✅ Datos de muestra creados en 'sample_data/'")
    print("📁 Archivos generados:")
    print("   - conversations.json")
    print("   - user.json")
    print("   - message_feedback.json")
    print("\n🚀 Para probar el analizador:")
    print("   python3 main.py sample_data/")

if __name__ == '__main__':
    create_sample_data()
