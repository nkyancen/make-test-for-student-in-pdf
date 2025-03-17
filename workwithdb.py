#!/usr/bin/env python3

from DBc import UseDB

path = ''

sw = 1920
sh = 1080

font_main = 'serif 14'
font_other = 'serif 11'

types = {}
pr_type = {}

## Добавляем запись в таблицу БД
def dbins(tab:str, ti:tuple, mask:str='?') -> None:
    with UseDB(path) as curs:
        curs.execute('INSERT INTO ' + tab + ' VALUES (NULL,' + mask + ')', ti)


## Удаляем запись из таблицы БД
def dbdel(tab:str, td:tuple) -> None:
    sqld = 'DELETE FROM ' + tab + ' WHERE %s_id = %s' % td

    with UseDB(path) as curs:
        curs.execute(sqld)
        

# Изменяем запись в таблице БД
def dbupd(tab:str, tu:tuple) -> None:
    sqlu = 'UPDATE ' + tab + ' SET %s = "%s" WHERE %s_id = %s' %tu

    with UseDB(path) as curs:
        curs.execute(sqlu)
        

## Выбираем записи из таблицы БД
def dbout(tab:str, to:tuple=()) -> dict:
    dic = {}

    with UseDB(path) as curs:
        if not to:
            sqlo = 'SELECT * FROM ' + tab
        else:
            sqlo = 'SELECT * FROM ' + tab +' WHERE %s' % to

        for row in curs.execute(sqlo):
            temp = []

            for i in range(1,len(row)):
                temp.append(str(row[i]))

            dic[str(row[0])] = temp

    return dic


## Возвращаем ключ по значению
def kval(dic:dict, val:list) -> str:
    val = list(val)
    temp = ''
    for item in dic:
        if val == dic[item]:
            temp = item
    return temp    

## Проверка зависимости между родительской и дочерней таблицами
def find_couple(dic_child:dict, val_par:str) -> bool:
    temp = []
    for item in dic_child.values():
        temp.append(val_par in item)

    fс = True in temp
    return fс

## Проверка наличия пункта в таблице
def find(dic:dict, val:list) -> bool:
    val = list(val)
    temp = []
    for item in dic.values():
        temp.append(val == item)

    f = True in temp
    return f

## Заменяем номер на текст
def trans(numb, n) -> str:
    numb = int(numb)
    name = str(numb)

    for item in range(n):
        if numb // 10**(item+1) == 0:
            name = '0' + name

    name = name.replace('0', 'zero')
    name = name.replace('1', 'one')
    name = name.replace('2', 'two')
    name = name.replace('3', 'three')
    name = name.replace('4', 'four')
    name = name.replace('5', 'five')
    name = name.replace('6', 'six')
    name = name.replace('7', 'seven')
    name = name.replace('8', 'eight')
    name = name.replace('9', 'nine')
    return name
