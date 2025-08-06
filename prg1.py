N1 = int(input("num1: "))
N2 = int(input("num2: "))

def pos(n1,n2):
    prod = n1*n2
    if prod <= 1000:
        return prod
    else:
        return n1+n2 
    
print(pos(N1,N2))