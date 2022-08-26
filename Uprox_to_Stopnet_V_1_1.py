import tkinter.font
from tkinter import *

win = tkinter.Tk()
win.title("UPROX <--> StopNet")
win.geometry('590x250+100+100')
ButtonFont = tkinter.font.Font(family='Hervetica', size=10, weight='bold')
BigFont = tkinter.font.Font(family='Hervetica', size=12, weight='bold')

td = ''
input_uprox_code = "Введи код UPROX!"
input_stopnet_code = "Введи код StopNet!"
eight_bit = "Ти заэбав! Менше цифр, 8 байт всього!"
zaibal = "Ти заэбав, не вводь хуйню!"
wrong = "ERROR"


def chekinputuprox():
    up_hex_code = uproxCodeEntryHEX.get()
    up_dec_code = uproxCodeEntryDEC.get()
    if up_hex_code == '' and up_dec_code == '':
        statusEntry.delete(0, END)
        stopNetCodeEntryHEX.delete(0, END)
        stopNetCodeEntryDEC.delete(0, END)
        statusEntry.insert(0, input_uprox_code)
        stopNetCodeEntryHEX.insert(0, wrong)
        stopNetCodeEntryDEC.insert(0, wrong)
    else:
        if up_hex_code != '' and up_dec_code != '':
            statusEntry.delete(0, END)
            stopNetCodeEntryHEX.delete(0, END)
            stopNetCodeEntryDEC.delete(0, END)
            statusEntry.insert(0, "Дядя, введи щось одне в UPROX! ")
            stopNetCodeEntryHEX.insert(0, wrong)
            stopNetCodeEntryDEC.insert(0, wrong)
        else:
            if up_hex_code != '':
                converttostopnet_hex()
            else:
                converttostopnet_dec()


def chekinputstopnet():
    st_hex_code = stopNetCodeEntryHEX.get()
    st_dec_code = stopNetCodeEntryDEC.get()
    if st_hex_code == '' and st_dec_code == '':
        statusEntry.delete(0, END)
        uproxCodeEntryHEX.delete(0, END)
        uproxCodeEntryDEC.delete(0, END)
        statusEntry.insert(0, input_stopnet_code)
        uproxCodeEntryHEX.insert(0, wrong)
        uproxCodeEntryDEC.insert(0, wrong)
    else:
        if st_hex_code != '' and st_dec_code != '':
            statusEntry.delete(0, END)
            uproxCodeEntryHEX.delete(0, END)
            uproxCodeEntryDEC.delete(0, END)
            statusEntry.insert(0, "Дядя, введи щось одне в StopNet! ")
            uproxCodeEntryHEX.insert(0, wrong)
            uproxCodeEntryDEC.insert(0, wrong)
        else:
            if st_hex_code != '':
                converttouprox_hex()
            else:
                converttouprox_dec()


def replacer(data):
    rpm = []
    rpm_mass = [3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8, 15, 14, 13, 12, 19, 18, 17, 16, 23, 22, 21, 20,
                27, 26, 25, 24, 31, 30, 29, 28, 35, 34, 33, 32, 39, 38, 37, 36, 43, 42, 41, 40,
                47, 46, 45, 44, 51, 50, 49, 48, 55, 54, 53, 52, 59, 58, 57, 56, 63, 62, 61, 60]
    for i in range(0, 64):
        rpm.insert(i, data[rpm_mass[i]])
    return rpm


def uproxclear():
    uproxCodeEntryDEC.delete(0, END)
    uproxCodeEntryHEX.delete(0, END)


def stopnetclear():
    stopNetCodeEntryDEC.delete(0, END)
    stopNetCodeEntryHEX.delete(0, END)


def allfieldsclear():
    uproxclear()
    stopnetclear()


def exitprogram():
    try:
        win.destroy()
    except NameError:
        win.exit()


def converttostopnet_hex():
    
    """converttostopnetHEX"""
    
    statusEntry.delete(0, END)
    stopnetclear()
    uproxCodeEntryDEC.delete(0, END)
    try:
        data = uproxCodeEntryHEX.get()
        databin = int(data, 16)
        databin2 = bin(databin)
#        print(data)
#        print(databin)
#        print(databin2)
        uproxCodeEntryDEC.delete(0, END)
        uproxCodeEntryDEC.insert(0, ((str(databin)).upper()).replace("0X", "", 1))
        mass = list(databin2)
        mass.pop(0)
        mass.pop(0)
        howmany = len(mass)
        if howmany >= 65:
            statusEntry.delete(0, END)
            statusEntry.insert(0, eight_bit)
        else:
            while howmany < 64:
                mass.insert(0, '0')
                howmany = len(mass)
#        print(howmany)
#        print(mass)
        stmass = replacer(mass)
        datast_dec = str(int(''.join(stmass), 2)).upper()
        datast_hex = hex(int(''.join(stmass), 2)).upper()
#        print(datast_dec)
#        print(datast_hex)
        stopnetclear()
        stopNetCodeEntryDEC.insert(0, datast_dec)
        stopNetCodeEntryHEX.insert(0, datast_hex.replace("0X", "", 1))

    except ValueError:
        err = uproxCodeEntryHEX.get()
        if err == '':
            statusEntry.delete(0, END)
            stopnetclear()
            statusEntry.insert(0, input_uprox_code)
            stopNetCodeEntryHEX.insert(0, wrong)
            stopNetCodeEntryDEC.insert(0, wrong)
        else:
            statusEntry.delete(0, END)
            statusEntry.insert(0, zaibal)
            stopnetclear()
            stopNetCodeEntryHEX.insert(0, wrong)
            stopNetCodeEntryDEC.insert(0, wrong)


def converttouprox_hex():
    
    """converttouproxHEX"""
    
    statusEntry.delete(0, END)
    uproxclear()
    stopNetCodeEntryDEC.delete(0, END)
    try:
        data = stopNetCodeEntryHEX.get()
        databin = int(data, 16)
        databin2 = bin(databin)
#        print(data)
#        print(databin)
#        print(databin2)
        stopNetCodeEntryDEC.delete(0, END)
        stopNetCodeEntryDEC.insert(0, ((str(databin)).upper()).replace("0X", "", 1))
        mass = list(databin2)
        mass.pop(0)
        mass.pop(0)
        howmany = len(mass)
        if howmany >= 65:
            statusEntry.delete(0, END)
            statusEntry.insert(0, eight_bit)
        else:
            while howmany < 64:
                mass.insert(0, '0')
                howmany = len(mass)
#        print(howmany)
#        print(mass)
        stmass = replacer(mass)

        datast_dec = str(int(''.join(stmass), 2)).upper()
        datast_hex = hex(int(''.join(stmass), 2)).upper()
#        print(datast_dec)
#        print(datast_hex)
        uproxclear()
        uproxCodeEntryDEC.insert(0, datast_dec)
        uproxCodeEntryHEX.insert(0, datast_hex.replace("0X", "", 1))

    except ValueError:
        err = stopNetCodeEntryHEX.get()
        if err == '':
            statusEntry.delete(0, END)
            uproxclear()
            statusEntry.insert(0, input_stopnet_code)
            uproxCodeEntryHEX.insert(0, wrong)
            uproxCodeEntryDEC.insert(0, wrong)
        else:
            statusEntry.delete(0, END)
            statusEntry.insert(0, zaibal)
            uproxclear()
            uproxCodeEntryHEX.insert(0, wrong)
            uproxCodeEntryDEC.insert(0, wrong)


def converttostopnet_dec():
    
    """converttostopnetDEC"""
    
    statusEntry.delete(0, END)
    stopnetclear()
    uproxCodeEntryHEX.delete(0, END)
    try:
        data = uproxCodeEntryDEC.get()
        datahex = hex(int(data, 10))
        databin = int(data, 10)
        databin2 = bin(databin)
        uproxCodeEntryHEX.delete(0, END)
        uproxCodeEntryHEX.insert(0, (datahex.upper()).replace("0X", "", 1))
#        print(data)
#        print(databin)
#        print(databin2)
        mass = list(databin2)
        mass.pop(0)
        mass.pop(0)
        howmany = len(mass)
        if howmany >= 65:
            statusEntry.delete(0, END)
            statusEntry.insert(0, eight_bit)
        else:
            while howmany < 64:
                mass.insert(0, '0')
                howmany = len(mass)
#        print(howmany)
#        print(mass)
        stmass = replacer(mass)

        datast_dec = str(int(''.join(stmass), 2)).upper()
        datast_hex = hex(int(''.join(stmass), 2)).upper()
#        print(datast_dec)
#        print(datast_hex)
        stopnetclear()
        stopNetCodeEntryDEC.insert(0, datast_dec)
        stopNetCodeEntryHEX.insert(0, datast_hex.replace("0X", "", 1))

    except ValueError:
        err = uproxCodeEntryDEC.get()
        if err == '':
            statusEntry.delete(0, END)
            stopnetclear()
            statusEntry.insert(0, input_uprox_code)
            stopNetCodeEntryHEX.insert(0, wrong)
            stopNetCodeEntryDEC.insert(0, wrong)
        else:
            statusEntry.delete(0, END)
            statusEntry.insert(0, zaibal)
            stopnetclear()
            stopNetCodeEntryHEX.insert(0, wrong)
            stopNetCodeEntryDEC.insert(0, wrong)


def converttouprox_dec():
    
    """converttouproxDEC"""
   
    statusEntry.delete(0, END)
    uproxclear()
    stopNetCodeEntryHEX.delete(0, END)
    try:
        data = stopNetCodeEntryDEC.get()
        datahex = hex(int(data, 10))
        databin = int(data, 10)
        databin2 = bin(databin)
        stopNetCodeEntryHEX.delete(0, END)
        stopNetCodeEntryHEX.insert(0, (datahex.upper()).replace("0X", "", 1))
#        print(data)
#        print(databin)
#        print(databin2)
        mass = list(databin2)
        mass.pop(0)
        mass.pop(0)
        howmany = len(mass)
        if howmany >= 65:
            statusEntry.delete(0, END)
            statusEntry.insert(0, eight_bit)
        else:
            while howmany < 64:
                mass.insert(0, '0')
                howmany = len(mass)
#        print(howmany)
#        print(mass)
        stmass = replacer(mass)

#        print(stmass)
        datast_dec = str(int(''.join(stmass), 2)).upper()
        datast_hex = hex(int(''.join(stmass), 2)).upper()
#        print(datast_dec)
#        print(datast_hex)
        uproxclear()
        uproxCodeEntryDEC.insert(0, datast_dec)
        uproxCodeEntryHEX.insert(0, datast_hex.replace("0X", "", 1))

    except ValueError:
        err = stopNetCodeEntryDEC.get()
        if err == '':
            statusEntry.delete(0, END)
            uproxclear()
            statusEntry.insert(0, input_stopnet_code)
            uproxCodeEntryHEX.insert(0, wrong)
            uproxCodeEntryDEC.insert(0, wrong)
        else:
            statusEntry.delete(0, END)
            statusEntry.insert(0, zaibal)
            uproxclear()
            uproxCodeEntryHEX.insert(0, wrong)
            uproxCodeEntryDEC.insert(0, wrong)
           

uproxLabel = Label(win, text="Uprox card code:", font=BigFont, width=14)
uproxLabel.pack()
uproxLabel.place(x=420, y=10)

uproxCodeEntryHEX = Entry(win, font=ButtonFont, width=20)
uproxCodeEntryHEX.pack()
uproxCodeEntryHEX.place(x=420, y=40)

uproxCodeEntryDEC = Entry(win, font=ButtonFont, width=20)
uproxCodeEntryDEC.pack()
uproxCodeEntryDEC.place(x=420, y=145)

stopNetLabel = Label(win, text="StopNet card code:", font=BigFont, width=14)
stopNetLabel.pack()
stopNetLabel.place(x=20, y=10)

stopNetCodeEntryHEX = Entry(win, font=ButtonFont, width=20)
stopNetCodeEntryHEX.pack()
stopNetCodeEntryHEX.place(x=20, y=40)

stopNetCodeEntryDEC = Entry(win, font=ButtonFont, width=20)
stopNetCodeEntryDEC.pack()
stopNetCodeEntryDEC.place(x=20, y=145)

convertStopnetBut = Button(win, font=BigFont, text="< CONVERT", command=chekinputuprox)
convertStopnetBut.pack()
convertStopnetBut.place(x=180, y=85)

convertUproxBut = Button(win, font=BigFont, text="CONVERT >", command=chekinputstopnet)
convertUproxBut.pack()
convertUproxBut.place(x=300, y=85)

statusEntry = Entry(win, font=ButtonFont, width=50)
statusEntry.pack()
statusEntry.place(x=100, y=210)

statusLabel = Label(win, text="STATUS:", font=BigFont, width=8)
statusLabel.pack()
statusLabel.place(x=0, y=208)

exitBut = Button(win, font=BigFont, text=" EXIT ", command=exitprogram)
exitBut.pack()
exitBut.place(x=500, y=200)

hex_st_Label = Label(win, text="HEX", font=BigFont, width=4)
hex_st_Label.pack()
hex_st_Label.place(x=70, y=60)

hex_uprox_Label = Label(win, text="HEX", font=BigFont, width=4)
hex_uprox_Label.pack()
hex_uprox_Label.place(x=470, y=60)

dec_st_Label = Label(win, text="DEC", font=BigFont, width=4)
dec_st_Label.pack()
dec_st_Label.place(x=70, y=120)

dec_uprox_Label = Label(win, text="DEC", font=BigFont, width=4)
dec_uprox_Label.pack()
dec_uprox_Label.place(x=470, y=120)

uproxclearBut = Button(win, font=ButtonFont, text="CLEAR", command=allfieldsclear)
uproxclearBut.pack()
uproxclearBut.place(x=465, y=88)

clearStopnetBut = Button(win, font=ButtonFont, text="CLEAR", command=allfieldsclear)
clearStopnetBut.pack()
clearStopnetBut.place(x=65, y=88)

mainloop()
