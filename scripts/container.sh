#!/bin/bash
echo "Hola desde el contenedor"
echo "HOSTNAME: $(hostname)"
echo "Archivo desde contenedor" > /app/output.txt
sleep 5
