#!/bin/bash

# $1 expect the (p)hash value of image
# copy images of the same hash value to a dedicated folder
echo 'process' $1
csvsql --query "select distinct file from 'data' where feature='$1'" data.csv > $1.txt
rm -rf similar_folder 
mkdir -p similar_folder
cd download_1
sed '1d' ../$1.txt | xargs -I % sh -c 'cp % ../similar_folder' 
cd .. && open similar_folder

