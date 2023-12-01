# Phiziks
В папке проекта создаём образ докера:
  sudo docker build -t phiz .
запускаем докер:
  xhost +local:docker
  sudo docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix phiz


чат

stages:
  - build
  - deploy

variables:
  DOCKER_IMAGE_NAME: phiz
  DOCKER_REGISTRY: registry.gitlab.com
  DOCKER_IMAGE_TAG: latest

before_script:
  - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $DOCKER_REGISTRY

build:
  stage: build
  script:
    - docker build -t $DOCKER_REGISTRY/$CI_PROJECT_NAMESPACE/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG .

deploy:
  stage: deploy
  script:
    - sudo docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --rm $DOCKER_REGISTRY/$CI_PROJECT_NAMESPACE/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG
