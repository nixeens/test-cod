#!/bin/bash
set -e

git init
git branch -M main
if ! git remote | grep -q origin; then
    git remote add origin git@github.com:nixeens/somethingels.git
fi

git add .
if ! git diff --cached --quiet; then
    git commit -m "Deploy project"
fi

git push -u origin main
