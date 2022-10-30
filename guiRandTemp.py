# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:41:43 2019

@author: jacob
generate random plus trend stations then calculate when the low happened
"""
from PIL import Image
from tkinter import Tk, BOTH ,LEFT,RIGHT, Button
from tkinter.ttk import Frame,Entry,Label
import random


class Example(Frame):
    years = 0
    
    def __init__(self):
        super().__init__()
        self.lowtemp = []
        self.initUI()

    def initUI(self):
        self.master.title("trend plus noise")
        FLeft = Frame(self)
        FLeft.pack(side = LEFT)
        FRight = Frame(self)
        FRight.pack(side = RIGHT)
        btn = Button(self,text="run me ",command=self.on_click)
        btn.pack(fill = BOTH)
        l = Label(FLeft,text="number of stations")
        l.pack( )
        self.e = Entry(FRight)
        self.e.insert(0,"1000") #default to 1000 stations
        self.e.pack()
        l2 = Label(FLeft,text="length in years")
        l2.pack()
        self.e2 = Entry(FRight)
        self.e2.insert(0,"100") # 100 years
        self.e2.pack()
        l3 = Label(FLeft,text="trend per year")
        l3.pack()
        self.e3 = Entry(FRight)
        self.e3.insert(0,"0.003") # 0.003 trend per year
        self.e3.pack()
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()


    def centerWindow(self):

        w = 290
        h = 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
    def on_click(self):
        txt = self.e.get()
        for x in range(int(txt)):
            self.rand_station()
        
        self.lowtemp.sort()
        #for y in self.lowtemp:
        #   print(y)
           
        self.rootwindow.destroy()
        # add a way to count number of lows
        self.count_mins()
             
    def rand_station(self):
            station = []
            self.years = int(self.e2.get())
            ytrend = float( self.e3.get())
            for x in range(self.years):
                # random plus small trend
                station.append(random.gauss(0,1)+x*ytrend)
    
            m = min(station)
            for y in range(int(self.years)):
                if station[y] == m:
                    self.lowtemp.append(y)


    def count_mins(self):
        # draw trend line of records
        img = Image.new("RGB",(self.years,50))
        cval = 0 # prime loop
        nval = 0
        count = 0
        for x in self.lowtemp:
            count += 1
            if(x == nval):
                cval += 1
            else:
                print((nval ),"   ",cval)
                img.putpixel((nval,cval),255)
                nval = x
                cval = 1
            # print last element
            if count == len(self.lowtemp):
                print((nval ),"   ",cval)     
                img.putpixel((nval,cval),255)

        img.save("trend.bmp")


def main():
    root = Tk()
    ex = Example()
    ex.rootwindow = root
    root.mainloop()

if __name__ == '__main__':
    main()