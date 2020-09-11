# Nutanix Containers and Why Presentation

Here are the examples used in the **Containers and Why** meeting with the Nutanix enterprise SE team.

Using these examples, we demonstrated:

* [Run a single container](demo-admin-backend/README.md#start-a-mongodb-container) with `docker run`
* Write a [Dockerfile](demo-admin-backend/Dockerfile)
* [Build an image](demo-admin-backend/README.md#build-our-container-image) with `docker-build`
* [Push an image to a repository](demo-admin-backend/README.md#store-our-image-in-a-container-registry) with `docker push`
* [Multi-stage images](demo-admin-frontend/Dockerfile)
* [Run multi-container applications with `docker-compose`](docker-compose.md)
* [Deploy a containerized application to Kubernetes](kubernetes/README.md)
  
---

## Tutorials

1. [Build, Push and Run a python flask application with docker](demo-admin-backend/README.md)
2. [Add a React frontend to the application and run multiple containers with docker-compose](docker-compose.md)
3. [Deploy the application to Kubernetes](kubernetes/README.md)

---

## Presentation

You can view the terminal presentation by following [presentation/README.md](presentation/README.md)

---

## Awesome Tools
We also discussed these handy tools and references

### **VS Code**
In my opinion, probably the best code editor there is for building cloud-native applications.

* [**code.visualstudio.com**](https://code.visualstudio.com/)

VS Code has a vast marketplace of extensions and is what makes it most powerful. The extensions span across virtually any language, technology, framework, platforms, etc. They massively increase your productivity and quality, heck this one will even predict and write your code for you.

* [Visual Studio IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)

Some other must have extensions are:

* [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
* [Kubernetes](https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-kubernetes-tools)

### **Docker**
To build, push or run containers, you'll need to [**install docker**](https://docs.docker.com/get-docker/).

Container images are created from a `Dockerfile`. The syntax of a Dockerfile is documented in the [**dockerfile reference guide**](https://docs.docker.com/engine/reference/builder/). You can also reference [this example](demo-admin-backend/Dockerfile).

### **Docker Compose**
`docker-compose` allows you to run multi-container applications - treating each container as a service. It is installed separate from the docker engine. Check out the [**docker-compose installation guide**](https://docs.docker.com/compose/install/).

`docker-compose` syntax is different from the Dockerfile syntax, it's a `.yaml` file, typically named `docker-compose.yaml`. You can check out the [**docker compose reference guide**](https://docs.docker.com/compose/compose-file/) or use the [**docker-compose.yaml**](docker-compose.yaml) to get an understanding of the file structure

### **Kubernetes CLI**
To run a containerized application for production, you would likely be looking to deploy to a kubernetes cluster. To interact with a kubernetes cluster, you'll need to [**install `kubectl`**](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

### **Kind**
Kind provides a very fast and easy way to spin up a local kubernetes cluster, running in docker. Hence the name **K**_ubernetes_ **In** **D**_ocker_.

If you already have docker and [Go installed](https://golang.org/doc/install), then you can install kind and start a cluster in a couple minutes with the command

    GO111MODULE="on" go get sigs.k8s.io/kind@v0.8.1 && kind create cluster

It's very quick and it's really straight forward. Checkout the [**kind website**](https://kind.sigs.k8s.io/) for install and usage docs.

### **Octant**
If you're looking for a kubernetes UI, there isn't one out of the box. There are many open-source dashboards you can use, this one is just of my own preference. You can get octant from [**octant.dev**](https://octant.dev/).

Octant is written in Go, with a binary for any OS. It's open-source, free and easy to install. I should warn, however, that Octant is a **vmware** backed project. It uses vmware's same clarity UI components and therefore very much looks like a vmware product.

### **GitHub**
If you don't have a [**GitHub**](https://github.com) account, sign up for one. You can use it to version control your own docker files. Above all though, there is likely someone or some project out there that has already solved a problem yu are trying to solve. For example, if I was trying to containerize a Nutanix LCM server, the [silent198214/nutanix-lcm](https://github.com/silent198214/nutanix-lcm) project may have already done the work for me.

### **Cloud Native Computing Foundation** (CNCF)
The Cloud Native Computing Foundation (CNCF) is a Linux Foundation project that was founded in 2015 to help advance container technology and align the tech industry around its evolution.

Projects that have either graduated or in still incubating are in large part setting today/tomorrow's standards. Credibility within the container ecosystem is largely dictated by CNCF recognition.

The ecosystem of products, services and technology is vast and rapidly evolving.

* [**CNCF Interactive Landscape**](https://landscape.cncf.io/zoom=150)