from tkinter.tix import INTEGER
from random import randint
def add(x,y):
    return  x+y  

print("Bine ati venit!")

print("Cate produse aveti?")
NrProd = int(input("Nr Produse: "))


print("1.Adaugare/Pret produse")
num1 = float(input("Produs 1: "))
num2 = float(input("Produs 2: "))
num3 = float(input("Produs 3: "))
num4 = float(input("Produs 4:"))


sum = num1 + num2 + num3 + num4
print("Suma produselor este :",sum)

print("a)1 leu")
print("b)5 lei")
print("c)10 lei")
print("d)50 lei")
print("e)100 lei")
print("f)200 lei")
print("g)500 lei")

choice = input("Alege bancnota(1/5/10/50/100/200/500/Alta suma): ")

if choice == "1":
    diff = 1-sum
    print("Rest=", diff)
if choice == "5":
    diff = 5-sum
    print("Rest=", diff)
if choice == "10":
    diff = 10-sum
    print("Rest=", diff)
if choice == "50":
    diff = 50-sum
    print("Rest=", diff)
if choice == "100":
    diff = 100-sum
    print("Rest=", diff)
if choice == "200":
    diff = 200-sum
    print("Rest=", diff)
if choice == "500":
    diff = 500-sum
    print("Rest=", diff)
if choice =="0":
    Altasuma = float(input("Alta suma: "))
    diff=Altasuma-sum
    print("Rest=", diff)