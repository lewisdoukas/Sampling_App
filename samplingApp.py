#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#+----------+-----------------------------------------------------------------+
#|   TITLE  | Sampling Coordinates Generator - Plotter Application            |
#+----------+-----------------------------------------------------------------+
#|  AUTHOR  | Ilias Doukas                                                    |
#+----------+-----------------------------------------------------------------+
#|  CONTACT | hliasduke@gmail.com                                             |
#+----------+-----------------------------------------------------------------+
#|          |This GUI application generates sample coordinates using Random,  |
#|          |Systematic and Random Stratified sampling method and saves them  |
#|  DETAILS |in a text file. Also the app calculates statistic measures for   |
#|          |the sample and plots the position of points on a toplevel window.|
#+----------+-----------------------------------------------------------------+

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import matplotlib
import texttable
import pandas as pd
import os
matplotlib.use('TkAgg')


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
#----------------------- M A I N   T K I N T E R   W I N D O W ---------------#
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x550")
        self.master.title(" Sample Coordinates Generator - Plotter ")

#------------------ S E L F   V A R I A B L E S   S E C T I O N --------------#       
        self.maximum = 0
        self.majorSpace = 0
        self.minorSpace = 0
        self.press1 = False
        self.press2 = False
        self.press3 = False
        self.buttonID = 0
        
#----------------------- R A N D O M   S A M P L I N G -----------------------#       
        self.x1r = tk.DoubleVar()
        self.x2r = tk.DoubleVar()
        self.y1r = tk.DoubleVar()
        self.y2r = tk.DoubleVar()
        self.nr = tk.IntVar()
        self.statusr = tk.StringVar() 
        self.expr = tk.StringVar()
        
#--------------------- S Y S T E M A T I C   S A M P L I N G -----------------#        
        self.x1s = tk.DoubleVar()
        self.x2s = tk.DoubleVar()
        self.ns = tk.IntVar()
        self.y1s = tk.DoubleVar()
        self.y2s = tk.DoubleVar()
        self.statuss = tk.StringVar()
        self.exps = tk.StringVar()

#--------------------- S T R A T I F I E D   S A M P L I N G -----------------#      
        self.strata = tk.IntVar()
        self.x1str = tk.DoubleVar()
        self.x2str = tk.DoubleVar()
        self.y1str = tk.DoubleVar()
        self.y2str = tk.DoubleVar()
        self.nstr = tk.IntVar()
        self.statusstr = tk.StringVar()
        self.expstr = tk.StringVar()
#-----------------------------------------------------------------------------#
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
#-------------------------------- W I D G E T S ------------------------------#  
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
        self.frame = tk.Frame(self.master).place(relx= 0, rely= 0, relheight= 1, relwidth= 1)

#---------------------------------- G R O U P   1 ----------------------------#            
        self.group1 = tk.LabelFrame(self.master, text= ' Random Sampling Coordinates ')
        self.group1.place(relx= 0.03, rely=0.01, relheight= 0.28, relwidth= 0.94)
        
        self.labelx1r = tk.Label(self.group1, text= 'Xlow: ').grid(row= 0, column= 0, padx= 5, pady= 10, sticky='w')
        self.entryx1r = tk.Entry(self.group1, textvariable= self.x1r, justify= 'center', width= 13)
        self.entryx1r.grid(row= 0, column= 1, padx= 10, pady= 10, sticky='w')
        self.labelx2r = tk.Label(self.group1, text= 'Xtop: ').grid(row= 0, column= 2, padx= 5, pady= 10, sticky='w')
        self.entryx2r = tk.Entry(self.group1, textvariable= self.x2r, justify= 'center', width= 13)
        self.entryx2r.grid(row= 0, column= 3, padx= 10, pady= 10, sticky='w')
        
        self.labely1r = tk.Label(self.group1, text= 'Ylow: ').grid(row= 1, column= 0, padx= 5, pady= 10, sticky='w')
        self.entryy1r = tk.Entry(self.group1, textvariable= self.y1r, justify= 'center', width= 13)
        self.entryy1r.grid(row= 1, column= 1, padx= 10, pady= 10, sticky='w')
        self.labely2r = tk.Label(self.group1, text= 'Ytop: ').grid(row= 1, column= 2, padx= 5, pady= 10, sticky='w')
        self.entryy2r = tk.Entry(self.group1, textvariable= self.y2r, justify= 'center', width= 13)
        self.entryy2r.grid(row= 1, column= 3, padx= 10, pady= 10, sticky='w')
        
        self.labelnr = tk.Label(self.group1, text= 'Number of points: ', width= 17).place(relx= 0.02, rely= 0.74, relheight= 0.13, relwidth= 0.21)
        self.entrynr = tk.Entry(self.group1, textvariable= self.nr, justify= 'center', width= 8)
        self.entrynr.place(relx= 0.27, rely= 0.73, relheight= 0.17, relwidth= 0.14)
        
        self.calcRS = tk.Button(self.group1, text= '📝 Calculate', activebackground= '#d9d9d9', command= lambda:self.randomSamplingCoordsCalc())
        self.calcRS.place(relx= 0.8, rely= 0.73, relheight= 0.23, relwidth= 0.18)
        
        self.buttonshowRS = tk.Button(self.group1, text= '🔍 Show', state= 'disabled', activebackground= '#d9d9d9', command= lambda:self.showRS())
        self.buttonshowRS.place(relx= 0.8, rely= 0.45, relheight= 0.23, relwidth= 0.18)
        
        self.statusRS = tk.Label(self.group1, textvariable= self.statusr).place(relx= 0.79, rely= 0.08, relheight= 0.13, relwidth= 0.2)
        self.expstatusRS = tk.Label(self.group1, textvariable= self.expr).place(relx= 0.79, rely= 0.27, relheight= 0.13, relwidth= 0.2)

#---------------------------------- G R O U P   2 ----------------------------#  

        self.group2 = tk.LabelFrame(self.master, text= ' Systematic Sampling Coordinates ')
        self.group2.place(relx= 0.03, rely=0.3, relheight= 0.28, relwidth= 0.94)

        self.labelx1s = tk.Label(self.group2, text= 'Xlow: ').grid(row= 0, column= 0, padx= 5, pady= 10, sticky='w')
        self.entryx1s = tk.Entry(self.group2, textvariable= self.x1s, justify= 'center', width= 13)
        self.entryx1s.grid(row= 0, column= 1, padx= 10, pady= 10, sticky='w')
        self.labelx2s = tk.Label(self.group2, text= 'Xtop: ').grid(row= 0, column= 2, padx= 5, pady= 10, sticky='w')
        self.entryx2s = tk.Entry(self.group2, textvariable= self.x2s, justify= 'center', width= 13)
        self.entryx2s.grid(row= 0, column= 3, padx= 10, pady= 10, sticky='w')
        
        self.labely1s = tk.Label(self.group2, text= 'Ylow: ').grid(row= 1, column= 0, padx= 5, pady= 10, sticky='w')
        self.entryy1s = tk.Entry(self.group2, textvariable= self.y1s, justify= 'center', width= 13)
        self.entryy1s.grid(row= 1, column= 1, padx= 10, pady= 10, sticky='w')
        self.labely2s = tk.Label(self.group2, text= 'Ytop: ').grid(row= 1, column= 2, padx= 5, pady= 10, sticky='w')
        self.entryy2s = tk.Entry(self.group2, textvariable= self.y2s, justify= 'center', width= 13)
        self.entryy2s.grid(row= 1, column= 3, padx= 10, pady= 10, sticky='w')
        
        self.labelns = tk.Label(self.group2, text= 'Sampling Interval: ').place(relx= 0.02, rely= 0.74, relheight= 0.13, relwidth= 0.22)
        self.entryns = tk.Entry(self.group2, textvariable= self.ns, justify= 'center', width= 8)
        self.entryns.place(relx= 0.27, rely= 0.73, relheight= 0.17, relwidth= 0.14)
        
        self.calcSS = tk.Button(self.group2, text= '📝 Calculate', activebackground= '#d9d9d9', command= lambda:self.systematicSamplingCoordsCalc())
        self.calcSS.place(relx= 0.8, rely= 0.73, relheight= 0.23, relwidth= 0.18)
        
        self.buttonshowSS = tk.Button(self.group2, text= '🔍 Show', state= 'disabled', activebackground= '#d9d9d9', command= lambda:self.showSS())
        self.buttonshowSS.place(relx= 0.8, rely= 0.45, relheight= 0.23, relwidth= 0.18)
        
        self.statusSS = tk.Label(self.group2, textvariable= self.statuss).place(relx= 0.79, rely= 0.08, relheight= 0.13, relwidth= 0.2)
        self.expstatusSS = tk.Label(self.group2, textvariable= self.exps).place(relx= 0.79, rely= 0.27, relheight= 0.13, relwidth= 0.2)

#---------------------------------- G R O U P   3 ----------------------------#  

        self.group3 = tk.LabelFrame(self.master, text= ' Stratified Random Sampling Coordinates ')
        self.group3.place(relx= 0.03, rely=0.59, relheight= 0.28, relwidth= 0.94)
        
        self.labelx1str = tk.Label(self.group3, text= 'Xlow: ').grid(row= 0, column= 0, padx= 5, pady= 10, sticky='w')
        self.entryx1str = tk.Entry(self.group3, textvariable= self.x1str, justify= 'center', width= 13)
        self.entryx1str.grid(row= 0, column= 1, padx= 10, pady= 10, sticky='w')
        self.labelx2str = tk.Label(self.group3, text= 'Xtop: ').grid(row= 0, column= 2, padx= 5, pady= 10, sticky='w')
        self.entryx2str = tk.Entry(self.group3, textvariable= self.x2str, justify= 'center', width= 13)
        self.entryx2str.grid(row= 0, column= 3, padx= 10, pady= 10, sticky='w')
        
        self.labely1str = tk.Label(self.group3, text= 'Ylow: ').grid(row= 1, column= 0, padx= 5, pady= 10, sticky='w')
        self.entryy1str = tk.Entry(self.group3, textvariable= self.y1str, justify= 'center', width= 13)
        self.entryy1str.grid(row= 1, column= 1, padx= 10, pady= 10, sticky='w')
        self.labely2str = tk.Label(self.group3, text= 'Ytop: ').grid(row= 1, column= 2, padx= 5, pady= 10, sticky='w')
        self.entryy2str = tk.Entry(self.group3, textvariable= self.y2str, justify= 'center', width= 13)
        self.entryy2str.grid(row= 1, column= 3, padx= 10, pady= 10, sticky='w')
        
        self.labelstrata = tk.Label(self.group3, text= 'Strata: ', width= 17).place(relx= 0.02, rely= 0.74, relheight= 0.13, relwidth= 0.08)
        self.entrystrata = tk.Entry(self.group3, textvariable= self.strata, justify= 'center', width= 8)
        self.entrystrata.place(relx= 0.115, rely= 0.73, relheight= 0.17, relwidth= 0.11)
        
        self.labelnstr = tk.Label(self.group3, text= 'Number of points: ', width= 17).place(relx= 0.265, rely= 0.74, relheight= 0.13, relwidth= 0.21)
        self.entrynstr = tk.Entry(self.group3, textvariable= self.nstr, justify= 'center', width= 8)
        self.entrynstr.place(relx= 0.5, rely= 0.73, relheight= 0.17, relwidth= 0.14)
        
        self.calcSTR = tk.Button(self.group3, text= '📝 Calculate', activebackground= '#d9d9d9', command= lambda:self.stratifiedSamplingCoordsCalc())
        self.calcSTR.place(relx= 0.8, rely= 0.73, relheight= 0.23, relwidth= 0.18)
        
        self.buttonshowSTR = tk.Button(self.group3, text= '🔍 Show', state= 'disabled', activebackground= '#d9d9d9', command= lambda:self.showSTR())
        self.buttonshowSTR.place(relx= 0.8, rely= 0.45, relheight= 0.23, relwidth= 0.18)
        
        self.statusSTR = tk.Label(self.group3, textvariable= self.statusstr).place(relx= 0.79, rely= 0.08, relheight= 0.13, relwidth= 0.2)
        self.expstatusSTR = tk.Label(self.group3, textvariable= self.expstr).place(relx= 0.79, rely= 0.27, relheight= 0.13, relwidth= 0.2)
        
#---------------------------------- O T H E R S ------------------------------#  

        self.buttonCompare = tk.Button(self.frame, state= 'disabled', activebackground= '#d9d9d9', text= '🔬 Compare', command= lambda:self.subplotsSampling())
        self.buttonCompare.place(relx= 0.03, rely= 0.89, relheight= 0.07, relwidth= 0.16)
        
        self.buttonStatistics = tk.Button(self.frame, state= 'disabled', activebackground= '#d9d9d9', text= '📊 Statistics', command= lambda:self.Statistics())
        self.buttonStatistics.place(relx= 0.225, rely= 0.89, relheight= 0.07, relwidth= 0.16)
        
        self.buttonHelp = tk.Button(self.frame, activebackground= '#d9d9d9', text= '💡 Help', command= lambda:self.openHelp())
        self.buttonHelp.place(relx= 0.42, rely= 0.89, relheight= 0.07, relwidth= 0.16)
        
        self.buttonReset = tk.Button(self.frame, state= 'disabled', activebackground= '#d9d9d9', text= '🔄 Reset', command= lambda:self.Reset())
        self.buttonReset.place(relx= 0.615, rely= 0.89, relheight= 0.07, relwidth= 0.16)
        
        self.buttonExit = tk.Button(self.frame, activebackground= '#d9d9d9', text= '🚪 Exit', command= lambda:self.exitApp())
        self.buttonExit.place(relx= 0.81, rely= 0.89, relheight= 0.07, relwidth= 0.16)
                
#-----------------------------------------------------------------------------#
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
#----------------------- F U N C T I O N   S E C T I O N ---------------------#
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
#------------------ C O N F I G U R I N G   T H E   G R I D ------------------#
#-----------------------------------------------------------------------------#
    def setGrid(self):
        self.fig = plt.figure(figsize=(10,6))
        ax = self.fig.add_subplot(1, 1, 1)
    
        major_ticks = np.arange(0, self.maximum, self.majorSpace)
        minor_ticks = np.arange(0, self.maximum, self.minorSpace)
        
        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)
     
        ax.grid(which='both')
    
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)

#-----------------------------------------------------------------------------#   
#---------------------- R A N D O M   S A M P L I N G ------------------------#  
#-----------------------------------------------------------------------------#                   
    def randomSamplingCoordsCalc(self):
        x1r = self.x1r.get()
        x2r = self.x2r.get()
        y1r = self.y1r.get()
        y2r = self.y2r.get()
        nr = self.nr.get()
        XS = [x1r, x2r]
        YS= [y1r, y2r]
        
        if x1r != x2r and y1r != y2r and nr != 0: 
            self.press1 = True
            self.buttonID = 1
            self.buttonReset.config(state= 'normal')
            
            self.maximum = max(x2r, y2r) + int(0.1 * max(x2r, y2r))
            self.majorSpace = int(0.1 * max(x2r, y2r))
            self.minorSpace = int (self.majorSpace / 2)
                  
            self.xRS = np.random.randint(x1r, x2r + 1, nr)
            self.yRS = np.random.randint(y1r, y2r + 1, nr)  
            
            xseries = pd.Series(self.xRS)
            yseries = pd.Series(self.yRS)
            self.meanxRS = round(xseries.mean(), 3)
            self.meanyRS = round(yseries.mean(), 3)      
            self.variancexRS = round(xseries.var(ddof=1), 5)
            self.varianceyRS = round(yseries.var(ddof=1), 5)
            self.stdevxRS = round(xseries.std(ddof=1), 5)
            self.stdevyRS = round(yseries.std(ddof=1), 5)
            self.skewxRS = round(xseries.skew(), 5)
            self.skewyRS = round(yseries.skew(), 5)
            self.covxyRS = round(xseries.cov(yseries) , 5)
            self.covyxRS = round(yseries.cov(xseries) , 5)
            self.corrxyRS = round(xseries.corr(yseries) , 5)
            self.corryxRS = round(yseries.corr(xseries) , 5)
            
            self.aaRS = np.arange(1, len(self.xRS) + 1)
            self.coordsRS = list(zip(self.aaRS, self.xRS, self.yRS))   
            
            tk.messagebox.showinfo('Info:', 'Random Sampling data was calculated successfully!')
            self.statusr.set(value= '✔ Calculated!')
            self.buttonshowRS.config(state= 'normal')
            
            self.exportfileRS()
            
            self.setGrid()
            plt.axis('auto')
            for l in range(len(XS)):
                plt.axvline(x= XS[l], ls='-.')
                plt.axhline(y= YS[l], ls='-.')
                
            plt.scatter(self.xRS, self.yRS, c= 'b')
            plt.title("Random Sampling",fontsize=20)
            plt.xlabel("X - coordinates",fontsize=14)
            plt.ylabel("Y - coordinates",fontsize=14)
            plt.tick_params(axis="both",labelsize=10)
            plt.show() 
            
            if self.press1 == True and self.press2 == True and self.press3 == True:
                self.buttonCompare.config(state= 'normal')
                self.buttonStatistics.config(state= 'normal')
            return(self.coordsRS)
        else:
            tk.messagebox.showwarning('Warning:', "Please insert valid data or click '💡 Help'.")
    
#-----------------------------------------------------------------------------# 
#-------------------- S Y S T E M A T I C   S A M P L I N G ------------------#
#-----------------------------------------------------------------------------# 
    def systematicSamplingCoordsCalc(self):
        x1s = self.x1s.get()
        x2s = self.x2s.get()
        y1s = self.y1s.get()
        y2s = self.y2s.get()
        ns = self.ns.get()
        
        XS = [x1s, x2s]
        YS = [y1s, y2s]
        
        if x1s != x2s and y1s != y2s and ns != 0: 
            self.press2 = True
            self.buttonID = 2
            self.buttonReset.config(state= 'normal')
            
            self.maximum = max(x2s, y2s) + int(0.1 * max(x2s, y2s))
            self.majorSpace = int(0.1 * max(x2s, y2s))
            self.minorSpace = int (self.majorSpace / 2)
            
            self.xSS = np.arange(x1s, x2s + 1, ns)
            self.ySS = np.arange(y1s, y2s + 1, ns)
          
            self.XIss = []
            self.YIss = []
            
            #self.XIss, self.YIss = np.meshgrid(self.xSS, self.ySS)
            for i in range(len(self.xSS)):
                for j in range(len(self.ySS)):
                    self.XIss.append(self.xSS[i])
                    self.YIss.append(self.ySS[j])
                    
            xseries = pd.Series(self.XIss)
            yseries = pd.Series(self.YIss)
            self.meanxSS = round(xseries.mean(), 3)
            self.meanySS = round(yseries.mean(), 3)      
            self.variancexSS = round(xseries.var(ddof=1), 5)
            self.varianceySS = round(yseries.var(ddof=1), 5)
            self.stdevxSS = round(xseries.std(ddof=1), 5)
            self.stdevySS = round(yseries.std(ddof=1), 5)
            self.skewxSS = round(xseries.skew(), 5)
            self.skewySS = round(yseries.skew(), 5)
            self.covxySS = round(xseries.cov(yseries) , 5)
            self.covyxSS = round(yseries.cov(xseries) , 5)
            self.corrxySS = round(xseries.corr(yseries) , 5)
            self.corryxSS = round(yseries.corr(xseries) , 5)
                    
            self.aaSS = np.arange(1, len(self.XIss) + 1)
            self.coordsSS = list(zip(self.aaSS, self.XIss, self.YIss))
            
            tk.messagebox.showinfo('Info:', 'Systematic Sampling data was calculated successfully!')
            self.statuss.set(value= '✔ Calculated!')
            self.buttonshowSS.config(state= 'normal')
            
            self.exportfileSS()
            
            self.setGrid()
            plt.axis('auto')
            for l in range(len(XS)):
                plt.axvline(x= XS[l], ls='-.')
                plt.axhline(y= YS[l], ls='-.')
                
            plt.scatter(self.XIss, self.YIss, c='r')
            plt.title("Systematic Sampling",fontsize=20)
            plt.xlabel("X - coordinates",fontsize=14)
            plt.ylabel("Y - coordinates",fontsize=14)
            plt.tick_params(axis="both",labelsize=10)
            plt.show()
            
            if self.press1 == True and self.press2 == True and self.press3 == True:
                self.buttonCompare.config(state= 'normal')
                self.buttonStatistics.config(state= 'normal')
            return(self.coordsSS)   
        else:
            tk.messagebox.showwarning('Warning:', "Please insert valid data or click '💡 Help'.")
    
#-----------------------------------------------------------------------------#   
#--------------------- S T R A T I F I E D   S A M P L I N G -----------------# 
#-----------------------------------------------------------------------------# 
    def stratifiedSamplingCoordsCalc(self):
        x1str = self.x1str.get()
        x2str = self.x2str.get()
        y1str = self.y1str.get()
        y2str = self.y2str.get()
        nstr = self.nstr.get()
        strata = self.strata.get()
        
        XS0 = [x1str, x2str]
        YS0 = [y1str, y2str]
        
        if x1str != x2str and y1str != y2str and nstr != 0 and strata != 0: 
            self.press3 = True
            self.buttonID = 3
            self.buttonReset.config(state= 'normal')
            
            self.maximum = max(x2str, y2str) + int(0.1 * max(x2str, y2str))
            self.majorSpace = int(0.1 * max(x2str, y2str))
            self.minorSpace = int (self.majorSpace / 2)
     
            self.st = int(np.sqrt(strata))
            self.x1 = np.arange(x1str, x2str + 1)
            self.y1 = np.arange(y1str, y2str + 1)
            self.dx = int((len(self.x1)-1) / self.st)
            self.dy = int((len(self.y1)-1) / self.st)
            
            self.klaseisx = []
            self.klaseisy = []
            tx = 0
            ty = 0
            self.stratax = []
            self.stratay = []
            for l in range(self.st):
                kx = [tx for tx in range(tx, self.dx + tx)]
                ky = [ty for ty in range(ty, self.dy + ty)]
                self.klaseisx.append(kx)
                self.klaseisy.append(ky)
                tx += self.dx
                ty += self.dy
                self.stratax.append(tx)
                self.stratay.append(ty)
            
            self.Xs = []
            self.Ys = []
            for i in range(self.st):
                for j in range(self.st):
                    xi = list(np.random.randint(self.klaseisx[i][0], self.klaseisx[i][-1] + 1, nstr))
                    yi = list(np.random.randint(self.klaseisy[j][0], self.klaseisy[j][-1] + 1, nstr))
                    self.Xs += xi
                    self.Ys += yi
                    
            xseries = pd.Series(self.Xs)
            yseries = pd.Series(self.Ys)
            self.meanxSTR = round(xseries.mean(), 3)
            self.meanySTR = round(yseries.mean(), 3)      
            self.variancexSTR = round(xseries.var(ddof=1), 5)
            self.varianceySTR = round(yseries.var(ddof=1), 5)
            self.stdevxSTR = round(xseries.std(ddof=1), 5)
            self.stdevySTR = round(yseries.std(ddof=1), 5)
            self.skewxSTR = round(xseries.skew(), 5)
            self.skewySTR = round(yseries.skew(), 5)
            self.covxySTR = round(xseries.cov(yseries) , 5)
            self.covyxSTR = round(yseries.cov(xseries) , 5)
            self.corrxySTR = round(xseries.corr(yseries) , 5)
            self.corryxSTR = round(yseries.corr(xseries) , 5)
        
            self.aaSTR = np.arange(1, len(self.Xs) + 1)
            self.coordsSTR = list(zip(self.aaSTR, self.Xs, self.Ys))
            
            tk.messagebox.showinfo('Info:', 'Stratified Random Sampling data was calculated successfully!')
            self.statusstr.set(value= '✔ Calculated!')
            self.buttonshowSTR.config(state= 'normal')
            
            self.exportfileSTR()
            
            self.setGrid()
            
            for l in range(len(self.stratax)):
                plt.axvline(x= self.stratax[l], ls='-.')
                plt.axhline(y= self.stratay[l], ls='-.')
            
            for l in range(len(XS0)):
                plt.axvline(x= XS0[l], ls='-.')
                plt.axhline(y= YS0[l], ls='-.')
            
            plt.axis('auto')
            plt.scatter(self.Xs, self.Ys, c= 'g')
            plt.title("Stratified Random Sampling",fontsize=20)
            plt.xlabel("X - coordinates",fontsize=14)
            plt.ylabel("Y - coordinates",fontsize=14)
            plt.tick_params(axis="both",labelsize=10)
            plt.show()
            
            if self.press1 == True and self.press2 == True and self.press3 == True:
                self.buttonCompare.config(state= 'normal')
                self.buttonStatistics.config(state= 'normal')
            return(self.coordsSTR)
        else:
            tk.messagebox.showwarning('Warning:', "Please insert valid data or click '💡 Help'.")
#-----------------------------------------------------------------------------#
#------------------- S U B P L O T   A L L   M E T H O D S -------------------#
#-----------------------------------------------------------------------------# 
    def subplotsSampling(self):  
        file_name = tk.filedialog.asksaveasfilename()
        if file_name:
            with open(f'{file_name}.txt', 'w') as file:
                file.write(self.textRS)
                file.write(self.textSS)
                file.write(self.textSTR)
        
            tk.messagebox.showinfo('Info:', 'All Sampling data was saved successfully!')
        
            open_file = file_name + '.txt'
            #os.system('" %s "' % open_file) Open file on Windows
            os.system('xdg-open "%s"' % open_file) # Open file on Linux
        
        f = plt.figure(figsize=(20,6))
        ax = f.add_subplot(131)
        ax2 = f.add_subplot(132)
        ax3 = f.add_subplot(133)
        
        XSr = [self.x1r.get(), self.x2r.get()]
        YSr = [self.y1r.get(), self.y2r.get()]
        for l in range(len(XSr)):
            ax.axvline(x= XSr[l], ls='-.')
            ax.axhline(y= YSr[l], ls='-.')
        ax.scatter(self.xRS, self.yRS, c= 'b')
        ax.grid()
        ax.set_title('Random Sampling',fontsize=15)
        ax.set_xlabel("X - coordinates",fontsize=13)
        ax.set_ylabel("Y - coordinates",fontsize=13)
                    
        XSs = [self.x1s.get(), self.x2s.get()]
        YSs = [self.y1s.get(), self.y2s.get()]
        for l in range(len(XSs)):
            ax2.axvline(x= XSs[l], ls='-.')
            ax2.axhline(y= YSs[l], ls='-.')
        ax2.scatter(self.XIss, self.YIss, c='r')
        ax2.grid()
        ax2.set_title('Systematic Sampling',fontsize=15)
        ax2.set_xlabel("X - coordinates",fontsize=13)
        ax2.set_ylabel("Y - coordinates",fontsize=13)
          
        
        XSstr = [self.x1str.get(), self.x2str.get()]
        YSstr = [self.y1str.get(), self.y2str.get()]
        for l in range(len(XSstr)):
            ax3.axvline(x= XSstr[l], ls='-.')
            ax3.axhline(y= YSstr[l], ls='-.')
        
        for l in range(len(self.stratax)):
            ax3.axvline(x= self.stratax[l], ls='-.')
            ax3.axhline(y= self.stratay[l], ls='-.')
            
        ax3.scatter(self.Xs, self.Ys, c= 'g')
        ax3.grid()
        ax3.set_title('Stratified Random Sampling',fontsize=15)
        ax3.set_xlabel("X - coordinates",fontsize=13)
        ax3.set_ylabel("Y - coordinates",fontsize=13)     
        
        f.suptitle('Comparing Sampling Methods',fontsize=18 )
        
        plt.show()
        
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#-----------------------------------------------------------------------------#
#------------- W R I T E   E A C H   M E T H O D   T O   T E X T -------------#
#-----------------------------------------------------------------------------#
    def exportfileRS(self):      
        self.tableRS = texttable.Texttable()
        self.tableRS.set_deco(texttable.Texttable.HEADER | texttable.Texttable.BORDER | texttable.Texttable.VLINES)
        self.tableRS.header(["ID", "X", "Y"])
        self.tableRS.set_cols_dtype(['i',  'f', 'f'])
        self.tableRS.set_cols_align(["c", "c", "c"])
  
        for point in self.coordsRS:   
            self.tableRS.add_row([point[0], point[1], point[2]])
             
        self.tableRS2 = texttable.Texttable()
        self.tableRS2.set_deco(texttable.Texttable.HEADER | texttable.Texttable.BORDER | texttable.Texttable.VLINES)
        self.tableRS2.set_cols_dtype(['t',  'f', 'f'])
        self.tableRS2.set_cols_align(["c", "c", "c"])
        self.tableRS2.add_rows([["MEASURE", "X", "Y"],
                        ["MEAN", self.meanxRS, self.meanyRS],
                        ["VARIANCE", self.variancexRS, self.varianceyRS],
                        ["ST. DEVIATION", self.stdevxRS, self.stdevyRS],
                        ["SKEWNESS", self.skewxRS, self.skewyRS],
                        ["COVARIANCE", self.covxyRS, self.covyxRS],
                        ["CORRELATION", self.corrxyRS, self.corryxRS]])
                
        self.titleRS1 = '\n-GENERATED COORDINATES BY RANDOM SAMPLING-\n'
        self.titleRS2 = '\n<MEASURES OF VARIABILITY AND SPREAD>\n'  

        self.textRS = self.titleRS1 + self.tableRS.draw() + self.titleRS2 + self.tableRS2.draw()
        self.statRS = self.titleRS2 + self.tableRS2.draw()
        
        self.file_nameRS = tk.filedialog.asksaveasfilename()
        if self.file_nameRS:  
            with open(f'{self.file_nameRS}.txt', 'w') as file:
                file.write(self.textRS)
        
            tk.messagebox.showinfo('Info:', 'Random Sampling data was saved successfully!')
            self.expr.set(value='✔ Exported!')
        
            self.open_fileRS = self.file_nameRS + '.txt'

#-----------------------------------------------------------------------------#
#-------------------- S H O W   R A N D O M   S A M P L I N G ----------------#
#-----------------------------------------------------------------------------#        
    def showRS(self):
        if self.file_nameRS:
            #os.system('" %s "' % self.open_fileRS) Open file on Windows
            os.system('xdg-open "%s"' % self.open_fileRS) # Open file on Linux
        else:
            tk.messagebox.showwarning('Warning:', 'You should first save the generated file.\nCalculate again.')
#-----------------------------------------------------------------------------#    
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#       
#-----------------------------------------------------------------------------#
    def exportfileSS(self):      
        self.tableSS = texttable.Texttable()
        self.tableSS.set_deco(texttable.Texttable.HEADER | texttable.Texttable.BORDER | texttable.Texttable.VLINES)
        self.tableSS.header(["ID", "X", "Y"])
        self.tableSS.set_cols_dtype(['i',  'f', 'f'])
        self.tableSS.set_cols_align(["c", "c", "c"])
  
        for point in self.coordsSS:   
            self.tableSS.add_row([point[0], point[1], point[2]])
             
        self.tableSS2 = texttable.Texttable()
        self.tableSS2.set_deco(texttable.Texttable.HEADER | texttable.Texttable.BORDER | texttable.Texttable.VLINES)
        self.tableSS2.set_cols_dtype(['t',  'f', 'f'])
        self.tableSS2.set_cols_align(["c", "c", "c"])
        self.tableSS2.add_rows([["MEASURE", "X", "Y"],
                        ["MEAN", self.meanxSS, self.meanySS],
                        ["VARIANCE", self.variancexSS, self.varianceySS],
                        ["ST. DEVIATION", self.stdevxSS, self.stdevySS],
                        ["SKEWNESS", self.skewxSS, self.skewySS],
                        ["COVARIANCE", self.covxySS, self.covyxSS],
                        ["CORRELATION", self.corrxySS, self.corryxSS]])
         
        self.titleSS1 = '\n-GENERATED COORDINATES BY SYSTEMATIC SAMPLING-\n'
        self.titleSS2 = '\n<MEASURES OF VARIABILITY AND SPREAD>\n'   

        self.textSS = self.titleSS1 + self.tableSS.draw() + self.titleSS2 + self.tableSS2.draw()
        self.statSS = self.titleSS2 + self.tableSS2.draw()      
        
        self.file_nameSS = tk.filedialog.asksaveasfilename()
        if self.file_nameSS:
            with open(f'{self.file_nameSS}.txt', 'w') as file:
                file.write(self.textSS)
            
            tk.messagebox.showinfo('Info:', 'Systematic Sampling data was saved successfully!')
            self.exps.set(value='✔ Exported!')
            
            self.open_fileSS = self.file_nameSS + '.txt'

#-----------------------------------------------------------------------------#
#---------------- S H O W   S Y S T E M A T I C  S A M P L I N G -------------# 
#-----------------------------------------------------------------------------#       
    def showSS(self):
        if self.file_nameSS:
            #os.system('" %s "' % self.open_fileSS) Open file on Windows
            os.system('xdg-open "%s"' % self.open_fileSS) # Open file on Linux
        else:
            tk.messagebox.showwarning('Warning:', 'You should first save the generated file.\nCalculate again.')
#-----------------------------------------------------------------------------#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#           
#-----------------------------------------------------------------------------#
    def exportfileSTR(self):      
        self.tableSTR = texttable.Texttable()
        self.tableSTR.set_deco(texttable.Texttable.HEADER | texttable.Texttable.BORDER | texttable.Texttable.VLINES)
        self.tableSTR.header(["ID", "X", "Y"])
        self.tableSTR.set_cols_dtype(['i',  'f', 'f'])
        self.tableSTR.set_cols_align(["c", "c", "c"])
  
        for point in self.coordsSTR:   
           self.tableSTR.add_row([point[0], point[1], point[2]])
             
        self.tableSTR2 = texttable.Texttable()
        self.tableSTR2.set_deco(texttable.Texttable.HEADER | texttable.Texttable.BORDER | texttable.Texttable.VLINES)
        self.tableSTR2.set_cols_dtype(['t',  'f', 'f'])
        self.tableSTR2.set_cols_align(["c", "c", "c"])
        self.tableSTR2.add_rows([["MEASURE", "X", "Y"],
                        ["MEAN", self.meanxSTR, self.meanySTR],
                        ["VARIANCE", self.variancexSTR, self.varianceySTR],
                        ["ST. DEVIATION", self.stdevxSTR, self.stdevySTR],
                        ["SKEWNESS", self.skewxSTR, self.skewySTR],
                        ["COVARIANCE", self.covxySTR, self.covyxSTR],
                        ["CORRELATION", self.corrxySTR, self.corryxSTR]])
         
        self.titleSTR1 = '\n-GENERATED COORDINATES BY STRATIFIED RANDOM SAMPLING-\n'
        self.titleSTR2 = '\n<MEASURES OF VARIABILITY AND SPREAD>\n'

        self.textSTR = self.titleSTR1 + self.tableSTR.draw() + self.titleSTR2 + self.tableSTR2.draw()
        self.statSTR = self.titleSTR2 + self.tableSTR2.draw()
        
        self.file_nameSTR = tk.filedialog.asksaveasfilename()
        if self.file_nameSTR:
            with open(f'{self.file_nameSTR}.txt', 'w') as file:
                file.write(self.textSTR)
            
            tk.messagebox.showinfo('Info:', 'Random Stratified Sampling data was saved successfully!')
            self.expstr.set(value='✔ Exported!')
        
            self.open_fileSTR = self.file_nameSTR + '.txt'

#-----------------------------------------------------------------------------#
#---------------- S H O W   S T R A T I F I E D  S A M P L I N G -------------#    
#-----------------------------------------------------------------------------#    
    def showSTR(self):
        if self.file_nameSTR:
            #os.system('" %s "' % self.open_fileSTR) Open file on Windows
            os.system('xdg-open "%s"' % self.open_fileSTR) # Open file on Linux
        else:
            tk.messagebox.showwarning('Warning:', 'You should first save the generated file.\nCalculate again.')
        
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
#-----------------------------------------------------------------------------#
#-------------------------- S T A T I S T I C S ------------------------------#
#-----------------------------------------------------------------------------#
    def Statistics(self):    
        self.title1STAT = '<RANDOM SAMPLING METHOD>\n'
        self.title2STAT = '\n<SYSTEMATIC SAMPLING METHOD>\n'
        self.title3STAT = '\n<STRATIFIED RANDOM SAMPLING METHOD>\n'
        self.statText = self.title1STAT + self.tableRS2.draw() + self.title2STAT + self.tableSS2.draw() + self.title3STAT + self.tableSTR2.draw()
                          
        self.file_nameSTAT = tk.filedialog.asksaveasfilename()
        if self.file_nameSTAT:
            with open(f'{self.file_nameSTAT}.txt', 'w') as file:
                file.write(self.statText)
        
            tk.messagebox.showinfo('Info:', 'Statistical data was saved successfully!')
        
            self.open_fileSTAT = self.file_nameSTAT + '.txt'
            #os.system('" %s "' % self.open_fileSTAT) Open file on Windows
            os.system('xdg-open "%s"' % self.open_fileSTAT) # Open file on Linux
        
#-----------------------------------------------------------------------------#
#------------------------- C L O S E   A P P L I C A T I O N -----------------#
#-----------------------------------------------------------------------------#
    def exitApp(self):
        self.master.destroy()
        
#-----------------------------------------------------------------------------# 
#------------------------------ R E S E T ------------------------------------#  
#-----------------------------------------------------------------------------#  
    def Reset(self):
        self.press1 = False
        self.press2 = False
        self.press3 = False
        self.buttonID = 0
        
        self.x1r.set(value= 0.0)
        self.x2r.set(value= 0.0)      
        self.y1r.set(value= 0.0)      
        self.y2r.set(value= 0.0)       
        self.nr.set(value= 0)      
          
        self.x1s.set(value= 0.0)        
        self.x2s.set(value= 0.0)           
        self.y1s.set(value= 0.0)        
        self.y2s.set(value= 0.0)       
        self.ns.set(value= 0)
        
        self.strata.set(value= 0)        
        self.x1str.set(value= 0.0)      
        self.x2str.set(value= 0.0)       
        self.y1str.set(value= 0.0)       
        self.y2str.set(value= 0.0)       
        self.nstr.set(value= 0)
               
        self.entryx1r.delete(0, tk.END)
        self.entryx2r.delete(0, tk.END)
        self.entryy1r.delete(0, tk.END)
        self.entryy2r.delete(0, tk.END)
        self.entrynr.delete(0, tk.END)
        self.entryx1s.delete(0, tk.END)
        self.entryx2s.delete(0, tk.END)
        self.entryy1s.delete(0, tk.END)
        self.entryy2s.delete(0, tk.END)
        self.entryns.delete(0, tk.END)
        self.entryx1str.delete(0, tk.END)
        self.entryx2str.delete(0, tk.END)
        self.entryy1str.delete(0, tk.END)
        self.entryy2str.delete(0, tk.END)
        self.entrynstr.delete(0, tk.END)
        self.entrystrata.delete(0, tk.END)

        self.entryx1r.insert(0, 0.0)        
        self.entryx2r.insert(0, 0.0)
        self.entryy1r.insert(0, 0.0)
        self.entryy2r.insert(0, 0.0)
        self.entrynr.insert(0, 0)
        self.entryx1s.insert(0, 0.0)
        self.entryx2s.insert(0, 0.0)
        self.entryy1s.insert(0, 0.0)
        self.entryy2s.insert(0, 0.0)
        self.entryns.insert(0, 0)
        self.entrystrata.insert(0, 0)
        self.entryx1str.insert(0, 0.0)
        self.entryx2str.insert(0, 0.0)
        self.entryy1str.insert(0, 0.0)
        self.entryy2str.insert(0, 0.0)
        self.entrynstr.insert(0, 0)
        
        self.buttonCompare.config(state= 'disabled')
        self.buttonStatistics.config(state= 'disabled')
        self.buttonReset.config(state= 'disabled')
           
        self.statusr.set(value= '')
        self.statuss.set(value= '')
        self.statusstr.set(value= '')
        self.expr.set(value= '')
        self.exps.set(value= '')
        self.expstr.set(value= '')
        self.buttonshowRS.config(state= 'disabled')
        self.buttonshowSS.config(state= 'disabled')
        self.buttonshowSTR.config(state= 'disabled')       
        
        self.maximum = 0
        self.majorSpace = 0
        self.minorSpace = 0 

#-----------------------------------------------------------------------------#
#------------------------- H E L P   W I N D O W -----------------------------#
#-----------------------------------------------------------------------------#
    def openHelp(self):
        with open("labels.txt") as f:
            readme = f.read()
            tk.messagebox.showinfo(title="Help", message = str(readme))

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
#------------------------ R O O T   T K I N T E R ----------------------------#
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
#-----------------------------------------------------------------------------#
#********************************** E N D ************************************#
#-----------------------------------------------------------------------------#