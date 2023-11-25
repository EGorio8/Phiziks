# Phiziks
В папке проекта создаём образ докера:
  sudo docker build -t phiz .
запускаем докер:
  xhost +local:docker
  sudo docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix phiz


чат

image: docker:stable

stages:
  - build

variables:
  DOCKER_DRIVER: overlay2
  IMAGE_TAG: $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG

services:
  - docker:dind

build:
  stage: build
  script:
    - docker build -t $IMAGE_TAG .
    - docker push $IMAGE_TAG
