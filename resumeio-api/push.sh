#!/bin/bash
echo "Version is set to $1"
mvn clean package -DskipTests
docker build -t resumeio-api:"$1" .
docker tag resumeio-api:"$1" galudas/resumeio:resumeio-api."$1"
docker push galudas/resumeio:resumeio-api."$1"