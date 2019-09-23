from scipy.integrate import quad
from matplotlib import pyplot


def calculate_midpoint_x_values(partitions, start, end):
    """
    Calculates the x values for the midpoint and trapezoidal sums
    :param partitions: The number of partitions of the function
    :param start: The starting value of the integral
    :param end: The end value of the integral
    :return: a list of the x values of the midpoint sum
    """
    midpointx=[]
    for i in range(partitions):
        midpointx.append((end-start)/(2*partitions)+((end-start)/partitions)*i)
    return midpointx

def calculate_trapezoid_x_values(partitions, start, end):
    """
       Calculates the x values for the midpoint and trapezoidal sums
       :param partitions: The number of partitions of the function
       :param start: The starting value of the integral
       :param end: The end value of the integral
       :return: a list of the x values of the trapezoidal sum
       """
    trapazoidx=[]
    for i in range(2*partitions):
        trapazoidx.append(((end-start)/(2*partitions))*i)
    trapazoidx.append(end)
    return trapazoidx

def calculate_y_values(power, xvalues):
    """
    Calculates the y values of the function
    :param power: The power x is being raised to
    :param lst: the list of x values
    :return: a list of y values of the function
    """
    values=[]
    for x in xvalues:
        values.append(x**power)
    return values

def midpoint_sum(yvalues, partition):
    """
    Calculates the midpoint approximation of the function
    :param yvalues: A list of the midpoint y values
    :param partition: the lenght of the partitions used
    :return: the midpoint approximation of the function
    """
    tally=sum(yvalues)
    return tally*partition

def trapazoid_sum(yvalues, partition, start, end):
    """
    Calculates the trapezoidal approximation of the function
    :param yvalues: List of the y values
    :param partition: the lenght of the partitions in the approximation
    :param start: the start value of the integral
    :param end: the end value of the integral
    :return: the trapezoidal approximation
    """
    end_index=len(yvalues) - 1
    tally=sum(yvalues[1:end_index])
    tally=(tally*2)+yvalues[end_index]
    return tally*((end-start)/(partition*2))

def integral(start, end, power):
    """
    Calculates the integral of the function
    :param start: the start value of the integral
    :param end: the end vale of the integral
    :param power:
    :return: the value of the integral from start to end
    """
    xprime=lambda x: x**power
    answer, error=quad(xprime, start, end)
    return answer

def ratio(midpoint, trapezoid, actual):
    """
    Calculates the ratio of midpoint to trapezoid approximation to get the actual value of the integral
    :param midpoint: the midpoint approximation
    :param trapezoid: the trapezoidal approximation
    :param actual: the actual integral value
    :return: the ratios of the midpoint and trapezoidal sums needed to get the actual integral value
    """
    midpoint_error=actual-midpoint
    trapezoid_error=trapezoid-midpoint
    MvT_ratio=midpoint_error/trapezoid_error
    return MvT_ratio, 1-MvT_ratio

def make_graph(xaxis, yaxis):
    """
    Creates a graph of the data
    :param xaxis: The values for the x axis
    :param yaxis: The values for the y axis
    :return: NULL
    """
    pyplot.plot(xaxis, yaxis)
    pyplot.title('Extended Graph')
    pyplot.ylabel('Amplitude')
    pyplot.xlabel('Power of X')
    pyplot.savefig("CalcGraph1.png")

def main():
    """
    Takes in user input for thr valus and loops over all the specified functions then graphs the data
    :return: NULL
    """
    partitions=int(input("Enter the number of partitions: "))
    start=int(input("Enter the start value of the integral: "))
    end=int(input("Enter the end value of the integral: "))
    power=int(input("Enter the power of x to calculate to: "))

    power_x_axis=[]
    Midpoint_ratio_y_axis=[]
    midpointXs=calculate_midpoint_x_values(partitions, start, end)
    trapezoidXs=calculate_trapezoid_x_values(partitions, start, end)

    for exponent in range(2,power+1):
        print("power: x^", power,sep="")
        midpointYs=calculate_y_values(power, midpointXs)
        trapezoidYs=calculate_y_values(power, trapezoidXs)
        print("midpont Xs:", midpointXs,"\n", "midpoint Ys:", midpointYs,"\n",
              "trapezoid Xs:", trapezoidXs,"\n", "trpezoid Ys:", trapezoidYs)
        midpoint_appox=midpoint_sum(midpointYs, (end - start) / partitions)
        trapezoid_approx=trapazoid_sum(trapezoidYs, 2 * partitions, start, end)
        print("midpoint approximation:", midpoint_appox,"\n",
              "Trapezoid approximation:", trapezoid_approx)
        actual=integral(start, end, power)
        print("actual: ", actual)
        trapezoid_ratio, midpoint_ratio=ratio(midpoint_appox, trapezoid_approx, actual)
        power_x_axis.append(power)
        Midpoint_ratio_y_axis.append(midpoint_ratio)
        print(actual,"=", midpoint_ratio, "Midpoint", "+", trapezoid_ratio, "Trapezoid")

    make_graph(power_x_axis, Midpoint_ratio_y_axis)

if __name__ == '__main__':
    main()


