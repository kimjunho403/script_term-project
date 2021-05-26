from tkinter import *
from tkinter import font
from tkinter.simpledialog import *
import tkinter.messagebox
import tkinter.ttk

DataList= []
class MainGUI:

    #이전 버튼을 누르면 한칸씩 출력
    def PreButtonAction(self):
        # 만약 가장 앞이면 아무일도 일어나지 않는다.
        pass

    #다음 버튼을 누르면 한칸씩 전진
    def NextButtonAction(self):
        # 만약 가장 뒤면 아무일도 일어나지 않는다.
        pass

    def MapButtonAction(self):
        pass
    def EmailButtonAction(self):
        pass
    def RenderText(self):
        pass
    def Detail_ButtonAction(self):
        pass

    def SearchButtonAction(self):
        self.Item_RenderText.configure(state='normal')
        self.SearchFoundArticle()

        self.Item_RenderText.configure(state='disabled')

    def SearchFoundArticle(self):
        import urllib
        import http.client
        from xml.dom.minidom import parse, parseString
        conn = http.client.HTTPConnection("apis.data.go.kr")
        conn.request("GET",
                     "/1320000/LosfundInfoInqireService/getLosfundInfoAccToLc?serviceKey=YrQn72lYE4qA3NfS2pkl%2FEwy95kCZ8jghF27PMOoOD3apbMi6htMwfFztU28urc6rMLLh8eWyVdDGVLCooMWPw%3D%3D&PRDT_NM=%EC%A7%80%EA%B0%91&ADDR=%EA%B3%A0%EC%96%91&pageNo=1&numOfRows=10")
        req = conn.getresponse()
        print(req.status, req.reason)

        DataList.clear()

        if req.status == 200:
            DocArticle = req.read().decode('utf-8')
            if DocArticle == None:
                print("에러")
            else:
                parsedata = parseString(DocArticle)
                items = parsedata.childNodes
                item = items[0].childNodes
            for obj in item:
                if obj.nodeName == "body":
                    obj_2 = obj.childNodes
            for obj_3 in obj_2:
                if obj_3.nodeName == "items":
                    obj_4 = obj_3.childNodes
            for obj_5 in obj_4:
                if obj_5.nodeName == "item":
                    subitems = obj_5.childNodes
                    print(subitems[1].firstChild.nodeValue)
                    DataList.append((subitems[0].firstChild.nodeValue, subitems[4].firstChild.nodeValue,
                                     subitems[5].firstChild.nodeValue, subitems[8].firstChild.nodeValue))

            for i in range(len(DataList)):
                self.Item_RenderText.insert(INSERT, "[")
                self.Item_RenderText.insert(INSERT, i + 1)
                self.Item_RenderText.insert(INSERT, "] ")
                self.Item_RenderText.insert(INSERT, "주소: ")
                self.Item_RenderText.insert(INSERT, DataList[i][0])
                self.Item_RenderText.insert(INSERT, "\n")
                self.Item_RenderText.insert(INSERT, "습득물: ")
                self.Item_RenderText.insert(INSERT, DataList[i][1])
                self.Item_RenderText.insert(INSERT, "\n")
                self.Item_RenderText.insert(INSERT, "상세내용: ")
                self.Item_RenderText.insert(INSERT, DataList[i][2])
                self.Item_RenderText.insert(INSERT, "\n\n")

    def v(self):
        pass
    def __init__(self):
        self.window = Tk("내정신좀보소!")
        self.window.geometry("760x760")
        self.window['bg'] = '#a9d4df'

        #이미지 선언
        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')
        self.image_title = PhotoImage(file='image/title.PNG')
        self.image_logo = PhotoImage(file='image/logo.PNG')
        self.image_map = PhotoImage(file='image/map.PNG')
        self.image_email = PhotoImage(file='image/email.PNG')
        self.image_oneleft = PhotoImage(file='image/1.PNG')
        self.image_oneright = PhotoImage(file='image/2.PNG')
        self.imageLabel = Label(self.window, image= self.image_title)
        self.imageLabel['bg'] = '#a9d4df'

        #위쪽 이미지
        self.imageLabel.pack()
        self.imageLabel.place(x=150, y=10)
        self.imageLabel2 = Label(self.window, image=self.image_logo)
        self.imageLabel2['bg'] = '#a9d4df'
        self.imageLabel2.pack()
        self.imageLabel2.place(x=550, y=10)
        self.type = IntVar()

        self.r1 = Radiobutton(self.window, text='습득물', variable=self.type, value=1, command=self.v)
        self.r1['bg'] = '#a9d4df'
        self.r1.pack()
        self.r1.place(x=200, y=100)

        self.r2 = Radiobutton(self.window, text='분실물', variable=self.type, value=2, command=self.v)
        self.r2['bg'] = '#a9d4df'
        self.r2.pack()
        self.r2.place(x=300, y=100)

        #notebook 관련 코드
        notebook = tkinter.ttk.Notebook(self.window, width=700, height=570)
        notebook.pack()
        notebook.place(x=20, y=140)

        frame1 = tkinter.Frame(self.window)
        notebook.add(frame1, text="메인 화면")
        #lab1=Label(self.window, text='', font=self.TempFont)
        #lab1.place(x=380,y=200)

        self.area_InputLabel = tkinter.Label(frame1)
        self.area_InputLabel = Entry(self.window, font=self.TempFont, width=26, borderwidth=6)
        self.area_InputLabel.pack()
        self.area_InputLabel.place(x=400, y=170)

        self.item_InputLabel = Entry(self.window, font=self.TempFont, width=13, borderwidth=6)
        self.item_InputLabel.pack()
        self.item_InputLabel.place(x=400, y=230)

        self.SearchButton = Button(self.window, font=self.TempFont, text="검색", command=self.SearchButtonAction)
        self.SearchButton.pack()
        self.SearchButton.place(x=600, y=230)

        self.RenderTextScrollbar = Scrollbar(self.window)
        self.RenderTextScrollbar.pack()
        self.RenderTextScrollbar.place(x=375, y=210)

        self.Item_RenderText = Text(self.window, width=49, height=27, borderwidth=6, yscrollcommand=self.RenderTextScrollbar.set)
        self.Item_RenderText.pack()
        self.Item_RenderText.place(x=20, y=170)
        self.RenderTextScrollbar.config(command=self.Item_RenderText)
        self.RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

        self.Item_RenderText.configure(state='disabled')

        # 상세 정보 표시판
        self.Detail_RenderText = Text(self.window, width=45, height=25, borderwidth=6)
        self.Detail_RenderText.pack()
        self.Detail_RenderText.place(x=400, y=290)

        self.Detail_RenderText.configure(state='disabled')

        self.previous = Button(self.window, image=self.image_oneleft, command=self.PreButtonAction())
        self.previous['bg'] = '#a9d4df'
        self.previous.pack()
        self.previous.place(x=20, y=590)

        self.previous = Button(self.window, image=self.image_oneright, command=self.NextButtonAction())
        self.previous['bg'] = '#a9d4df'
        self.previous.pack()
        self.previous.place(x=250, y=590)

        #상세 정보 버튼
        self.Detail_SearchButton = Button(self.window,width=28, font=self.TempFont, text="상세 정보", command=self.Detail_ButtonAction)
        self.Detail_SearchButton['bg'] = '#a9d4df'
        self.Detail_SearchButton.pack()
        self.Detail_SearchButton.place(x=25, y=540)

        self.map_Button = Button(self.window, image=self.image_map, command=self.MapButtonAction)
        self.map_Button['bg'] = '#a9d4df'
        self.map_Button.pack()
        self.map_Button.place(x=400, y=640)

        self.email_Button = Button(self.window, image=self.image_email, command=self.EmailButtonAction)
        self.email_Button['bg'] = '#a9d4df'
        self.email_Button.pack()
        self.email_Button.place(x=600, y=640)

        frame2 = tkinter.Frame(self.window)
        notebook.add(frame2, text="최근 들어온 물품들")

        label2 = tkinter.Label(frame2, text="페이지2의 내용")
        label2.pack()

        self.window.mainloop()

MainGUI()