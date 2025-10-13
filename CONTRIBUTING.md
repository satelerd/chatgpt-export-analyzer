# Guía de Contribución 🤝

¡Gracias por tu interés en contribuir a ChatGPT Data Explorer! Este documento te guiará a través del proceso de contribución.

## 🚀 Cómo Contribuir

### 1. Fork del Repositorio
1. Ve a [GitHub](https://github.com/satelerd/chatgpt-export-analyzer)
2. Haz clic en "Fork" en la esquina superior derecha
3. Clona tu fork localmente:
```bash
git clone https://github.com/tu-usuario/chatgpt-export-analyzer.git
cd chatgpt-export-analyzer
```

### 2. Configurar el Entorno de Desarrollo
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar setup automático
python setup.py

# Ejecutar el servidor
python app.py
```

### 3. Crear una Rama
```bash
git checkout -b feature/nueva-funcionalidad
# o
git checkout -b fix/correccion-bug
```

### 4. Hacer Cambios
- Modifica el código según sea necesario
- Asegúrate de que tu código siga las convenciones del proyecto
- Prueba tus cambios localmente

### 5. Commit y Push
```bash
git add .
git commit -m "feat: agregar nueva funcionalidad"
git push origin feature/nueva-funcionalidad
```

### 6. Crear Pull Request
1. Ve a tu fork en GitHub
2. Haz clic en "New Pull Request"
3. Describe tus cambios claramente
4. Espera la revisión

## 📋 Tipos de Contribuciones

### 🐛 Reportar Bugs
- Usa el template de issue para bugs
- Incluye pasos para reproducir
- Especifica tu sistema operativo y versión de Python
- Incluye logs de error si es posible

### ✨ Sugerir Nuevas Funcionalidades
- Usa el template de issue para features
- Describe la funcionalidad detalladamente
- Explica por qué sería útil
- Considera la complejidad de implementación

### 🔧 Mejoras de Código
- Optimizaciones de rendimiento
- Refactoring para mejor legibilidad
- Mejoras en la documentación
- Nuevos tests

### 🎨 Mejoras de UI/UX
- Nuevos temas visuales
- Mejoras en responsive design
- Nuevos gráficos o visualizaciones
- Mejoras en la experiencia de usuario

## 🛠️ Estructura del Proyecto

```
chatgpt-export-analyzer/
├── app.py                 # Servidor Flask principal
├── chatgpt_parser.py     # Parser de datos de ChatGPT
├── advanced_report.html  # Template del reporte
├── index.html           # Landing page
├── requirements.txt     # Dependencias Python
├── setup.py            # Script de configuración
├── README.md           # Documentación principal
├── CONTRIBUTING.md     # Esta guía
├── LICENSE            # Licencia MIT
└── .gitignore         # Archivos ignorados por Git
```

## 📝 Convenciones de Código

### Python
- Usa PEP 8 como guía de estilo
- Nombres de variables en snake_case
- Nombres de clases en PascalCase
- Comentarios en español para claridad

### JavaScript
- Usa camelCase para variables y funciones
- Usa PascalCase para componentes
- Comentarios en español

### HTML/CSS
- Indentación de 4 espacios
- Nombres de clases en kebab-case
- Comentarios descriptivos

## 🧪 Testing

### Pruebas Manuales
1. Ejecuta el servidor localmente
2. Sube un archivo ZIP de prueba
3. Verifica que todos los gráficos funcionen
4. Prueba en diferentes navegadores
5. Verifica la responsividad en móvil

### Pruebas Automatizadas
```bash
# Ejecutar tests (cuando estén implementados)
pytest tests/

# Verificar estilo de código
flake8 .

# Formatear código
black .
```

## 🎯 Ideas para Contribuir

### Funcionalidades Prioritarias
- [ ] Exportación de reportes en PDF
- [ ] Nuevos tipos de gráficos (barras, líneas, etc.)
- [ ] Análisis de sentimientos mejorado
- [ ] Filtros por fecha en los gráficos
- [ ] Búsqueda en conversaciones
- [ ] Temas visuales adicionales

### Mejoras Técnicas
- [ ] Tests automatizados
- [ ] CI/CD pipeline
- [ ] Docker containerization
- [ ] Optimización de rendimiento
- [ ] Mejor manejo de errores
- [ ] Logging mejorado

### Documentación
- [ ] Guía de desarrollo más detallada
- [ ] Documentación de API
- [ ] Ejemplos de uso
- [ ] Screenshots y demos
- [ ] Video tutorial

## 🔍 Proceso de Revisión

### Criterios de Aceptación
- [ ] El código funciona correctamente
- [ ] Sigue las convenciones del proyecto
- [ ] Incluye documentación si es necesario
- [ ] No rompe funcionalidad existente
- [ ] Es compatible con diferentes sistemas operativos

### Timeline de Revisión
- **Issues**: Revisión inicial en 2-3 días
- **Pull Requests**: Revisión de código en 1 semana
- **Bugs críticos**: Prioridad alta, revisión rápida

## 💬 Comunicación

### Canales de Comunicación
- **GitHub Issues**: Para bugs y features
- **GitHub Discussions**: Para preguntas generales
- **Pull Request Comments**: Para discusiones específicas de código

### Etiquetas de Issues
- `bug`: Algo no funciona
- `enhancement`: Nueva funcionalidad
- `documentation`: Mejoras en documentación
- `good first issue`: Bueno para principiantes
- `help wanted`: Se necesita ayuda
- `question`: Pregunta general

## 🏆 Reconocimiento

### Contribuidores
Todos los contribuidores serán reconocidos en:
- README.md
- Release notes
- Agradecimientos especiales

### Tipos de Contribuciones
- **Código**: Nuevas funcionalidades, correcciones
- **Documentación**: Mejoras en README, guías
- **Testing**: Reportes de bugs, pruebas
- **Diseño**: Mejoras en UI/UX
- **Traducción**: Soporte para otros idiomas

## ❓ Preguntas Frecuentes

### ¿Puedo contribuir si soy principiante?
¡Absolutamente! Busca issues marcados con `good first issue` o `help wanted`.

### ¿Necesito experiencia en Python?
No es necesario, pero ayuda. Puedes contribuir con documentación, testing, o diseño.

### ¿Cómo elijo en qué trabajar?
- Revisa los issues abiertos
- Elige algo que te interese
- Pregunta si no estás seguro

### ¿Qué pasa si mi PR es rechazado?
No te preocupes, es parte del proceso. Los maintainers te darán feedback constructivo.

## 📞 Contacto

Si tienes preguntas sobre contribuir:
- Abre un issue en GitHub
- Usa GitHub Discussions
- Menciona a los maintainers en tu issue

---

**¡Gracias por contribuir a ChatGPT Data Explorer! 🎉**

*Juntos hacemos que el análisis de datos de ChatGPT sea más accesible y poderoso.*
