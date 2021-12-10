from tkinter import *
from PIL import ImageGrab
from PIL import Image

window = None
canvas = None
x1, y1 = None, None # 마우스 좌표
wp = 10 # 선 굵기


def mouseMove(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    canvas.create_oval(x1-wp, y1-wp, x1+wp, y1+wp, fill="black", width=3)


def clearCanvas():
    canvas.delete("all")


def saveCanvas():
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    w = window.winfo_width() + x
    h = window.winfo_height() + y
    captureBox = (x+20, y+2, x+300, y+282) # 2정도 오차가 나더라.. y좌표 오차 조절
    img = ImageGrab.grab(captureBox) # macOS에서는 Pillow모듈의 좌표가 이상하게 잡힘;
    img = img.resize((28, 28)) # 28*28로 조절
    img.save("capture.png")


window = Tk()
window.title("손글씨를 써보세요!")
window.geometry("320x480+800+300")
window.resizable(False, False)

canvas = Canvas(window, width=280, height=280, bg="white", bd=0)
canvas.bind('<B1-Motion>', mouseMove)
canvas.place(x=18, y=0) # 2정도 오차가 나더라.. x좌표 오차 조절

clearButton = Button(window, text="지우기", fg="black", command=clearCanvas)
saveButton = Button(window, text="실행", fg="black", command=saveCanvas)
clearButton.place(x=100, y=290, width=50)
saveButton.place(x=170, y=290, width=50)

window.mainloop()