from tkinter import *
import time
import math

#Окно
root = Tk()
root.title('Полёт_Шара')
root.geometry('500x600')
root.resizable(width=False, height=False)

#Фон
my_canvas = Canvas(root, width=500, height=600, bg='black')
my_canvas.pack()

nebo_img = PhotoImage(file='Fon31.png')
nebo = my_canvas.create_image(0, 600, anchor=SW, image=nebo_img)

shar_img = PhotoImage(file='shar.png')
shar = my_canvas.create_image(250,497, anchor=CENTER, image=shar_img)


def up(event):
    x = 0
    y = 10
    my_canvas.move(nebo, x, y)

def down(event):
    x = 0
    y = -10
    my_canvas.move(nebo, x, y)

root.bind("<Up>", up)
root.bind("<Down>", down)

#Меню
title = Label(root, text='Введите значения', bg='#6ABBD9', font=("Times New Roman", 16))
title.place(relx=0.5, rely=0.2, anchor=CENTER)

title1 = Label(root,
               text='Здравствуйте! Вас приветствует команда разработчиков данной программы.',
               bg='#6ABBD9',
               font=("Times New Roman", 8))
title1.place(relx=0.5, rely=0.075, anchor=CENTER)

title2 = Label(root,
               text='С помощью неё Вы можете узнать, какой объём гелия (1 шар - 0.0075 (кг/м^3)) понадобится',
               bg='#6ABBD9',
               font=("Times New Roman", 8))
title2.place(relx=0.5, rely=0.1, anchor=CENTER)

title3 = Label(root,
               text='для подъёма определённого груза на определённую высоту',
               bg='#6ABBD9',
               font=("Times New Roman", 8))
title3.place(relx=0.5, rely=0.125, anchor=CENTER)

title4 = Label(root,
               text='Версия: alpha',
               bg='#6ABBD9',
               font=("Times New Roman", 8))
title4.place(relx=0.5, rely=0.15, anchor=CENTER)

m1 = Entry(root, width=20)
m1.place(relx=0.5, rely=0.3, anchor=CENTER)

h1 = Entry(root, width=20)
h1.place(relx=0.5, rely=0.4, anchor=CENTER)

m = Label(root, text='Масса груза (кг)', bg='#6ABBD9', font=("Times New Roman", 10))
m.place(relx=0.5, rely=0.25, anchor=CENTER)

h = Label(root, text='Высота (км)', bg='#6ABBD9', font=("Times New Roman", 10))
h.place(relx=0.5, rely=0.35, anchor=CENTER)

def close():
    x = float(m1.get())
    y = float(h1.get())

    title.destroy()
    title1.destroy()
    title2.destroy()
    title3.destroy()
    title4.destroy()
    m1.destroy()
    h1.destroy()
    m.destroy()
    h.destroy()
    button.destroy()

    # Математика
    try:
        pl = 0

        if 0 <= y < 0.05:
            pl = 1.225
        else:
            if 0.05 <= y < 0.1:
                pl = 1.219
            else:
                if 0.1 <= y < 0.2:
                    pl = 1.213
                else:
                    if 0.2 <= y < 0.3:
                        pl = 1.202
                    else:
                        if 0.3 <= y < 0.5:
                            pl = 1.190
                        else:
                            if 0.5 <= y < 1:
                                pl = 1.167
                            else:
                                if 1 <= y < 2:
                                    pl = 1.112
                                else:
                                    if 2 <= y < 3:
                                        pl = 1.007
                                    else:
                                        if 3 <= y < 5:
                                            pl = 0.909
                                        else:
                                            if 5 <= y < 8:
                                                pl = 0.736
                                            else:
                                                if 8 <= y < 10:
                                                    pl = 0.526
                                                else:
                                                    if 10 <= y < 12:
                                                        pl = 0.414
                                                    else:
                                                        if 12 <= y < 15:
                                                            pl = 0.312
                                                        else:
                                                            if 15 <= y < 20:
                                                                pl = 0.195
                                                            else:
                                                                if 20 <= y <= 50:
                                                                    pl = 0.089
        ob = Label(root, text="Объём гелия будет равен {}".format(x / pl))
        ob.place(relx=0.5, rely=0.3, anchor=CENTER)
        ksh = Label(root, text="Шаров понадобится {}".format(round((x / pl) / (0.0075))))
        ksh.place(relx=0.5, rely=0.4, anchor=CENTER)
        my_canvas.create_text(250, 466, text="x{}".format(round((x / pl) / (0.0075))), font=("Times New Roman", 10), fill='White')
        my_canvas.create_text(250, 534, text="{} Кг".format(x), font=("Times New Roman", 8), fill='White')
        my_canvas.create_text(375, 546, text="-------------------------------------------------------------------", font=("Times New Roman", 8), fill='black')
    except ValueError:
        osh = Label(root, text="Ошибка введите цифры")
        osh.place(relx=0.5, rely=0.3, anchor=CENTER)
# Движуха
    for i in range(1, 100):

        v=0

        if 0 <= y <= 0.025:
            frac, whole = math.modf(y)
            u = frac * 1000
            u = int(u)
            p = 0.424
            v=p*u
            my_canvas.move(1, 0, v)
            root.update()
            time.sleep(0.02)
        else:
            if 0.025<y<1:
                frac, whole = math.modf(y)
                u = frac * 1000
                u = int(u)
                p = 0.012589
                u = u-25
                v = u*p
                v = 10.6 + v
                my_canvas.move(1, 0, v)
                root.update()
                time.sleep(0.02)
            else:
                if 1 <= y <=50:
                    u = y * 1000
                    p = 0.000916
                    u = u - 1000
                    v = u * p
                    v = 22.89 + v
                    my_canvas.move(1, 0, v)
                    root.update()
                    time.sleep(0.02)

def pog():
    close()

button = Button(root, text='Поехали!', bg='white', font=("Times New Roman", 15), command=pog)
button.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()