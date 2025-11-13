#!/bin/bash

# Script de Inicio Rápido - RPM API

echo "🚀 Iniciando RPM API + Frontend..."
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python no está instalado"
    exit 1
fi

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -q -r requirements.txt

# Iniciar servidor
echo ""
echo "✅ ¡Servidor iniciado!"
echo ""
echo "📍 Accede a las siguientes URLs:"
echo "   🔐 Login/Registro:  http://localhost:5000/"
echo "   📦 CRUD Productos:  http://localhost:5000/crud"
echo ""
echo "⚠️  El servidor debe estar ejecutándose en puerto 5000"
echo "🔴 Presiona Ctrl+C para detener el servidor"
echo ""

# Ejecutar Flask
python main.py
