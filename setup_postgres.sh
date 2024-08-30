#!/bin/bash

# Variables
DB_NAME="thepythonstore"
DB_USER="thepythonstoreuser"
DB_PASSWORD="yourpassword"

# Verificar si PostgreSQL está instalado
if ! command -v psql > /dev/null; then
  echo "PostgreSQL no está instalado. Instalando PostgreSQL..."
  sudo apt update && sudo apt install -y postgresql postgresql-contrib
else
  echo "PostgreSQL ya está instalado."
fi

# Comprobar si la base de datos ya existe
DB_EXIST=$(sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME'")
if [ "$DB_EXIST" == "1" ]; then
  echo "La base de datos '$DB_NAME' ya existe. Saltando creación de la base de datos."
else
  # Crear base de datos
  echo "Creando base de datos '$DB_NAME'..."
  sudo -u postgres psql -c "CREATE DATABASE $DB_NAME;"
fi

# Comprobar si el usuario ya existe
USER_EXIST=$(sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='$DB_USER'")
if [ "$USER_EXIST" == "1" ]; then
  echo "El usuario '$DB_USER' ya existe. Saltando creación de usuario."
else
  # Crear usuario
  echo "Creando usuario '$DB_USER'..."
  sudo -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
  # Otorgar privilegios al usuario sobre la base de datos
  sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
fi

# Confirmación
echo "Configuración completada con éxito. Base de datos '$DB_NAME' y usuario '$DB_USER' creados."
