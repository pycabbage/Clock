#coding: utf-8
#import getdate
#Clock 0.0.0
#Copyright 2017 Cabbage All Rights Reserved.
#python C:\Users\owner\code\project01_Clock\clock.py

from tkinter import *
import time, sys

ver = 'Clock 0.0.0\nCopyright 2017 Cabbage All Rights Reserved.'
help = '''<<HELP>>
-c [color]            : Set color of text [color].
-b [color]            : Set color of background [color].
-v                    : Show version and exit.
-f [FONT]             : Set font of text [FONT]
--fullscreen          : Fullscreen.
-h or --help          : Show this help and exit.
-H or --japanese-help : Show Japanese help and exit.'''
jhelp = '''<<ヘルプ>>
-c [color]                  : 文字色を[color]にします。
-b [color]                  : 背景色を[color]にします。
-v                          : バージョンを表示し、終了します。
-f [FONT]                   : フォントを[FONT]にします。
--fullscreen                : 画面をフルスクリーン表示にします。
-h もしくは --help          : 英語のヘルプを表示し、終了します。
-H もしくは --japanese-help : このヘルプを表示し、終了します。'''
print(ver)
if '-h' in sys.argv or '--help' in sys.argv:
    print(help)
    exit()
elif '-H' in sys.argv or '--japanese-help' in sys.argv:
    print(jhelp)
    exit()

if '-v' in sys.argv:
    exit()

textsize = 50
if '-s' in sys.argv:
    textsize = int(sys.argv[sys.argv.index('-s') + 1])

#Source Code Pro Medium : 450, 65/220,30
#7barSPBd               : 360, 80/180,50
#FuxedSys               : 320, 70/160, 35
#メニューバーで+20
tk = Tk()
tk.title('CabbageClock')
ca = Canvas(tk, width=320, height=90)
ca.pack()
tk.update()
tk.resizable(0, 0) # 画面サイズ変更を禁止
tk.iconbitmap(tk, 'lettuce.ico')

def readargs():
    global textcolor
    global backgroundcolor
    global netcheck
    arg = sys.argv
    textcolor = 'black'
    if '-c' in arg:
        textcolor = arg[(arg.index('-c') + 1)]
    backgroundcolor = 'white'
    if '-b' in arg:
        backgroundcolor = arg[(arg.index('-b') + 1)]
    netcheck = False
    if '-n' in arg:
        netcheck = True
        print('Sync time for Internet.')
    if '--fullscreen' in arg:
        tk.attributes("-fullscreen", True)

def sk(i):
    sa = str(i)
    if len(sa) == 1:
        sa = '0' + sa
    return sa

def start():
    global del_id
    global id
    global textcolor
    global backgroundcolor
    global printdebug
    global textsize
    global netcheck
    global fs
    readargs()
    del_id = [ca.create_rectangle(0, 0, 500, 500, fill=backgroundcolor)]
    textsize = 70
    #fontname = '7barSPBd'
    #fontname = 'Source Code Pro Medium'
    fontname = 'FuxedSys'
    if '-f' in sys.argv:
        fontname = sys.argv[sys.argv.index('-f') + 1]
    id = ca.create_text(160, 35, text='', fill=textcolor, font=(fontname, textsize))
    fs = False
    tk.attributes('-topmost', True)
    #時間調整
    s = time.localtime().tm_sec
    while True:
        if s != time.localtime().tm_sec:
            break
            del s


def rv():
    global id
    t = time.localtime()
    tt = sk(str(t.tm_hour)) + ':' + sk(str(t.tm_min)) + ':' + sk(str(t.tm_sec))
    ca.itemconfig(id, text=tt)

def crv():
    global id
    tt = detdate.getdate(1)
    ca.itemconfig(id, text=tt)


def ev(event):
    global fs
    if fs:
        #フルスクリーンをオフにする
        tk.attributes('-fullscreen', False)
        fs = False
    else:
        if event.keysym == 'F11':
            #フルスクリーンをオンにする
            tk.attributes('-fullscreen', True)
            fs = True

ca.bind_all('<KeyPress-F11>', ev)
ca.bind_all('<Escape>', ev)

start()

menubar = Menu(tk)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=tk.destroy)
menubar.add_cascade(label="File", menu=filemenu)
tk.config(menu=menubar)

while True:
    if netcheck:
        crv()
    else:
        rv()
    tk.update()
    time.sleep(0.2)
