def Read(numbers):
    numbers.clear()
    n = input()
    for numar in n.split():
        numbers.append(int(numar))

def DigitSum( n ):
    n=abs(n)
    s=0
    while n:
        s+=n%10
        n//=10
    return s

def PrintList(numbers):
    print (numbers)


def subList(numbers):
    lmax=0
    right=0
    l=0
    last_sum=-1
    for i in range( len(numbers)):
        x=numbers[i]
        sum=DigitSum(x)
        if sum==last_sum :
            l+=1
        else:
            l=1
            last_sum=sum
        if l>lmax:
            lmax=l
            right=i+1
    print(numbers[right-lmax : right])
        
        
def removeList(numbers):
    i=0
    while i<len(numbers):
        sum=DigitSum(numbers[i])
        if sum%2==0:
            del numbers[i]
        else:
            i+=1



def Menu(numbers):
    print("  ---Choose an option from below---")
    print("")
    print("1 . Read a list of integer numbers : ")
    print("2 . Find sublist with maximum length that has the sum of digits of all elements the same")
    print("3 . Remove from the list elements that have the sum of digits even")
    print("E . Exit")
    print("P . Print current list")
    print("")
    op = input()
    if op=='1':
        Read(numbers)
    elif op=='2':
        subList(numbers)
    elif op=='3':
        removeList(numbers)
    elif op=='E':
        exit()
    elif op=='P':
        PrintList(numbers)

numbers = []
while True:
    Menu(numbers)