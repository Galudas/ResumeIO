#!/bin/bash

minikube delete
minikube start
kubectl apply -f kube/