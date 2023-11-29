from tkinter import*
from PIL import ImageTk, Image


def every_1000(text):
    final_text= ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i%100 ==0 and  i!=0:
            final_text += "\n"
            return final_text
          


root=Tk()
root.title("The hardwork")
root.geometry("1000x800")

texts = []
photos = []
for i in range(0 ,3):
  
    with open(f"{i+1}.txt", encoding="utf8") as file:
        text= file.read()
        texts.append((text))

image = Image.open(f"{i+1}.jpg" )
#TODO: resize these images 
image =image.resize((225, 225), Image.ANTIALIAS)
photos.append(ImageTk.PhotoImage(image))

f1= Frame(root, width=100,height=70)
Label(f1, text="The Karan's Magzines",font="lucida 33 bold").pack()
Label(f1, text="December 21",font="lucida 14 bold").pack()
f1.pack()



f2 =Frame(root,width=900,height=200)
Label(f2, text=texts[0] ,padx=22 ,pady=22).pack(side="left")
Label(f2 , image=photos[0] , anchor="e").pack()
f2.pack(anchor="w")

f3 =Frame(root,width=900,height=200)
Label(f3, text=texts[1] ,padx=22 ,pady=22).pack(side="left")
Label(f2 , image=photos[1] , anchor="e").pack()
f3.pack(anchor="w")

f4 =Frame(root,width=900,height=200)
Label(f4, text=texts[2] ,padx=22 ,pady=22).pack(side="left")

f4.pack(anchor="w")



root.mainloop()
