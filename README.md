## ResumeIO
###  A place where your resume is analysed

### Useful Commands

Description  | Command
------------- | -------------
Check Health of pods  | `kubectl get pods`
Apply services  | `kubectl apply -f kube/`
Restart pod  | `kubectl rollout restart deployment <name>`
Get link of service  | `minikube service <name>`
Get logs | `kubectl logs <name>`

//TODO -> rename `resumeio-app` in `resumeio-api`
//TODO -> nodurile pe retele diferite
//TODO -> utilizat secrete pentru date sensibile
//TODO -> Rancher sau Portainer? 