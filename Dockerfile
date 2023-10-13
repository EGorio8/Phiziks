# Используйте базовый образ Ubuntu
FROM ubuntu:20.04

# Установите необходимые зависимости, включая Tkinter и xauth
RUN apt-get update && apt-get install -y python3-tk xauth

# Установите переменную среды DISPLAY
ENV DISPLAY=:0

# Создайте директорию приложения
WORKDIR /app

# Копируйте ваш код и файлы в образ
COPY main.py /app/main.py
COPY Fon31.png /app/Fon31.png
COPY shar.png /app/shar.png

# Установите команду, которая будет запущена при старте контейнера
CMD ["python3", "main.py"]
