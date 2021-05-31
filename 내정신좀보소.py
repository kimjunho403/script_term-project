from tkinter import *
from tkinter import font
from tkinter.simpledialog import *
import tkinter.messagebox
import tkinter.ttk

import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

id = []
DataList= []
detail_DataList = []
add_high=100
add_wight=100
l =[]
d_l= []
class MainGUI:

    #이전 버튼을 누르면 한칸씩 출력
    def PreButtonAction(self):
        # 만약 가장 앞이면 아무일도 일어나지 않는다.
        if self.pageNum >1:
            self.pageNum -= 1

        from urllib import parse
        id.clear()

        self.Item_RenderText.configure(state='normal')
        self.Item_RenderText.delete(0.0, END)

        self.item_e = parse.quote(self.item_InputLabel.get())
        self.area_e = parse.quote(self.area_InputLabel.get())
        self.SearchFoundArticle()

        self.Item_RenderText.configure(state='disabled')

    #다음 버튼을 누르면 한칸씩 전진
    def NextButtonAction(self):
        from urllib import parse
        id.clear()

        self.pageNum += 1

        self.Item_RenderText.configure(state='normal')
        self.Item_RenderText.delete(0.0, END)

        self.item_e = parse.quote(self.item_InputLabel.get())
        self.area_e = parse.quote(self.area_InputLabel.get())
        self.SearchFoundArticle()

        self.Item_RenderText.configure(state='disabled')

    def DoublePreButtonAction(self):
        if self.pageNum > 5:
            self.pageNum -= 5

        from urllib import parse
        id.clear()

        self.Item_RenderText.configure(state='normal')
        self.Item_RenderText.delete(0.0, END)

        self.item_e = parse.quote(self.item_InputLabel.get())
        self.area_e = parse.quote(self.area_InputLabel.get())
        self.SearchFoundArticle()

        self.Item_RenderText.configure(state='disabled')
    def DoubleNextButtonAction(self):
        from urllib import parse
        id.clear()

        self.pageNum += 5

        self.Item_RenderText.configure(state='normal')
        self.Item_RenderText.delete(0.0, END)

        self.item_e = parse.quote(self.item_InputLabel.get())
        self.area_e = parse.quote(self.area_InputLabel.get())
        self.SearchFoundArticle()

        self.Item_RenderText.configure(state='disabled')

    def MapButtonAction(self):
        pass
    def EmailButtonAction(self):
        pass
    def RenderText(self):
        pass
    def Detail_ButtonAction(self):
        from urllib import parse


        self.Detail_RenderText.configure(state='normal')
        self.Detail_RenderText.delete(0.0, END)

        if self.is_foundArticle ==True:
            self.Show_Founddetail()
        else:
            self.Show_Lostdetail()
    def Show_Lostdetail(self):
        import urllib
        import http.client
        from xml.dom.minidom import parse, parseString

        conn = http.client.HTTPConnection("apis.data.go.kr")
        conn.request("GET",
                     "/1320000/LostGoodsInfoInqireService/getLostGoodsDetailInfo?serviceKey=YrQn72lYE4qA3NfS2pkl%2FEwy95kCZ8jghF27PMOoOD3apbMi6htMwfFztU28urc6rMLLh8eWyVdDGVLCooMWPw%3D%3D&ATC_ID" + id[int(self.Detail_SearchEntry.get())-1])
        req = conn.getresponse()

        detail_DataList.clear()

        if req.status == 200:
            DocArticle = req.read().decode('UTF-8')
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
                if obj_3.nodeName == "item":
                    subitems = obj_3.childNodes
                    for atom in subitems:
                        if atom.nodeName in "lstFilePathImg":  # 이미지
                            detail_DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "lstPlace":  # 분실장소
                            detail_DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "lstSbjt":  # 분실물
                            detail_DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "orgNm":  # 경찰서
                            detail_DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "tel":  # 전화번호
                            detail_DataList.append(atom.firstChild.nodeValue)

                self.Detail_RenderText.insert(INSERT, "[")
                self.Detail_RenderText.insert(INSERT, 1)
                self.Detail_RenderText.insert(INSERT, "] ")
                self.Detail_RenderText.insert(INSERT, "분실물 사진: ")
                self.Detail_RenderText.insert(INSERT, detail_DataList[0])
                self.Detail_RenderText.insert(INSERT, "\n")
                self.Detail_RenderText.insert(INSERT, "분실한 장소: ")
                self.Detail_RenderText.insert(INSERT, detail_DataList[1])
                self.Detail_RenderText.insert(INSERT, "\n")
                self.Detail_RenderText.insert(INSERT, "분실물: ")
                self.Detail_RenderText.insert(INSERT, detail_DataList[2])
                self.Detail_RenderText.insert(INSERT, "\n")
                self.Detail_RenderText.insert(INSERT, "관할 경찰서: ")
                self.Detail_RenderText.insert(INSERT, detail_DataList[3])
                self.Detail_RenderText.insert(INSERT, "\n")
                self.Detail_RenderText.insert(INSERT, "전화번호: ")
                self.Detail_RenderText.insert(INSERT, detail_DataList[4])
                self.Detail_RenderText.insert(INSERT, "\n\n")

    def Show_Founddetail(self):
        import urllib
        import http.client
        from xml.dom.minidom import parse, parseString


        conn = http.client.HTTPConnection("apis.data.go.kr")
        conn.request("GET",
                     "/1320000/LosfundInfoInqireService/getLosfundDetailInfo?serviceKey=YrQn72lYE4qA3NfS2pkl%2FEwy95kCZ8jghF27PMOoOD3apbMi6htMwfFztU28urc6rMLLh8eWyVdDGVLCooMWPw%3D%3D&ATC_ID=" + id[int(self.Detail_SearchEntry.get())-1] + "&FD_SN=1")
        req = conn.getresponse()

        detail_DataList.clear()

        if req.status == 200:
            DocArticle = req.read().decode('UTF-8')

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
                if obj_3.nodeName == "item":
                    subitems = obj_3.childNodes
                    for atom in subitems:
                        if atom.nodeName in "csteSteNm":  # 보관상태
                            detail_DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "depPlace":  # 보관 경찰서
                            detail_DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "fdFilePathImg":  # 이미지
                            detail_DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "fdPlace":  # 습득 장소
                            detail_DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "fdPrdtNm":  # 물품명
                            detail_DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "tel":  # 전화번호
                            detail_DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "uniq":  # 내용
                            detail_DataList.append(atom.firstChild.nodeValue)

                self.Detail_RenderText.insert(INSERT, "[")
                self.Detail_RenderText.insert(INSERT, 1)
                self.Detail_RenderText.insert(INSERT, "] ")
                self.Detail_RenderText.insert(INSERT, "보관상태: ")
                self.Detail_RenderText.insert(INSERT, detail_DataList[0])
                self.Detail_RenderText.insert(INSERT, "\n")
                self.Detail_RenderText.insert(INSERT, "경찰서: ")
                self.Detail_RenderText.insert(INSERT, detail_DataList[1])
                self.Detail_RenderText.insert(INSERT, "\n")
                self.Detail_RenderText.insert(INSERT, "이미지: ")
                self.Detail_RenderText.insert(INSERT, detail_DataList[2])
                self.Detail_RenderText.insert(INSERT, "\n")
                self.Detail_RenderText.insert(INSERT, "습득 장소: ")
                self.Detail_RenderText.insert(INSERT, detail_DataList[3])
                self.Detail_RenderText.insert(INSERT, "\n")
                self.Detail_RenderText.insert(INSERT, "물품명: ")
                self.Detail_RenderText.insert(INSERT, detail_DataList[4])
                self.Detail_RenderText.insert(INSERT, "\n")
                self.Detail_RenderText.insert(INSERT, "전화번호: ")
                self.Detail_RenderText.insert(INSERT, detail_DataList[5])
                self.Detail_RenderText.insert(INSERT, "\n")
                self.Detail_RenderText.insert(INSERT, detail_DataList[6])
                self.Detail_RenderText.insert(INSERT, "\n\n")

    def SearchButtonAction(self):
        from urllib import parse
        self.pageNum =1
        id.clear()

        self.Item_RenderText.configure(state='normal')
        self.Item_RenderText.delete(0.0, END)

        self.item_e = parse.quote(self.item_InputLabel.get())
        self.area_e = parse.quote(self.area_InputLabel.get())

        if self.is_foundArticle ==True:#습득물
            self.SearchFoundArticle()
        elif self.is_foundArticle  ==False:
            self.SearchLostArticle()



        self.Item_RenderText.configure(state='disabled')
    def SearchLostArticle(self):
        import urllib
        import http.client
        from xml.dom.minidom import parse, parseString

        conn = http.client.HTTPConnection("apis.data.go.kr")
        conn.request("GET",
                     "/1320000/LostGoodsInfoInqireService/getLostGoodsInfoAccTpNmCstdyPlace?serviceKey=YrQn72lYE4qA3NfS2pkl%2FEwy95kCZ8jghF27PMOoOD3apbMi6htMwfFztU28urc6rMLLh8eWyVdDGVLCooMWPw%3D%3D&LST_PLACE="+self.area_e+"&LST_PRDT_NM="+self.item_e + "&pageNo="+str(self.pageNum)+"&numOfRows=10")
        req = conn.getresponse()
        print(req.status, req.reason)


        DataList.clear()
        l.clear()

        if req.status == 200:
            DocArticle = req.read().decode('UTF-8')
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
                    for atom in subitems:
                        if atom.nodeName in "atcId":  # 코드
                            id.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "lstPlace":
                            DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "lstPrdtNm":
                            DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "lstSbjt":
                            DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "lstYmd":
                            DataList.append(atom.firstChild.nodeValue)


            for i in range(len(DataList) // 4):
                self.Item_RenderText.insert(INSERT, "[")
                self.Item_RenderText.insert(INSERT, i + 1)
                self.Item_RenderText.insert(INSERT, "] ")
                self.Item_RenderText.insert(INSERT, "주소: ")
                self.Item_RenderText.insert(INSERT, DataList[0 + i * 4])
                self.Item_RenderText.insert(INSERT, "\n")
                self.Item_RenderText.insert(INSERT, "분실물: ")
                self.Item_RenderText.insert(INSERT, DataList[1 + i * 4])
                self.Item_RenderText.insert(INSERT, "\n")
                self.Item_RenderText.insert(INSERT, "상세내용: ")
                self.Item_RenderText.insert(INSERT, DataList[2 + i * 4])
                self.Item_RenderText.insert(INSERT, "\n")
                self.Item_RenderText.insert(INSERT, "날짜: ")
                self.Item_RenderText.insert(INSERT, DataList[3 + i * 4])
                self.Item_RenderText.insert(INSERT, "\n\n")


    def SearchFoundArticle(self):
        import urllib
        import http.client
        from xml.dom.minidom import parse, parseString

        conn = http.client.HTTPConnection("apis.data.go.kr")
        conn.request("GET",
                     "/1320000/LosfundInfoInqireService/getLosfundInfoAccToLc?serviceKey=YrQn72lYE4qA3NfS2pkl%2FEwy95kCZ8jghF27PMOoOD3apbMi6htMwfFztU28urc6rMLLh8eWyVdDGVLCooMWPw%3D%3D&PRDT_NM="+self.item_e +"&ADDR="+self.area_e+"&pageNo="+str(self.pageNum)+"&numOfRows=10")
        req = conn.getresponse()
        print(req.status, req.reason)

        DataList.clear()
        l.clear()

        if req.status == 200:
            DocArticle = req.read().decode('UTF-8')

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
                    for atom in subitems:
                        if atom.nodeName in "atcId":#코드
                            id.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "addr":
                            DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "fdPrdtNm":
                            DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "fdSbjt":
                            DataList.append(atom.firstChild.nodeValue)
                        if atom.nodeName in "fdYmd":
                            DataList.append(atom.firstChild.nodeValue)



            for i in range(len(DataList)//4):

                self.Item_RenderText.insert(INSERT, "[")
                self.Item_RenderText.insert(INSERT, i + 1)
                self.Item_RenderText.insert(INSERT, "] ")
                self.Item_RenderText.insert(INSERT, "주소: ")
                self.Item_RenderText.insert(INSERT, DataList[0 + i * 4])
                self.Item_RenderText.insert(INSERT, "\n")
                self.Item_RenderText.insert(INSERT, "습득물: ")
                self.Item_RenderText.insert(INSERT, DataList[1 + i * 4])
                self.Item_RenderText.insert(INSERT, "\n")
                self.Item_RenderText.insert(INSERT, "상세내용: ")
                self.Item_RenderText.insert(INSERT, DataList[2 + i * 4])
                self.Item_RenderText.insert(INSERT, "\n")
                self.Item_RenderText.insert(INSERT, "날짜: ")
                self.Item_RenderText.insert(INSERT, DataList[3 + i * 4])
                self.Item_RenderText.insert(INSERT, "\n\n")




    def v(self):
        if self.type.get() ==1:
            self.is_foundArticle = True
        else:
            self.is_foundArticle =False

    def __init__(self):
        self.window = Tk("내정신좀보소!")
        self.window.geometry("760x760")
        self.window.configure(bg='#a9d4df')

        self.pageNum =1
        self.is_foundArticle = True

        #이미지 선언
        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')
        self.image_title = PhotoImage(file='image/title.PNG')
        self.image_logo = PhotoImage(file='image/logo.PNG')
        self.image_map = PhotoImage(file='image/map.PNG')
        self.image_email = PhotoImage(file='image/email.PNG')
        self.image_oneleft = PhotoImage(file='image/1.PNG')
        self.image_oneright = PhotoImage(file='image/2.PNG')
        self.image_fiveleft = PhotoImage(file='image/3.PNG')
        self.image_fiveright = PhotoImage(file='image/4.PNG')
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

        self.canvas = Canvas(frame1, width=700, height=600, bg='#a9d4df')
        self.canvas.pack()
        #lab1=Label(self.window, text='', font=self.TempFont)
        #lab1.place(x=380,y=200)

        self.area_InputLabel = tkinter.Label(frame1)
        self.area_InputLabel = Entry(self.window, font=self.TempFont, width=26, borderwidth=6)
        self.area_InputLabel.pack()
        self.area_InputLabel.place(x=390, y=170)

        self.item_InputLabel = Entry(self.window, font=self.TempFont, width=13, borderwidth=6)
        self.item_InputLabel.pack()
        self.item_InputLabel.place(x=390, y=230)

        self.SearchButton = Button(self.window, font=self.TempFont, text="검색", command=self.SearchButtonAction)
        self.SearchButton.pack()
        self.SearchButton.place(x=590, y=230)

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
        self.Detail_RenderText.place(x=390, y=290)

        self.Detail_RenderText.configure(state='disabled')

        self.previous = Button(self.window, image=self.image_oneleft, command=self.PreButtonAction)
        self.previous['bg'] = '#a9d4df'
        self.previous.pack()
        self.previous.place(x=120, y=590)

        self.Next = Button(self.window, image=self.image_oneright, command=self.NextButtonAction)
        self.Next['bg'] = '#a9d4df'
        self.Next.pack()
        self.Next.place(x=200, y=590)

        self.double_previous = Button(self.window, image=self.image_fiveleft, command=self.DoublePreButtonAction)
        self.double_previous['bg'] = '#a9d4df'
        self.double_previous.pack()
        self.double_previous.place(x=30, y=590)

        self.double_Next = Button(self.window, image=self.image_fiveright, command=self.DoubleNextButtonAction)
        self.double_Next['bg'] = '#a9d4df'
        self.double_Next.pack()
        self.double_Next.place(x=300, y=590)

        #상세 정보 버튼
        self.Detail_SearchButton = Button(self.window,width=14, font=self.TempFont, text="상세 정보", command=self.Detail_ButtonAction)
        self.Detail_SearchButton['bg'] = '#a9d4df'
        self.Detail_SearchButton.pack()
        self.Detail_SearchButton.place(x=200, y=540)

        self.Detail_SearchEntry = Entry(self.window, font=self.TempFont, width=13, borderwidth=6)
        self.Detail_SearchEntry.pack()
        self.Detail_SearchEntry.place(x=25, y=540)

        self.map_Button = Button(self.window, image=self.image_map, command=self.MapButtonAction)
        self.map_Button['bg'] = '#a9d4df'
        self.map_Button.pack()
        self.map_Button.place(x=430, y=640)

        self.email_Button = Button(self.window, image=self.image_email, command=self.EmailButtonAction)
        self.email_Button['bg'] = '#a9d4df'
        self.email_Button.pack()
        self.email_Button.place(x=580, y=640)

        # 두번째 리스트
        frame2 = tkinter.Frame(self.window)
        notebook.add(frame2, text="최근 들어온 물품들")

        label2 = tkinter.Label(frame2, text="하루동안 들어온 물품 리스트")
        label2.pack()

        #self.canvas = Canvas(frame2, width=700, height=600, bg='#a9d4df')
        #self.canvas.pack()

        # 그래프 그리기

        data2 = {'Category': ['Wallet', 'Phone', 'Bag', 'Jewllery', 'Etc'],
                 'Count': [10, 5, 8, 7.2, 15]
                 }
        df2 = DataFrame(data2, columns=['Category', 'Count'])

        self.canvas = Canvas(frame2, width=700, height=600, bg='#a9d4df')
        self.canvas.pack()

        figure2 = plt.Figure(figsize=(6, 4), dpi=100)
        #plt.xlabel('카테고리', fontproperties=fontprop)
        #plt.ylabel('갯수', fontproperties=fontprop)

        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self.canvas)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2 = df2[['Category', 'Count']].groupby('Category').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='b', marker='o', fontsize=10)
        ax2.set_title('Recent Commodities')

        self.window.mainloop()

MainGUI()