
## Check EMIRP number or not??

n=int(input("Enter n value: "))
num=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if num!=rev:
    if num>1:
        for i in range(2,num//2+1):
            if num%i==0:
                print("Not EMIRP")
                break
        else:
            for j in range(2,rev//2+1):
                if rev%j==0:
                    print("Not EMIRP")
                    break
            else:
                print("EMRIP")
    else:
        print("Not EMRIP")
else:
    print("Not EMRIP")
