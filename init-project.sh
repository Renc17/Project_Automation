#!/bin/bash

python create.py $1
source .env
cd $WORKING_DIR
git init
git add .
git commit -m "Added README.md"

git remote add origin $CLONE_URL
git branch -M main
git push -u origin main