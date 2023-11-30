import random as r
password=[]
alpha_list=[]
alpha="abcdefghijklmnopqrstuvwxyz"
num_list=["1","2","3","4","5","6","7","8","9","0"]
char_list=["!","@","&","*","#","^","$","-","_"]
for i in alpha:
    alpha_list.append(i)
char=int(input("enter the number of characters"))
a=int(input("enter the number of alphabets"))
num=int(input("enter the number of numbers"))
for i in range(char):
    password.append(r.choice(char_list))
for i in range(a):
    password.append(r.choice(alpha_list))
for i in range(num):
    password.append(r.choice((num_list)))
    r.shuffle(password)
word="".join(password)
print(f"your password is '{word}'")
