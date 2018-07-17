# coding:utf8
from Tkinter import *
import time
import tkMessageBox
from cProfile import label
from PIL.ImageOps import expand
class Count():
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.entryWidget = Entry(frame,font=('times',14))
        self.entryWidget["width"] = 15
        self.entryWidget.pack(side=LEFT,padx=5)
        self.hi_there = Button(frame,text="Start",bg="green",font=('times',14),command=self.start)
        self.hi_there.pack(side=LEFT,padx=5)
        self.button = Button(frame,text="Quit",fg="red",bg="gray",font=('times',14),command=frame.quit)
        self.button.pack(side=LEFT,padx=5)
    def start(self):
        text = self.entryWidget.get().strip()
        if text != "":
            if text.isdigit():
                num = int(text)
                self.countDown(num)
            else:
                tkMessageBox.showerror("errorTips","请输入数字！")
        else:
            tkMessageBox.showerror("errorTips","不能为空！")
    def countDown(self,seconds):
        frame_area.config(bg='yellow')
        frame_area.config(height=3, font=('times',20,'bold'),fg="black")
        for k in range(seconds, 0, -1):
            frame_area["text"] = k
            root.update()
            time.sleep(1)
        frame_area.config(bg='red')
        frame_area.config(fg='white')
        frame_area["text"] = "Time's up!"
        tkMessageBox.showinfo("Time's up!","Time's up!")
    def GetSource():
        get_window = Tkinter.Toplevel(root)
        get_window.title('Source File?')
        Tkinter.Entry(get_window, width=30,
                textvariable=source).pack()
        Tkinter.Button(get_window, text="Change",
            command=lambda: update_specs()).pack()
if __name__ == "__main__":
    root = Tk()
    root.geometry('300x200')
    root.title("测试30分钟超时(30*60)")
    root.resizable(width=False, height=False)
    root_f = Frame(root, bg="black")
    root_f.pack()
#     root.iconbitmap("qtec.ico")        # 图标添加报错
    tips = Label(root, text="倒计时计算（输入单位：秒/s）",font=("times",12,'bold'))
    tips.pack()
    frame_area = Label()
    frame_area.pack(fill=BOTH, expand=1)
    app = Count(root)
    root.mainloop()