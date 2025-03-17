#!/usr/bin/env python3

from tkinter import *
import tkinter.filedialog as fd
import gui_wid as gw
import workwithdb as ww
import maketest as mt

## ww.font_main = 'serif 14'
## ww.font_other = 'serif 10'

main = Tk()
main.title('Создание тестовых заданий')

ww.sw = main.winfo_screenwidth()
ww.sh = main.winfo_screenheight()

main.geometry( '+%d+%d' % (ww.sw/2 - 175 , 100))
main.resizable(0,0)

ww.path = fd.askopenfilename(filetypes = [('DataBase', '.db'),('all files', '*')])

if not ww.path:
    exit()
##    ww.path = 'TestVop.db'

ww.types = ww.dbout('typeproblem')
for item in ww.types:
    ww.pr_type[item] = (ww.types[item][1])
    
main_label = Label(main, text = 'База подключена\n' + ww.path, font = ww.font_other)

main_dis = Button(main, text = 'Дисциплины', width=10, height=2, font = ww.font_main, \
                  command = lambda: gw.win_dis(main))
main_razd = Button(main, text = 'Разделы\nи задания', width=10, height=2, font = ww.font_main, \
                  command = lambda: gw.win_razd(main))
## main_prob = Button(main, text = 'Задания', width=10,height=2, font = ww.font_main)
main_test = Button(main, text = 'Тесты', height=2, font = ww.font_main,\
                   command = lambda: mt.dis_choise(main))

main_label.grid(row = 1, column = 1, columnspan = 2, pady = 20, padx = (10,10), sticky = 'ew')
main_dis.grid(row = 2, column = 1, pady = 20, padx = 10, sticky = 'w')
main_razd.grid(row = 2, column = 2, padx = 10, sticky = 'e')
##main_prob.grid(row = 2, column = 3, padx = 10)
main_test.grid(row = 4, column = 1, columnspan = 2, padx = (10,10), pady = 10, sticky = 'ew')

main.mainloop()
