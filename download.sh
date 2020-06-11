#!/bin/bash

for i in {1..10}
do
./avatar_dl -i sample100k.csv -d download_${i}
done
