# ResumeIO

## A place where your resume is analysed

### Set up

* Install `Conda`

  https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
* Run `export FLASK_ENV=development` locally
### Useful Commands

| Description                       | Command                                      |
|-----------------------------------|----------------------------------------------|
| Check Health of pods              | `kubectl get pods`                           |
| Apply services                    | `kubectl apply -f kube/`                     |
| Restart pod                       | `kubectl rollout restart deployment <name>`  |
| Get link of service               | `minikube service <name>`                    |
| Get logs                          | `kubectl logs <name>`                        |
| Port Forward to visualize prod db | `kubectl port-forward <pod-name> 54321:5432` |
| Create virtual environment        | `conda env create -f <env file>`             |
| Update environment                | `conda env update --file <env file> --prune` |

//TODO -> rename `resumeio-app` in `resumeio-api`
//TODO -> nodurile pe retele diferite //TODO -> utilizat secrete pentru date sensibile //TODO -> Rancher sau Portainer?

In case needed
https://www.bogotobogo.com/DevOps/Docker/Docker_Kubernetes_MongoDB_MongoExpress.php