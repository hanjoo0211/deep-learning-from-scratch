from tkinter import *
from PIL import ImageGrab
from predictNumber import predictNumber

window = None
canvas = None
x1, y1 = None, None # 마우스 좌표
wp = 8 # 선 굵기
p, n = None, "답" # 결과


def mouseMove(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    canvas.create_oval(x1-wp, y1-wp, x1+wp, y1+wp, fill="black")


def clearCanvas(): # 지우기
    canvas.delete("all")


def run(): # 실행
    # 캔버스 저장
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    captureBox = (x+20, y+2, x+300, y+282) # 2정도 오차가 나더라.. y좌표 오차 조절
    img = ImageGrab.grab(captureBox) # macOS에서는 Pillow모듈의 좌표가 이상하게 잡힘;
    img = img.resize((28, 28)) # 28*28로 조절

    # 신경망에 보내 결과 추출
    global p, n
    p, n = predictNumber(img) # p는 각 숫자일 확률이 담긴 배열, n은 확률 최댓값의 index
    print(p)

    # 결과
    resultLabel = Label(window, text=n[0], font=("궁서", 40))
    resultLabel.place(x=140, y=350)


window = Tk()
window.title("손글씨를 써보세요!")
window.geometry("320x480+800+300")
window.resizable(False, False)

# 그림판
canvas = Canvas(window, width=280, height=280, bg="white")
canvas.bind('<B1-Motion>', mouseMove)
canvas.place(x=18, y=0) # 2정도 오차가 나더라.. x좌표 오차 조절

# 버튼
clearButton = Button(window, text="지우기", fg="black", command=clearCanvas)
saveButton = Button(window, text="실행", fg="black", command=run)
clearButton.place(x=100, y=290, width=50)
saveButton.place(x=170, y=290, width=50)

window.mainloop()