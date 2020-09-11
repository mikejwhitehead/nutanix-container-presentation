# Deploy to Kubernetes
Running our containers at scale, orchestrated across kubernetes cluster nodes

## Pre-requisites
* [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [kind](https://kind.sigs.k8s.io/)
* [Docker](https://docs.docker.com/get-docker/)
---

## In this tutorial

Previously we reviewed the steps for using docker-compose to run our multi-container application on a single host. Going a little further, we'll deploy our application stack to Kubernetes, which will orchestrate and run our containers accross an entire cluster of nodes.

---

## Start a local cluster with kind

Make sure you have `kind` installed, start a cluster with the command
```
kind cluster create
```

## Kubernetes Manifests (Templates)
Take a peek at the kubernetes manifests for our application. 
* [db deployment](manifests/demo-admin-app-db-deployment.yaml)
* [db service](manifests/demo-admin-app-db-svc.yaml)
* [db persistent volume claim](manifests/demo-admin-app-db-pvc.yaml)
* [backend deployment](manifests/demo-admin-backend-deployment.yaml)
* [backend service](manifests/demo-admin-backend-svc.yaml)
* [frontend deployment](manifests/demo-admin-frontend-deployment.yaml)
* [frontend service](manifests/demo-admin-frontend-svc.yaml)

Each manifest provides kubernetes with the declared state of the resource being requested. There are many other kinds of k8s resources and custom resources, were using just a few for our app.

## Create a Kubernetes Namespace

```
kubectl create ns demo-admin-app
kubectl config set-context --current --namespace=demo-admin-app
```

`config set-context` in the above command sets the `kubectl` default namespace to the one we created.

## Kubectl Apply
Make sure you're shells current directory is set to the kubernetes folder (`nutanix-container-presentation/kubernetes`).

Apply the kubernetes manifests
```
kubectl apply -f manifests/
```

You should see the resources being created
```
deployment.apps/demo-admin-app-db created
persistentvolumeclaim/demo-admin-app-db created
service/demo-admin-app-db created
deployment.apps/demo-admin-backend created
service/demo-admin-backend created
deployment.apps/demo-admin-frontend created
service/demo-admin-frontend created
```

Run `kubectl get all` to see our resources
```
NAME                                      READY   STATUS    RESTARTS   AGE
pod/demo-admin-app-db-7bbb4d6795-mml9k    1/1     Running   0          72s
pod/demo-admin-backend-7f54dcfcd9-7vxjc   1/1     Running   0          72s
pod/demo-admin-frontend-85698d774-gdwm6   1/1     Running   0          72s

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)     AGE
service/demo-admin-app-db     ClusterIP   10.110.86.35    <none>        27017/TCP   72s
service/demo-admin-backend    ClusterIP   10.104.243.39   <none>        80/TCP      72s
service/demo-admin-frontend   ClusterIP   10.110.78.50    <none>        80/TCP      72s

NAME                                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/demo-admin-app-db     1/1     1            1           72s
deployment.apps/demo-admin-backend    1/1     1            1           72s
deployment.apps/demo-admin-frontend   1/1     1            1           72s

NAME                                            DESIRED   CURRENT   READY   AGE
replicaset.apps/demo-admin-app-db-7bbb4d6795    1         1         1       72s
replicaset.apps/demo-admin-backend-7f54dcfcd9   1         1         1       72s
replicaset.apps/demo-admin-frontend-85698d774   1         1         1       72s
```

## Port Forwarding
Because our services were deployed with only ClusterIP, they are not accessible outside of our cluster. Use port forwarding to bind a service port to a port on the host. Make sure your pods are running with `kubectl get pods`
```
kubectl port-forward service/demo-admin-frontend 8080:80
```
You should now be able to view our applications frontend at http://localhost:8080


You should see our containers building, followed by something like
```
Successfully tagged nutanix-container-presentation_demo-admin-app-frontend:latest
Creating demo-admin-app-db ... done
Creating demo-admin-app-backend ... done
Creating demo-admin-app-frontend ... done
```

## Check the logs
If you want to see what is being logged by our containers (stderr/stdout)
```
kubectl logs -f -l app=demo-admin-app
```

---

## Wrapping Up
To remove our resources and stop kind, run
```
kubectl delete -f manifests/
kind delete cluster
```





