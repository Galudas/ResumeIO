#!/bin/bash
echo "Version is set to $1"
docker build -t resumeio-model:"$1" .
docker tag resumeio-model:"$1" galudas/resumeio:resumeio-model."$1"
docker push galudas/resumeio:resumeio-model."$1"