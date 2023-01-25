from tkinter import *
root = Tk()
root.geometry('700x500')
root['bg'] = "skyblue"
root.title('Tkinter Game')
Label(root, text= 'READ THE PARAGRAPH AND ANSWER THE QUESTIONS' , font = 'arial 15 bold',borderwidth=10,relief=GROOVE,bg="yellow").pack()
x = Label(root, text = 'Click Any One :', font = 'comicsans 15 bold',bg='black',fg = 'ghost white')
x.place(x=140, y=180)
x.pack(expand=1)

def printlab1():
    print("Congrats! You guessed all correct.")

def madlib1():
    print('''say  cheese  the photographer said as the camera flashed! 
Alex  and I had gone to berlin to get our photos taken on my birthday. 
The first photo we really wanted was a picture of us dressed as tiger and lion pretending to be a doctor. 
when we saw the second photo, it was exactly what I wanted. 
We both looked like  table cloth  wearing  check shirt and Love --exactly what I had in mind''')

    print("From the following paragraph find the following and answer")
    
    animals= input('enter a animal name : ') == "tiger and lion"
    profession = input('enter a profession name: ') == "doctor"
    things = input('enter a thing name: ') == "table cloth"
    name= input('enter a name: ') == "Alex"
    place = input('enter a place name: ') == "berlin"
    verb = input('enter a verb in ing form: ') == "Love"
    food = input('food name: ') == "cheese"

    if animals and profession and things and name and place and verb and food == True:
        printlab1()
    else:
        print("Oops! You got something  wrong try again")

    

def madlib2():
   
    print('''Last night I dreamed I was a big butterfly with pink 
splocthes that looked like bottle .I flew to garden 
with my bestfriend and Mother who was a  small ant
.We ate some pizza when we got there and then decided to fly and the dream ended when I said-- lets fly.''')
    
    print("From the following paragraph find the following and answer")

    adjactive = input('enter adjective : ') == "big"
    color = input('enter a color name : ') == "pink"
    thing = input('enter a thing name :') == "bottle"
    place = input('enter a place name : ') == "garden"
    person= input('enter a person name : ') == "Mother"
    adjactive1 = input('enter an adjactive : ') == "small"
    insect= input('enter an insect name : ') == "ant"
    food = input('enter a food name : ') == "pizza"
    verb = input('enter a verb name : ') == "fly"

    if adjactive and color and thing and place and person and adjactive1 and insect and food and verb == True:
        printlab1()
    else:
        print("Oops! You got something  wrong try again")

def madlib3():

    print('''Today we picked apple from Olive's Orchard. I had no idea there were so many different varieties of apples. I ate red 
apples straight off the tree that tested like sugarcane. Then there was a small 
apple that looked like a ball. When our bag were full, we went on a free hay ride to 
garden and back. It ended at a hay pile where we got to eat 
slowly. I can hardly wait to get home and cook with the apples. We are going to make apple juice and creamy pies!.''')  
    
    person = input('enter person name: ') == "Olive"
    color = input('enter color : ') == "red"
    foods = input('enter food name : ') == "sugarcane"
    adjective = input('enter aa adjective name: ') == "small"
    thing = input('enter a thing name : ') == "ball"
    place = input('enter place : ') == "garden"
    verb = input('enter verb : ') == "eat"
    adverb = input('enter adverb : ') == "slowly"
    drink = input('enter food name: ') == "juice"
    things = input('enter a thing name : ') == "creamy"

    if drink and color and thing and place and person and adjective and adverb and foods and verb and things == True:
        printlab1()
    else:
        print("Oops! You got something  wrong try again")
   

y1 = Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white')
y1.place(x=260, y=120)
y1.pack(expand=1)
y2 = Button(root, text= 'apple and apple', font ='arial 15', command = madlib3 , bg = 'ghost white')
y2.place(x=270, y=180)
y2.pack(expand=1)
y3 = Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white')
y3.place(x=280, y=240)
y3.pack(expand=1)
root.mainloop()
