# Phiziks
В папке проекта создаём образ докера:
  sudo docker build -t phiz .
запускаем докер:
  xhost +local:docker
  sudo docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix phiz


чат

Running with gitlab-runner 16.6.1 (f5da3c5a)
  on 1 Sze9i6yxn, system ID: s_6ea0a7daf4dd
Preparing the "docker" executor 00:03
Using Docker executor with image phiz ...
Pulling docker image phiz ...
WARNING: Failed to pull image with policy "always": Error response from daemon: pull access denied for phiz, repository does not exist or may require 'docker login': denied: requested access to the resource is denied (manager.go:250:1s)
ERROR: Job failed: failed to pull image "phiz" with specified policies [always]: Error response from daemon: pull access denied for phiz, repository does not exist or may require 'docker login': denied: requested access to the resource is denied (manager.go:250:1s)

Enter an executor: ssh, virtualbox, docker+machine, kubernetes, shell, docker-autoscaler, instance, custom, docker, docker-windows, parallels:


curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash


This job is stuck because the project doesn't have any runners online assigned to it.
Go to project CI settings


stages:
  - build
  - deploy

variables:
  DOCKER_IMAGE_NAME: phiz
  DOCKER_REGISTRY: registry.gitlab.com
  DOCKER_IMAGE_TAG: latest

before_script:
  - docker login -u $CI_JOB_TOKEN -p $CI_JOB_TOKEN $DOCKER_REGISTRY

build:
  stage: build
  script:
    - docker build -t $DOCKER_REGISTRY/$CI_PROJECT_NAMESPACE/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG .

deploy:
  stage: deploy
  script:
    - sudo docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --rm $DOCKER_REGISTRY/$CI_PROJECT_NAMESPACE/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG
