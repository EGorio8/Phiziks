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
  DOCKER_DRIVER: overlay2
  CONTAINER_TEST_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_NAME

before_script:
  - apt-get update -qy
  - apt-get install -y python3-tk xauth

build:
  stage: build
  script:
    - python3 -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt  # Если у вас есть файл с зависимостями
    - python main.py

deploy:
  stage: deploy
  script:
    - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin $CI_REGISTRY
    - docker build -t $CONTAINER_TEST_IMAGE .
    - docker push $CONTAINER_TEST_IMAGE
    - docker run --rm $CONTAINER_TEST_IMAGE  # Запустите тесты в контейнере
