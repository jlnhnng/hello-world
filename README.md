# Hello-World Container

This repository provides a simple container image built with Python running on Alpine Linux. The container dynamically generates an `index.html` page displaying its **name**, **IP address**, and **current time**. This image is intended for **demonstration and testing purposes**.

## Run in Docker
To start the container using Docker, run:

```bash
docker run -d -p 8080:80 ghcr.io/jlnhnng/hello-world:latest
```

This will launch the container in detached mode (`-d`), mapping port **8080 on the host** to **port 80 inside the container**.

## Run in Docker Swarm
Deploy the container in a **Docker Swarm** environment with the following command:

```bash
docker stack deploy -c - hello-world-stack <<EOF
version: '3.8'
services:
  hello-world-service:
    image: ghcr.io/jlnhnng/hello-world:latest
    ports:
      - "8080:80"
    deploy:
      replicas: 1
EOF
```

This creates a **Docker stack** with a service named `hello-world-service`, running **one replica** of the container.

## Run in Kubernetes
Deploy the container in a **Kubernetes cluster** using the following command:

```bash
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: hello-world
spec:
  containers:
    - name: hello-world
      image: ghcr.io/jlnhnng/hello-world:latest
      ports:
        - containerPort: 80
EOF
```

This creates a **Kubernetes Pod** named `hello-world`, running the container and exposing port **80** inside the pod.

---

This container is for **testing, debugging, and network visibility demos**.
