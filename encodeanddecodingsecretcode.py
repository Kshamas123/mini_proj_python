#secret code 
#in this program we can encode as well as decode the secret code based on certain rules

import  string,random
choice=int(input("if you want to encode enter 1 ,to decode enter 2"))
if choice==1:
    encode=input("enter the word that you want to encode")
    if len(encode)<=3:
        print(f"after encoding the word is {encode[-1:]}")
    else:
        l = list(encode)
        ch = l[0]
        l.remove(l[0])
        l.append(ch)
        for i in range(3):
            l.insert(0, random.choice(string.ascii_letters))
        for i in range(3):
            l.append(random.choice(string.ascii_letters))
        encode = "".join(l)
        print(f"after encoding the word is {encode}")
elif choice==2:
    decode=input("enter the word that we need to decode")
    if len(decode)<=3:
        print(f"word after decoding is {decode[-1:]}")
    else:
        l=list(decode)
        for i in range(3):
            l.remove(l[0])
        l=l[0:len(l)-3]
        ch=l[-1]
        l.remove(l[-1])
        l.insert(0,ch)
        print(l)
        decode="".join(l)
        print(f"word after decoding is {decode}")
else:
    print("invalid choice")


