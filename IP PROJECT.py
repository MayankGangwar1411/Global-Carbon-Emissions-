#This is the IP project made by Mayank Gangwar , Aheek Gupta and Bhavya Sharma


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

#DataFrame used
csv1=pd.read_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv')



#FUNCTION FOR THE MAIN MENU
def menu():
    while True :
        print('1-Data Visualization')
        print('2-Data Analysis')
        print('3-Data Manipulation')
        print('4-Exit')
        a1=int(input('Enter choice'))
        if a1==1:
            d_viz()
        elif a1==2:
            d_ana()
        elif a1==3:
            d_man()
        elif a1==4:
            break


def d_viz():
    while True :
        print('1- Line Chart- Countries vs. Past Emissions(Top "n")')
        print('2- Line Chart- Countries vs. Present Emissions(Top "n")')
        print('3- Line Chart- Countries vs. Future Emissions(Top "n")')
        print('4- Bar Chart- Countries vs. Past Emissions(Top "n")')
        print('5- Bar Chart- Countries vs. Present Emissions(Top "n")')
        print('6- Bar Chart- Countries vs. Future Emissions(Top "n")')
        print('7- Exit')
        a2= int(input('Enter choice'))
        if a2==1 :
            lp1()
        elif a2==2:
            lp2()
        elif a2==3:
            lp3()
        elif a2==4:
            bg1()
        elif a2==5:
            bg2()
        elif a2==6:
            bg3()
        elif a2==7:
            break

def bg1():
    n=int(input('ENTER n '))
    a=csv1.sort_values(by=['PAST'], axis=0,ascending=False)
    graph_1=a.head(n).plot.bar(x='COUNTRIES',y='PAST')
    plt.show()

def bg2():
    n=int(input('ENTER n '))
    b=csv1.sort_values(by=['PRESENT'], axis=0,ascending=False)
    graph_2=b.head(n).plot.bar(x='COUNTRIES',y='PRESENT')
    plt.show()

def bg3():
    n=int(input('ENTER n '))
    c=csv1.sort_values(by=['FUTURE'], axis=0,ascending=False)
    graph_3=c.head(n).plot.bar(x='COUNTRIES',y='FUTURE')
    plt.show()
    
def lp1():
    n=int(input('ENTER n '))
    a=csv1.sort_values(by=['PAST'], axis=0,ascending=False)
    graph_4=a.head(n).plot(x='COUNTRIES',y='PAST')
    plt.show()

def lp2():
    n=int(input('ENTER n '))
    b=csv1.sort_values(by=['PRESENT'], axis=0,ascending=False)
    graph_5=b.head(n).plot(x='COUNTRIES',y='PRESENT')
    plt.show()

def lp3():
    n=int(input('ENTER n '))
    c=csv1.sort_values(by=['FUTURE'], axis=0,ascending=False)
    graph_6=c.head(n).plot(x='COUNTRIES',y='FUTURE')
    plt.show()


def d_ana():
    while True :
        print('1- Top Countries by Past Emissions')
        print('2-Top Countries by Present Emissions')
        print('3-Top Countries by Future Emissions')
        print('4-Bottom Countries by Past Emissions')
        print('5-Bottom Countries by Present Emissions')
        print('6-Bottom Countries by Future Emissions')
        print('7- Dataframe discription')
        print('8- Go back to main menu')
        a2=int(input('Enter choice'))
        if a2==1:
            a=csv1.sort_values(by=['PAST'], axis=0,ascending=False)
            print(a[['COUNTRIES','PAST']])
        elif a2==2:
            b=csv1.sort_values(by=['PRESENT'], axis=0,ascending=False)
            print(b[['COUNTRIES','PRESENT']])
        elif a2==3:
            c=csv1.sort_values(by=['FUTURE'], axis=0,ascending=False)
            print(c[['COUNTRIES','FUTURE']])
        elif a2==4:
            d= csv1.sort_values(by=['PAST'], axis=0 , ascending=True)
            print(d[['COUNTRIES','PAST']])
        elif a2==5:
            e= csv1.sort_values(by=['PRESENT'], axis=0 , ascending=True)
            print(e[['COUNTRIES','PRESENT']])
        elif a2==6:
            f= csv1.sort_values(by=['FUTURE'], axis=0 , ascending=True)
            print(f[['COUNTRIES','FUTURE']])
        elif a2==7:
            print(csv1.describe())
        elif a2==8:
            break
             


def d_man():
    csv1=pd.read_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv')
    while True :
        print('1- Inserting Row')
        print('2- Deleting Row')
        print('3- Inserting Column')
        print('4- Deleting Column')
        print('5- Renaming Coulmn')
        print('6- Go back to main menu')
        a3= int(input('Enter choice'))
        if a3==1:
            x=len(csv1)
            x1=str(input('Enter Country name'))
            x2=float(input('Enter Past Emissions'))
            x3=float(input('Enter Present Emissions'))
            x4=float(input('Enter Future Emissions'))
            csv1.loc[x]=[x1,x2,x3,x4]
            csv1.to_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv', index=False)
            csv1=csv1.read_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv')
            print(csv1)
        elif a3==2:
            x=int(input('enter which row axis'))
            csv1=csv1.drop(x,axis=0)
            csv1.to_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv', index=False)
            csv1=csv1.read_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv')
            print(csv1)
        elif a3==3:
            x=str(input('enter new column name'))
            csv1[x]='NaN'
            csv1.to_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv', index=False)
            csv1=csv1.read_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv')
            print(csv1)
        elif a3==4:
            x=input('Enter which column to delete')
            csv1=csv1.drop(x, axis=1)
            csv1.to_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv', index=False)
            csv1=csv1.read_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv')
            print(csv1)
        elif a3==5:
            x1=input('Enter a column which has to be renamed
                     ')
            x2=input('Enter new column name')
            csv1=csv1.rename(columns={x1:x2})
            csv1.to_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv', index=False)
            csv1=csv1.read_csv('C:/Users/MP Gangwar/Desktop/Mayank/SCHOOL/IP Class 12/Project/CSV1.csv')
            print(csv1)
        elif a3==6:
            break

menu()














        

