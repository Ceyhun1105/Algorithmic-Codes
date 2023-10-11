'''
nickname : Ceyhun11
time : 27/10/2023  3:40 AM
code name : Hamming Code
description :
    1. include data bits
    2. program makes code with using data bits and return it 
    3. you must include receive code (length must be the length of the program return code)
    4. if your receive code equal to program return code, it'll write "haven't any problem"
       if not same , program'll find error and repair it then return it 
'''

def powertwo(n):
    for i in range(0,5):
        if n==2**i:
            return True

sendcode=input("Include data_bits : ")

# lenght+1+r<=2**r
lenght=len(sendcode)+1        
for r in range(3,100):
    if lenght+r<=2**r:
        lenght=lenght+r-1
        break
mylist=[]

for i in range(0,lenght):
    mylist.append("p"+str(i+1))


for i in sendcode:
    for j in range(1,lenght+1):
        if powertwo(j)!=True and mylist[j-1]!=str(1) and mylist[j-1]!=str(0):
            mylist[j-1]=i
            break

t=1
number=0
for i in range(1,lenght+1):
    if powertwo(i)==True:
        for j in range(1,lenght+1):
            if len(bin(j))<t:
                continue
            else:
                if str(bin(j))[-t]=="1":
                    if mylist[j-1]=="1":
                        number+=1
        if number%2==1:
            mylist[i-1]="1"
        else:
            mylist[i-1]="0"
        t+=1
        number=0

code=""
for i in mylist:
    code+=i
print(code)


receive=input("Include receive code : ")
mylist2=[]
for i in receive:
   mylist2.append(i)

mylist3=[]
t=1
number=0

for i in range(1,lenght+1):
    if powertwo(i)==True:
        for j in range(1,lenght+1):
            if len(bin(j))<t:
                continue
            else:
                if str(bin(j))[-t]=="1":
                    if mylist2[j-1]=="1":
                        number+=1
        if number%2==1:
            mylist3.append("1")
        else:
            mylist3.append("0")
        t+=1
        number=0
    
error=0
for i in range(0,len(mylist3)):
    error+=int(mylist3[i])*(2**i)


codetrue=''    
if error==0:
    print("Code checking... please wait...")
    print("Succesfully... have not any problem")
else:
    print("Code checking... please wait...")
    print(receive+" >> have some problems")
    if mylist2[error-1]=="1":
        mylist2[error-1]="0"
    else:
        mylist2[error-1]="1"
    for i in mylist2:
        codetrue+=i
    print("Your codes have to be "+codetrue)
            
