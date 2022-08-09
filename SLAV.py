from tkinter import *
import math
import datetime

list_dni = ["Понедельникъ","Вторникъ", "Третейникъ", "Четверикъ", "Пятница", "Шестица", "Седьмица", "Осьмица", "Неделя"]
list_mes = ["Рамхатъ", "Айлѣтъ", "Бейлѣтъ", "Гэйлѣтъ", "Дайлѣтъ", "Элѣтъ", "Вэйлѣтъ", "Хейлѣтъ", "Тайлѣтъ"]


# nowq = datetime.datetime.now().microsecond
def x_cord(leng, angle):
    return width / 2 + leng * math.cos(angle * math.pi / 180)


def y_cord(leng, angle):
    return height / 3 - leng * math.sin(angle * math.pi / 180)


# hours = {18:0,19}

width = 500
height = 500
radius = 100

root = Tk()
root.title("Часы")

canvas = Canvas(root, width=width, height=height)
canvas.pack()

#canvas.create_oval(width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius)
second_arrow = canvas.create_line(0, 0, 0, 0, fill="red")
minute_arrow = canvas.create_line(0, 0, 0, 0, fill="green")
hour_arrow = canvas.create_line(0, 0, 0, 0, )

hour_text = Label(text="Часы: ", font=('Times',15))
hour_text.place(x = width-450, y = width - 150)
minute_text = Label(text="Части: ", font=('Times',15))
minute_text.place(x = width-350, y = width - 150)
second_text = Label(text="Доли: ", font=('Times',15))
second_text.place(x = width-250, y = width - 150)


def change_hand(len, time, clock_hand, degree):
    alph = 180 - time * degree
    x1 = x_cord(0, alph)
    y1 = y_cord(0, alph)
    x2 = x_cord(len, alph)
    y2 = y_cord(len, alph)
    canvas.coords(clock_hand, x1, y1, x2, y2)


def update():
    # nowq = datetime.datetime.now().microsecond

    global hour  # * (2/3) + 4
    global minute  # * 1.6
    global second  # = (time.second * 1000 + time.microsecond / 1000) / 28.9
    global year
    global n
    second += 16  # 17.5
    if n == 1:
        second = 0
        minute = 0
    if second >= 1296:
        second -= 1296
        minute += 1
    if minute >= 144:
        minute -= 144
        hour += 1

    change_hand(radius - 20, int(second), second_arrow, 0.277)
    change_hand(radius - 40, int(minute), minute_arrow, 2.5)
    change_hand(radius - 80, int(hour), hour_arrow, 22.5)
    hour_text.config(text = "Часы: " + str(int(hour)))
    minute_text.config(text="Части: " + str(int(minute)))
    second_text.config(text="Доли: " + str(int(second)))


    # second += 34.5
    # nowq1 = datetime.datetime.now().microsecond
    print(hour, minute, int(second))
    # print(nowq - nowq1)
    root.after(462, update)  # 500


alph = 157.5
for i in range(1, 17):
    canvas.create_text(x_cord(radius + 20, alph), y_cord(radius + 20, alph), text=i, fill="darkblue",
                       font="Times 10 bold")
    alph -= 22.5

for i in range(144):
    if alph % 22.5 == 0:
        vit = 20
    else:
        vit = 10
    xli1 = x_cord(radius, alph)
    yli1 = y_cord(radius, alph)
    xli2 = x_cord(radius - vit, alph)
    yli2 = y_cord(radius - vit, alph)

    canvas.create_line(xli1, yli1, xli2, yli2)
    alph += 2.5

# datetime.datetime.now().microsecond
# datetime.datetime.now().second

time = datetime.datetime.now()
hour = time.hour

year = time.year


minute = time.minute

second = time.second
n = 0

if hour % 1.5 != 0:
    hour -= 1
    minute += 60
    if hour % 1.5 != 0:
        hour += 0.5
        minute -= 30
'''
if hour % 1.5 != 0:

    if minute // 30 == 1:
        hour += 0.5
        minute -= 30
        if hour % 1.5 != 0:
            hour -= 1
            minute += 60# + (hour / 1.5 - int(hour / 1.5)) * 60
'''

fake_minute = 0

minute *= 1.6
second *= 34.56

second += (minute - int(minute)) * 1296



if second >= 1296:
    fake_minute = 1
    second -= 1296

minute += fake_minute

if hour < 18:
    hour = hour * (2 / 3) + 4
else:
    hour = hour * (2 / 3) - 12

# nowq1 = datetime.datetime.now().microsecond
# print(nowq - nowq1)
update()

root.mainloop()
