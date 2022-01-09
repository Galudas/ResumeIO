#!/bin/bash
echo "Version is set to $1"
rm -rf build/
npm run-script build
docker build -t resumeio-frontend:"$1" .
docker tag resumeio-frontend:"$1" galudas/resumeio:resumeio-frontend."$1"
docker push galudas/resumeio:resumeio-frontend."$1"