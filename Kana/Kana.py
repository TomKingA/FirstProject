import tkinter as tk
import random as rd
rd.seed()
hiragana={
    'あ':'a','い':'i','う':'u','え':'e','お':'o',
    'か':'ka','き':'ki','く':'ku','け':'ke','こ':'ko',
    'さ':'sa','し':'shi','す':'su','せ':'se','そ':'so',
    'た':'ta','ち':'chi','つ':'tsu','て':'te','と':'to',
    'な':'na','に':'ni','ぬ':'nu','ね':'ne','の':'no',
    'は':'ha','ひ':'hi','ふ':'fu','へ':'he','ほ':'ho',
    'ま':'ma','み':'mi','む':'mu','め':'me','も':'mo',
    'や':'ya','ゆ':'yu','よ':'yo','わ':'wa','を':'wo',
    'ら':'ra','り':'ri','る':'ru','れ':'re','ろ':'ro',
    'ん':'n'
}
katakana={
    'ア':'a','イ':'i','ウ':'u','エ':'e','オ':'o',
    'カ':'ka','キ':'ki','ク':'ku','ケ':'ke','コ':'ko',
    'サ':'sa','シ':'shi','ス':'su','セ':'se','ソ':'so',
    'タ':'ta','チ':'chi','ツ':'tsu','テ':'te','ト':'to',
    'ナ':'na','ニ':'ni','ヌ':'nu','ネ':'ne','ノ':'no',
    'ハ':'ha','ヒ':'hi','フ':'fu','ヘ':'he','ホ':'ho',
    'マ':'ma','ミ':'mi','ム':'mu','メ':'me','モ':'mo',
    'ヤ':'ya','ユ':'yu','ヨ':'yo','ワ':'wa','ヲ':'wo',
    'ラ':'ra','リ':'ri','ル':'ru','レ':'re','ロ':'ro',
    'ン':'n'
}

dis=dict()
cur=tuple()
def mix():
    global dis,cur
    dis=dict()
    if eh.get()==1:
        dis={**dis,**hiragana}
    if ek.get()==1:
        dis={**dis,**katakana}
    cur=get()
    w.after(10,myloop)

def get():
    t=rd.sample(dis.keys(),1)[0]
    return (t,dis[t])

def myloop():
    global cur,dis
    l['text']=cur[0]
    if en.get()==cur[1]:
        cur=get()
        en.delete(0,tk.END)
    w.after(10,myloop)


w=tk.Tk()
w.title('一个简简单单的程序')
w.geometry('300x300')
eh,ek=tk.IntVar(),tk.IntVar()
chkh=tk.Checkbutton(w,text='平假名',variable=eh,onvalue=1,offvalue=0,command=mix)
chkh.pack()
chkk=tk.Checkbutton(w,text='片假名',variable=ek,onvalue=1,offvalue=0,command=mix)
chkk.pack()
l=tk.Label(w,text=' ',font=('Arial',96),width=2,height=1)
l.pack()
en=tk.Entry(w,font=('Arial',14))
en.pack()
w.mainloop()