#!/bin/bash

cd ../app

docker build -t app-cp3 .

docker run -d \
  --name api-cp3 \
  --network dimdim-network \
  -p 5000:5000 \
  app-cp3