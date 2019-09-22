from scipy.integrate import quad
from matplotlib import pyplot
x=[]
y=[]
def values(partitions, start, end):
    midpoint=[]
    trapazoid=[]
    for x in range(partitions):
        midpoint.append(((end-start)/(2*partitions))+(.125*x))
    for x in range(2*partitions):
        trapazoid.append(((end-start)/(2*partitions))*x)
    trapazoid.append(end)
    return midpoint, trapazoid
def fx(power, lst):
    values=[]
    for x in lst:
        values.append(x**power)
    return values
def midpoint(lst, partition):
    tally=sum(lst)
    return tally*partition
def trapazoid(lst, partion, s, e):
    end=len(lst)-1
    tally=sum(lst[1:end])
    tally=(tally*2)+lst[end]
    return tally*((e-s)/(partion*2))
def inter(start, end, power):
    xp= lambda x: x**power  # x**power
    ans, err=quad(xp, start, end)
    return ans
def ratio(M, T, act):
    y=act-M
    r=T-M
    x=y/r
    return x, 1-x
def main(power):
    print("power: x^",power,sep="")
    partitions=8
    start=0
    end=1
    mid, trap=values(partitions, start, end)
    midval=fx(power, mid)
    trapval=fx(power, trap)
    print("midponts: ", mid,"\n", "midpoint ys: ", midval,"\n", "trapezoid points:", trap,"\n", "trpezoid ys: ", trapval, sep="")
    A=midpoint(midval, (end-start)/partitions)
    B=trapazoid(trapval, 2*partitions,start, end)
    print("midpoint: ", A,"\n", "Trapezoid: ", B, sep="")
    act=inter(start, end, power)
    print("actual: ", act)
    trat, mrat=ratio(A, B, act)
    x.append(power)
    y.append(mrat)
    print(act," = ", mrat," Midpoint ", "+ ", trat, " Trapezoid", sep="")
for i in range(2, 500): # 4 512 8
    main(i)
print(x, "\n", y)

pyplot.plot(x,y)
pyplot.title('Extended Graph')
pyplot.ylabel('Amplitude')
pyplot.xlabel('Power of X')
pyplot.savefig("CalcGraph1.png")