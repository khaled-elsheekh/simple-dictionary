# import modules

from tkinter import *
import sqlite3
import pyttsx3
import time
from awesometkinter import Button3d
from awesometkinter.bidirender import render_bidi_text , render_text
from ttkwidgets.autocomplete import AutocompleteEntry
from googletrans import Translator

win = Tk()
win.title('dictionary'.upper())
win.attributes('-type','normal')
win.attributes('-alpha', 1.0 )
win.iconphoto(True, PhotoImage(file='/home/poss/projcets/dictionary/dic.png'))
win.wm_resizable(False,False)
win.attributes('-topmost',False)

wid = win.winfo_screenwidth()//2 - 700//2
hei = win.winfo_screenheight()//2 - 300//2
win.geometry(f'+{wid}+{hei}')
win.wm_overrideredirect(0)
win.config(bd=5,bg='#140033')

def about_():
    win1 =Tk()
    win1.title('about us'.title())
    win1.geometry('350x250+600+20')
    lab = Label(win1,text=''' simple dictionary
    =======================
    version = 1.0 
    copyright elsheik 2021\nall rights reserved
    for information about this application  
    email : khaled.elsheekh@gmail.com''',bg='#140033',fg='silver',font='arial 12 bold' )
    lab.pack(expand=1,fill='both')
    btn = Button(win1,text='close',command=lambda: win1.destroy())
    btn.pack()

def clear():
    trans_e.config(bg='white')
    word_e.delete(0, 'end')
    trans_e.delete(0, 'end')

def git_trans1():
    try:
        # trans_e.config(bg='white')
        trans_e.delete(0,END)
        trans_e.config(bg='white')

        word = f"'{word_e.get()}'"

        trans = Translator()
        
        trans1 = trans.translate(text=word,dest='ar')
        
        trans_e.insert('end',render_bidi_text(trans1.text).strip("'"))
    except:
        trans_e.config(bg='red')
        trans_e.insert('end','no network connection!!!!!!'.title())
        
            
            
def minidic():
    win.iconify()
    dic =Toplevel(win)
    dic.overrideredirect(0)
    dic.attributes('-type','normal')
    dic.attributes('-alpha',1.0)
    dic.geometry('+700+800')
    dic.attributes('-topmost',True)
    dic.config(bd=5,bg='#140033') 
    dic.grab_set()
    


    
    def look_for():
        word_e_mini_rans = f"'{word_e_mini.get().title()}'"
        var = cursor.execute('select * from dict')
        for row in var:
            if word_e_mini_rans == row[1]:
                trans_e_mini.delete(0,'end')
                # talk()
                trans_e_mini.insert('end',render_bidi_text(row[2]).strip("'("))

    con = sqlite3.connect('/home/poss/projcets/dictionary/dict_data.db')
    cursor = con.cursor()       
    mini =Frame(dic)
    mini.pack()
    
    def clear():
        word_e_mini.delete(0,'end')
        trans_e_mini.delete(0,'end')

    def git_trans():
        try:
            trans_e_mini.delete(0,END)
            trans_e_mini.config(bg='white')
            word = f"'{word_e_mini.get()}'"

            trans = Translator()
            
            trans1 = trans.translate(text=word,dest='ar')
            
            trans_e_mini.insert('end',render_bidi_text(trans1.text).strip("'"))
        except:
            trans_e_mini.config(bg='red')

            trans_e_mini.insert('end','no network connection!!!!!'.title())


    word_lab_mini = Label(mini,text='word'.title(),bg='#140033',fg='white')
    tran_btn = Button(mini,text='translate'.title(),bg= '#ff3700',cursor='hand2',command=look_for)
    word_e_mini = Entry(mini,justify='center',bg='#D3D3D3',highlightcolor='#140033')
    word_e_mini.focus()
    trans_e_mini = Entry(mini,justify='center',bg='#D3D3D3',font='bold')
    google_btn = Button(mini,text='google'.title(),bg= '#ff3700',cursor='hand2',command=git_trans)
    exit_btn = Button(mini,text='clear'.title(),cursor='hand2',bg= '#140033',fg='white',command=clear)
    word_lab_mini.pack(side='left')
    word_e_mini.pack(side='left')
    tran_btn.pack(side='left')
    trans_e_mini.pack(side='left')
    exit_btn.pack(side='right')
    google_btn.pack(side='right')

def talk():
    word_to_trans = word_e.get()
    if len(word_to_trans) == 0:
        engine = pyttsx3.init('espeak')
        # rate = engine.getProperty('rate')  # getting details of current speaking rate
        engine.setProperty('rate', 130)  # setting up new voice rate
        engine.say('enter word please')
        engine.runAndWait()
    else:
        word_to_trans = word_e.get()
        engine = pyttsx3.init('espeak')
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        engine.setProperty('rate', 100)  # setting up new voice rate
        engine.say(word_to_trans)
        engine.runAndWait()


def copy():
    word_e.get()


def look_for(event=None):
    word_to_trans = f"'{word_e.get().title()}'"
    var = cursor.execute('select * from dict')
    for row in var:
        if word_to_trans == row[1]:
            trans_e.delete(0,'end')
            talk()
            trans_e.insert('end',render_bidi_text(row[2]).strip("'("))

def clock():
    tim = time.strftime('%I:%M:%S: %p')
    clock_label.config(text=tim,relief='sunken',bg='#0c022e',fg='#ff3700',font='jost 15 bold')
    clock_label.after(1000, clock)
con = sqlite3.connect('/home/poss/projcets/dictionary/dict_data.db')
cursor = con.cursor()

def open_site():
    import webbrowser
    webbrowser.open('https://translate.google.com/?sl=en&tl=ar&op=translate')


#=========================  option frame ==============================    

option_frame = Frame(win,width=600,height=30,bg='#140033')
option_frame.grid(row=0 ,column=0,columnspan=3,pady=5)




clock_label = Label(option_frame, text='',bd=0,bg='grey',width=12)
clock_label.place(y=0,x=200)
open_url_btn = Button(win,text='google url'.title(),cursor='hand2',justify='left',bg='#140033',fg='#ff3700',activebackground='#ff3700',bd=1,highlightthickness=0,command=open_site)
open_url_btn.place(y=5,x=535,width='120')
abou = Button(win,text='about'.title(),cursor='hand2',fg='#140033',bg='#ff3700',activebackground='#00af00',bd=1,highlightthickness=0,relief=GROOVE,command=about_)
# abou.place(y=5,x=535,bordermode='inside',width='70')
abou.grid(row=3,column=4)



word_lab = Label(win,text='word'.title(),font='times 15 bold',height=1,bg='#140033',fg='#ffffff',bd=5)
word_lab.grid(row=1 ,column=0)
trans_lab = Label(win,text='translation'.title(),font='times 15 bold',height=1,bg='#140033',fg='#ffffff',bd=5)
trans_lab.grid(row=2 ,column=0)
word_e =  Entry(win,width=35,relief=SUNKEN,justify='center', bd=3,font='times 17 bold',bg='#fff',highlightcolor='#140033')
word_e.grid(row=1 ,column=1,pady=(0,5))
word_e.focus()
trans_e = Entry(win,width=35,relief=SUNKEN,justify='center', bd=3,font='times 17 bold',bg='#fff')
trans_e.grid(row=2 ,column=1 )
im = PhotoImage(file='/home/poss/projcets/talk.png')
# talk_btn = Button3d(win,image=im,cursor='hand2',compound='center',bg='silver',command=talk)
talk_btn = Button(win,image=im,text=' talk ',cursor='hand2',compound='center',bg='#140033',fg='#ff3700',height=15,  activebackground='#ff3700',bd=1,highlightthickness=0,command=talk)
talk_btn.grid(row=1 ,column=2)
copy_btn1 = Button(win,text='copy'.title(),cursor='hand2',fg='#140033',bg='#ff3700',activebackground='#00af00',highlightthickness=0,command=copy)
copy_btn1.grid(row=2 ,column=4,)

mini = Button(win,text='mini'.title(),cursor='hand2', fg='#140033',bg='#ff3700',activebackground='#00af00',highlightthickness=0,   bd=1,command=minidic)
mini.grid(row=1,column=4,columnspan=4)
tran_btn = Button3d(win,text='translate '.upper(),bg= '#ff3700',cursor='hand2',command=lambda:look_for(1))
tran_btn.grid(row=3 ,column=0,padx=(0,10),columnspan=2)
tran_btn1 = Button3d(win,text='google'.upper(),bg= '#ff3700',cursor='hand2',command=git_trans1)
tran_btn1.grid(row=3 ,column=1,padx=(30,0),columnspan=3)

clear_btn = Button(win,text='clear'.title(),cursor='hand2',bg='#140033',fg='#ff3700',activebackground='#ff3700',bd=1,highlightthickness=0, command=clear)
clear_btn.grid(row=2 ,column=2,ipadx=0)
exit_btn = Button(win,text='exit'.title(),cursor='hand2',bg='#140033',fg='#ff3700',activebackground='#ff3700',bd=1,highlightthickness=0, command=win.quit)
exit_btn.grid(row=3 ,column=2,ipadx=5)


word_e.bind('<Return>', look_for)
clock()
win.mainloop()
# http://www.eso.org/projects/vlt/sw-dev/tcl8.4.19/html/TkCmd/wm.htm#M8