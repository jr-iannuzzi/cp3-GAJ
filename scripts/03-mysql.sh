#!/bin/bash

docker run -d \
  --name mysql-cp3 \
  --network dimdim-network \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -e MYSQL_DATABASE=dimdim \
  -p 3306:3306 \
  -v mysql-volume:/var/lib/mysql \
  mysql:8

echo "Aguardando MySQL iniciar..."
sleep 15

docker exec -i mysql-cp3 mysql -u root -p123456 < ../database/init.sql