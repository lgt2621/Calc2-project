from scipy.integrate import quad
from matplotlib import pyplot

power_x_axis=[]
Midpoint_ratio_y_axis=[]

def values(partitions, start, end):
    """
    Calculates the x values for the midpoint and trapezoidal sums
    :param partitions: The number of partitions of the function
    :param start: The starting value of the integral
    :param end: The end value of the integral
    :return: midpointx- the x values of the midpoint sum and trapezoidx- the x values of the trapezoidal sum
    """
    midpointx=[]
    trapazoidx=[]
    for x in range(partitions):
        midpointx.append((end-start)/(2*partitions)+((end-start)/partitions)*x)
    for x in range(2*partitions):
        trapazoidx.append(((end-start)/(2*partitions))*x)
    trapazoidx.append(end)
    return midpointx, trapazoidx

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
    end=4
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
    power_x_axis.append(power)
    Midpoint_ratio_y_axis.append(mrat)
    print(act," = ", mrat," Midpoint ", "+ ", trat, " Trapezoid", sep="")
for i in range(2, 3):
    main(i)
print(power_x_axis, "\n", Midpoint_ratio_y_axis)

pyplot.plot(power_x_axis, Midpoint_ratio_y_axis)
pyplot.title('Extended Graph')
pyplot.ylabel('Amplitude')
pyplot.xlabel('Power of X')
pyplot.savefig("CalcGraph1.png")