# AWN Term Project

## Part1: Router

### To start with Docker

##### Build images.

```
cd router/docker
docker network create my-routing
cd server
docker build -t server:latest .
cd ../router
docker build -t router:latest .
```

##### Run server.
```
docker run --rm --name server -p 8001:8001 --network my-routing server
```
##### Run router.
```
docker run --rm --name router -p 8201:8201 --network my-routing router
```
##### Run clients.
```
cd router/docker/client
python client_1.py
python client_2.py
python client_3.py
```

### To start with Kubernetes

##### Build images.

```
cd router/kubernetes
cd server
docker build -t server:latest .
cd ../router
docker build -t router:latest .
```

##### Run server.
```
cd router/kubernetes
cd server
kubectl apply -f=server-deployment.yaml
```
##### Run router.
```
cd router/kubernetes
cd router
kubectl apply -f=router-deployment.yaml
```
>> You can list deployments and services by ``` kubectl get deploy,svc```
##### Run clients.
###### First, get the external IP of router by ```minikube service router```
#
```
cd router/kubernetes
cd client
```
###### Edit the router IP in client_1.py, client_2.py, client_3.py before executing the following command.
#
```
python client_1.py
python client_2.py
python client_3.py
```

---
## Part2: Proxy
### To start with Docker

##### Build images.

```
cd proxy/docker
docker build -t proxy:latest .
```
##### Run proxy.
```
docker run --rm --name proxy -p 8080:8080 proxy
```
##### Now proxy service is at localhost, port8080.

### To start with Kubernetes

##### Build images.
###### First, create repositories on dockerhub, ex: proxy.
#
```
docker login
//enter your dockerhub username and password
cd proxy/docker
docker build -t {dockerhubUserName}/{dockerhubRepoName}:latest .
docker push {dockerhubUserName}/{dockerhubRepoName}
```

##### Run proxy.
```
cd proxy/kubernetes
kubectl apply -f=proxy-deployment.yaml
```
>> You can list deployments and services by ``` kubectl get deploy,svc```
##### Apply Horizontal Pod Autoscaling on proxy.
```
cd proxy/kubernetes
kubectl apply -f=proxy-hpa.yaml
```
>> To check the autoscaler:
>> list autoscalers by ```kubectl get hpa```
>> To stop the autoscaler: ```kubectl delete hpa/proxy```
##### Apply Vertical Pod Autoscaling on proxy.
```
cd proxy/kubernetes
kubectl apply -f=proxy-vpa.yaml
```
>> To check the autoscaler:
>> list autoscalers by ```kubectl get vpa```
>> get detailed description by ```kubectl describe vpa proxy```
>> To stop the autoscaler: ```kubectl delete vpa/proxy```