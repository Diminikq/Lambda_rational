import math
def lamb(n):
    rn=0
    while (n>0):
        rem=n % 10
        rn=rn*10+rem
        n=n//10
    return rn
def wholenum(num1,num2):
    return (num1-num1%num2)//num2

def concatonate_lambd(list):
    num = ""
    for i in range(len(list)):
        num+=str(list[len(list)-1-i])
    output = int(num)
    return output

def unit_digits(num1,num2):
    digits = []
    remainders = []
    nonperiod = []
    output = []
    cut = 0
    factor = 0
    factor2 = 0
    while num1 not in remainders:
        if num1<num2:
            remainders+=[num1]
            num1*=10
            if num1<num2:
                digits += [0]
            else:
                digits += [num1//num2]
        num1=num1%num2
    while num1!=remainders[cut]:
        cut+=1
    if cut==0:
        nonperiod += [0]
    else:
        nonperiod = digits[:cut]
        factor = len(nonperiod)
    factor2 = len(digits[cut:])
    output += [concatonate_lambd(nonperiod)]
    output += [concatonate_lambd(digits[cut:])]
    output += [factor,factor2]
    return output

def checksign(num):
    if num==abs(num):
        sign=1
    else:
        sign=-1
    return sign

def simplify(numer, denom):
    grcode = math.gcd(numer,denom)
    if checksign(numer)+checksign(denom)==-2:
        output = [-numer // grcode, -denom // grcode]
    elif checksign(denom)==-1:
        output = [-numer//grcode,-denom//grcode]
    else:
        output = [numer // grcode, denom // grcode]
    return output

def lambdafrac(decimal,period,whole,sign,factor, factor2):
    whole = lamb(whole)
    period_length=factor2
    period *= 10**factor
    periodpart = simplify(period,(1-10**(period_length)))
    wholepart = simplify(whole,10**(len(str(whole))))
    denominator = wholepart[1]*periodpart[1]//math.gcd(wholepart[1],periodpart[1])
    numerator = denominator//wholepart[1]*wholepart[0]+denominator//periodpart[1]*periodpart[0]+denominator*decimal
    output = simplify(numerator*sign,denominator)
    return output

def splitfrac(numer, denom):
    composite = wholenum(numer,denom)
    numer -= composite*denom
    output = [numer,denom]
    return output

def lambda_frac(numerdenom):
    zlomok = numerdenom
    znamienko = 1
    if checksign(zlomok[0])==-1:
        zlomok[0]=-zlomok[0]
        znamienko=-1
    cele = wholenum(zlomok[0],zlomok[1])
    zvysok = splitfrac(zlomok[0],zlomok[1])
    unita = unit_digits(zvysok[0],zvysok[1])
    vysledok = lambdafrac(unita[0],unita[1],cele,znamienko,unita[2],unita[3])
    return vysledok
n = 1
# for denom in range(50):
#     if lambda_frac(lambda_frac([1,n]))!=[1,n]:
#         print(n)
#     n+=1
print(lambda_frac([-69,91]))
# lambda 23/3 je 1/30, ale lambda 1/30 je -1/3. Koľko riešení je pre lambda(x)=1/n?