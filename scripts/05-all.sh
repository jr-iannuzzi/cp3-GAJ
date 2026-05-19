#!/bin/bash

echo "Criando rede..."
bash 01-network.sh

echo "Criando volume..."
bash 02-volume.sh

echo "Subindo MySQL..."
bash 03-mysql.sh

echo "Subindo API..."
bash 04-api.sh

echo "Tudo rodando!"
docker ps