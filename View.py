from tkinter import *
import tkinter,time
from tkinter import messagebox
from Controller import Logic

def showCanvas(info,bottomFrame):
    font_size = ('Verdana', 16)
    Label(bottomFrame,text ='City : ' + info['name']  ,font=font_size,bg = 'grey').place(x=0,y=160)
    Label(bottomFrame,text = 'Country : ' + info['country'] ,font=font_size,bg = 'grey').place(x=0,y = 190)
    Label(bottomFrame,text = 'Temperature : ' + str(info['temp']) + ' (in celcius)', font = font_size,bg = 'grey').place(x=0,y=220)
    Label(bottomFrame,text = 'Humidity : ' + str(info['humidity']) + ' (in celcius)', font = font_size,bg = 'grey').place(x=0,y=250)
    Label(bottomFrame,text = 'Min Temp : ' + str(info['temp_min']) + ' (in celcius)', font = font_size,bg = 'grey').place(x=0,y=280)
    Label(bottomFrame,text = 'Max Temp : ' + str(info['temp_max']) + ' (in celcius)', font = font_size,bg = 'grey').place(x=0,y=310)
    Label(bottomFrame,text ='Coordinates : ' + 'Lattitude :- ' + str(info['lat']) + ' , ' + 'Longitude :- '  + str(info['lon']),font=('Verdana', 16),bg = 'grey').place(x=0,y=340)
    Label(bottomFrame, text='Pressure : ' + str(info['pressure']), font=font_size, bg='grey').place(x=0, y=370)
    Label(bottomFrame, text='Sunrise : ' + str(time.ctime(info['sunrise'])) , font=font_size, bg ='grey').place(x=0, y=400)
    Label(bottomFrame, text='Sunset : ' + str(time.ctime(info['sunset'])), font=font_size, bg ='grey').place(x=0, y=430)
    Label(bottomFrame, text='Weather : ' + info['weather'], font=font_size, bg='grey').place(x=0, y=460)


def showError(info):
    messagebox.showerror('Error Message','Error Code : ' + info['cod'] + '  & ' + info['message'])

def entry_hi():

    if city_name.get() is '':
        test = Frame(window, width=600, height=600).grid(row=1, column=0)
        messagebox.showinfo('Warning','Please Enter the City')
    else:
        bottomFrame = Frame(window, width=600, height=600, bg='grey').grid(row=1, column=0)
        flag,info = Logic(city_name.get()).getJson()
        if flag == True :
            showCanvas(info,bottomFrame)
        else :
            showError(info)




window = tkinter.Tk()
window.geometry('600x500')
window.title('Weather Application')
window.resizable(width = False,height = False)
entry1Var = StringVar()

''' Making Frames '''

topFrame = Frame(window,width = 600,height = 130).grid(row=0,column=0)


'''Making Labels '''

welcome_label = Label(topFrame, text='Welcome to Weather Checking App', font=('Verdana', 15)).place(x=120, y=10)
choose_city = Label(topFrame, text='Chose City', font=('Verdana', 20)).place(x=20, y=57)
button = Button(topFrame, text='Press', fg='red', width=10, height=1, command=entry_hi).place(x=470, y=60)

''' Making Buttons '''

city_name = StringVar()
entry_city = Entry(topFrame,textvariable=city_name,font=('Verdana', 15)).place(x=200, y=60)


window.mainloop()
