# Docker Documentation

## Overview

An underlying technology for this entire project is Docker. Docker is a containerization/sandboxing program that allows multiple Linux boxes to be instantiated on one computer. The primary reason we are using Docker is because NCAR/UCAR has produced a Docker Image which has WRF-HYDRO and all its dependncies prebuilt. Docker also operates as our version management/back up system. [The official "Getting Started" by Docker](https://docs.docker.com/get-started/) 

### Images

Images are what Docker Containers are insantiated out of, multiple containers can be made from one Image. Images can not be changed. The primary image we are concrned with is NCAR/UCAR's _WRFHYDROTRAINING_ image. The commands for insantiating a Docker Contianer from an Image are as follows

_To list the available images_
``` 
sudo docker images 
sudo docker image ls
```
_To start an image_
```
docker run <image>
docker run -- name <name> <image>
```
_Replace \<image> with the name of the image and \<name> with the desired name of the container. Both commands have the same effect, the second just allows naming the container._

## Containers
Containers can be though of as Virtual Machines(VMs) The main difference between VMs and Containers is that VMs run on their own Linux Kernel while all Containers use the host machines Kernel. More about Containers vs VMs can be found [here](https://www.backblaze.com/blog/vm-vs-containers/) At the end of the day each contianer can be though of as a virtual Linux box running whatever OS/Program the Image it came from had. 

Steps for Starting a Docker Container
```bash
docker ps -a # This lists all the running processes
docker start <container>
docker exec -it <container> <program>
```
_Replace \<container> with the name of the container and \<program>  

