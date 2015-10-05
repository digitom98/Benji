# coding=utf-8
import threading
import urllib

import webbrowser
import os
import winsound
import time
import urllib.request as ur

#from gtts import gTTS

from random import randint
from tkinter import *

#############WINDOW AND FRAME ############################
myWindows = Tk()
myWindows.configure(background='black')
myWindows.wm_title("Benji : Assistant Personnel")
myWindows.iconbitmap('Benji_icon.ico')
myFrame = Frame(myWindows, bg="black")
myFrame.pack()
myWindows.geometry('{}x{}'.format(600, 400))


imagelist = ["0002.png", "0003.png", "0004.png", "0005.png", "0006.png", "0007.png", "0008.png", "0009.png", "0010.png",
             "0011.png", "0012.png", "0013.png", "0014.png", "0015.png", "0016.png", "0017.png", "0018.png", "0018.png",
             "0019.png", "0020.png", "0021.png", "0022.png", "0023.png", "0024.png", "0025.png", "0026.png", "0027.png",
             "0028.png", "0029.png", "0030.png", "0031.png", "0032.png", "0033.png", "0034.png", "0035.png"]


# extract width and height info



##############################################################

##################GIF FRAMES##################################

###############FIND String Between 2##########################
def quit():
    quit()


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


##############################################################


def submitTxt():
    print(textbox.get())

    if "salut" in textbox.get() or "bonjour" in textbox.get() or "hey" in textbox.get():
        answer.configure(text="Bonjour !")
        print("Bonjour !")

    elif "ca va" in textbox.get() or "comment allez" in textbox.get() or "vas-tu" in textbox.get() or "vas tu" in textbox.get():
        answer.configure(text="Je vais tres bien, merci.")
        answer.update()
        print("Je vais tres bien, merci.")
        winsound.PlaySound("TresBien.wav", winsound.SND_ALIAS)

    elif "comment" in textbox.get() and "va" in textbox.get():
        answer.configure(text="Je vais tres bien, merci.")
        answer.update()
        print("Je vais tres bien, merci.")

    elif "qui es-tu" in textbox.get() or "qui etes" in textbox.get() or "qui es tu" in textbox.get():
        answer.configure(text="Je suis Benji, votre assistant personnel, pour vous servir.")
        answer.update()
        print("Je suis Benji, votre assistant personnel, pour vous servir.")

    elif "ouvre" in textbox.get() or "lance" in textbox.get() or "execute" in textbox.get():

        if "bloc" in textbox.get() or "blocnote" in textbox.get() or "blocnotes" in textbox.get():
            answer.configure(text="Application Bloc Notes ouverte.")
            answer.update()
            os.system('notepad.exe')

        elif "internet" in textbox.get() or "google" in textbox.get() or "IE" in textbox.get():
            answer.configure(text="Ouverture de www.google.fr")
            answer.update()
            time.sleep(1)
            webbrowser.open_new("www.google.fr")

    elif "definition" in textbox.get() or "définition" in textbox.get() or "dictionnaire" in textbox.get() or "signifie" in textbox.get():

        keyword = ""

        mystring = textbox.get()
        if "finition" in textbox.get() and not "finition de" in textbox.get() and not "mot" in textbox.get():
            keyword = 'finition '
        elif "du mot" in textbox.get():
            keyword = "mot "
        elif "finition de" in textbox.get():
            keyword = 'finition de '
        elif "signifie" in textbox.get():
            keyword = 'signifie '
        elif "cherche" in textbox.get() and not "finition" in textbox.get():
            keyword = 'cherche '

        before_keyowrd, keyword, after_keyword = mystring.partition(keyword)

        wordtodefine = after_keyword.split(' ', 1)[0]

        print(wordtodefine)

        htmlfile = ur.urlopen("http://www.cnrtl.fr/definition/" + wordtodefine)
        htmltext = htmlfile.read()
        print(htmltext)
        definition = find_between(str(htmltext), '<span class="tlf_cdefinition">', '</span>')
        process1 = definition.replace(" ", "0espace0").replace(",", "0virgule0").replace(".", "0point0").replace(";", "0ptvirgule0") \
            .replace("'", "0apostrophe0").replace("(", "0debparenthese0").replace(")", "0finparenthese0")
        process2 = ''.join(e for e in process1 if e.isalnum())
        process3 = process2.replace("xc3xa9", "é").replace("0espace0", " ").replace("0virgule0", ",").replace("0point0", ".").replace(
            "xc3x8a", "Ê").replace("xc3xaa", "ê").replace("0ptvirgule0", ";").replace("xc3x89", "É").replace("xc3xa8", "è") \
            .replace("xc3xa0", "à").replace("0apostrophe0", "'").replace("0debparenthese0", "(").replace("0finparenthese0", ")").replace("isup1sup", " ") \
            .replace("xc3xb4", "ô").replace(',,', "").replace('xc3xbb', "û").replace("i(","(").replace(") i",") ").replace("xc5x93", "œ").replace("xc3xaf","ï")
        print(process3)
        deff, key, conneries = process3.partition("(span")
        process4 = deff
        if process4 != "":
            answer.configure(text=wordtodefine + ": " + process4)
            #tts = gTTS(text=process4, lang="fr")
            #tts.save("definition.mp3")
            #os.system('definition.mp3')

        else:
            answer.configure(text="Aucune définition trouvée, désolé.")
        answer.update()



    elif "cherche" in textbox.get() and "sur" in textbox.get() or "cherche" in textbox.get() and "dans" in textbox.get():
        s = textbox.get()
        if not "dans" in textbox.get():
            answer.configure(text="Recherche de : '" + find_between(s, "cherche ", " sur") + "' sur le web")
            answer.update()
            time.sleep(1.5)
            print(find_between(s, "cherche ", " sur"))
            urll = "http://www.google.fr/search?q=" + find_between(s, "cherche ", " sur")
            webbrowser.open(urll)
            print(urll)
        else:
            answer.configure(text="Recherche de : '" + find_between(s, "cherche ", " dans") + "' sur le web")
            answer.update()
            time.sleep(1.5)
            urll = "http://www.google.fr/search?q=" + find_between(s, "cherche ", " dans")
            webbrowser.open(urll)

    else:
        answer.configure(text="Desole, je n'ai pas compris...")
        answer.update()
        print("Desole, je n'ai pas compris...")

    textbox.delete(0, END)


# loop through the gif image objects for a while

def playAnim(event):
    incrementer = randint(2, 5)

    for k in range(0, incrementer):
        for gif in giflist:
            canvas.delete(ALL)
            canvas.create_image(width / 2.0, height / 2.0, image=gif)
            canvas.update()
            time.sleep(0.01)
    submitTxt()


##########GLOBAL UI#############################################
photo = PhotoImage(file=imagelist[0])
width = photo.width()
height = photo.height()
canvas = Canvas(myFrame, width=width, height=height, bg="black", highlightbackground="black")
canvas.pack()
idle = PhotoImage(file="0002.png")
canvas.create_image(width / 2.0, height / 2.0, image=idle)

answer = Label(myFrame, text="Que puis-je pour vous ?", fg='DeepSkyBlue', bg='black', font="Calibri 14", justify=CENTER,
               wraplength=500)
answer.pack(side=BOTTOM)
textbox = Entry(myWindows, width=18, font="Calibri 14", bg="DeepSkyBlue3", fg="gray14")
textbox.pack(side=BOTTOM, fill=X, ipady=10)
textbox.focus_force()

textbox.bind("<Key>", print("Key pressed"))
textbox.bind("<Return>", playAnim)



# create a list of image objects

giflist = []
for imagefile in imagelist:
    photo = PhotoImage(file=imagefile)
    giflist.append(photo)

myWindows.mainloop()
