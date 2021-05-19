from tkinter import *
from tkinter import font
from tkinter.simpledialog import *
import tkinter.messagebox

class MainGUI:
    def MapButtonAction(self):
        pass
    def EmailButtonAction(self):
        pass
    def RenderText(self):
        pass
    def Detail_ButtonAction(self):
        pass

    def SearchButtonAction(self):
        pass

    def v(self):
        pass
    def __init__(self):
        self.window = Tk("내정신좀보소!")
        self.window.geometry("760x760")
        self.window['bg'] = '#a9d4df'

        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')
        self.image_title = PhotoImage(file='image/title.PNG')
        self.image_logo = PhotoImage(file='image/logo.PNG')
        self.image_map = PhotoImage(file='image/map.PNG')
        self.image_email = PhotoImage(file='image/email.PNG')
        self.imageLabel = Label(self.window, image= self.image_title)
        self.imageLabel['bg'] = '#a9d4df'
        self.imageLabel.pack()
        self.imageLabel.place(x=150,y=10)
        self.imageLabel2 = Label(self.window, image=self.image_logo)
        self.imageLabel2['bg']= '#a9d4df'
        self.imageLabel2.pack()
        self.imageLabel2.place(x=550,y=10)
        self.type = IntVar()

        self.r1 = Radiobutton(self.window,text='습득물',variable=self.type,value=1,command=self.v)
        self.r1['bg'] = '#a9d4df'
        self.r1.pack()
        self.r1.place(x=200,y=100)

        self.r2 = Radiobutton(self.window,text='분실물', variable=self.type, value=2,command=self.v)
        self.r2['bg'] = '#a9d4df'
        self.r2.pack()
        self.r2.place(x=300,y=100)

        self.day_InputLabel = Entry(self.window, font=self.TempFont, width=26, borderwidth=6)
        self.day_InputLabel.pack()
        self.day_InputLabel.place(x=400, y=200)

        self.area_InputLabel = Entry(self.window, font=self.TempFont, width=26, borderwidth=6)
        self.area_InputLabel.pack()
        self.area_InputLabel.place(x=400, y=250)

        self.item_InputLabel = Entry(self.window, font=self.TempFont, width=13, borderwidth=6)
        self.item_InputLabel.pack()
        self.item_InputLabel.place(x=400, y=300)

        self.SearchButton = Button(self.window, font=self.TempFont, text="검색", command=self.SearchButtonAction)
        self.SearchButton['bg'] = '#a9d4df'
        self.SearchButton.pack()
        self.SearchButton.place(x=600, y=300)

        self.RenderTextScrollbar = Scrollbar(self.window)
        self.RenderTextScrollbar.pack()
        self.RenderTextScrollbar.place(x=375, y=200)

        self.Item_RenderText = Text(self.window, width=49, height=27, borderwidth=6, yscrollcommand=self.RenderTextScrollbar.set)
        self.Item_RenderText.pack()
        self.Item_RenderText.place(x=10, y=215)
        self.RenderTextScrollbar.config(command=self.Item_RenderText)
        self.RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

        self.Item_RenderText.configure(state='disabled')

        self.Detail_RenderText = Text(self.window, width=47, height=25, borderwidth=6)
        self.Detail_RenderText.pack()
        self.Detail_RenderText.place(x=390, y=370)

        self.Detail_RenderText.configure(state='disabled')

        self.Detail_SearchButton = Button(self.window,width=30, font=self.TempFont, text="상세 정보", command=self.Detail_ButtonAction)
        self.Detail_SearchButton['bg'] = '#a9d4df'
        self.Detail_SearchButton.pack()
        self.Detail_SearchButton.place(x=10, y=580)

        self.map_Button = Button(self.window, image=self.image_map, command=self.MapButtonAction)
        self.map_Button['bg'] ='#a9d4df'
        self.map_Button.pack()
        self.map_Button.place(x=10, y=630)

        self.email_Button = Button(self.window, image=self.image_email, command=self.EmailButtonAction)
        self.email_Button['bg'] = '#a9d4df'
        self.email_Button.pack()
        self.email_Button.place(x=200, y=630)

        self.window.mainloop()

MainGUI()