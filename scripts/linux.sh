#!/bin/bash
set -e
echo "Archivo Linux" > linux.txt
chmod 600 linux.txt
sleep 2
if [ ! -f linux.txt ]; then exit 1; fi
