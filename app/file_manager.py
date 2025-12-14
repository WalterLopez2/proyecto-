import logging
import os

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    logging.info(f"Archivo {filename} creado")

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        logging.info(f"Archivo {filename} leído")
        return content
    else:
        logging.error("Archivo no encontrado")
        return None
