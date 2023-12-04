# Phiziks
В папке проекта создаём образ докера:
  sudo docker build -t phiz .
запускаем докер:
  xhost +local:docker
  sudo docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix phiz


чат

_tkinter.TclError: couldn't connect to display ":0" ERROR: Job 


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
  DOCKER_DRIVER: overlay2

before_script:
  - apt-get update -qy
  - apt-get install -y docker.io
  - docker info
  - usermod -aG docker $USER  # Add the current user to the docker group
  - newgrp docker  # Activate the changes to the group membership

build_image:
  stage: build
  script:
    - docker build -t my-python-app .
    - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" $CI_REGISTRY
    - docker push $CI_REGISTRY_IMAGE

deploy_app:
  stage: deploy
  script:
    - docker pull $CI_REGISTRY_IMAGE
    - docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --rm $CI_REGISTRY_IMAGE
-----

import time
import math
import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.timeout(100)

    height, width = stdscr.getmaxyx()
    y = 10  # начальная высота
    x = width // 2  # середина экрана

    # Фон и шар
    nebo_img = [[' ' for _ in range(width)] for _ in range(height)]
    shar_img = [
        '         @         ',
        '        / \\        ',
        '       /___\\       ',
        '      |     |      ',
        '      |     |      ',
        '     |_____|      '
    ]

    while True:
        stdscr.clear()

        # Отрисовка фона
        for i, row in enumerate(nebo_img):
            stdscr.addstr(i, 0, ''.join(row))

        # Отрисовка шара
        for i, row in enumerate(shar_img):
            stdscr.addstr(y + i, x - len(row) // 2, row)

        y += 1

        stdscr.refresh()

        time.sleep(0.1)

        if y >= 500:
            break

try:
    curses.wrapper(main)
except KeyboardInterrupt:
    pass

