# Phiziks
В папке проекта создаём образ докера:
  sudo docker build -t phiz .
запускаем докер:
  sudo docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix phiz
