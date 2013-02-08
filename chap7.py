# Enter your answers for chapter 7 here
# Name: Aparna Sud 


# Ex. 7.5
import math

def estimate_pi():
    k = 0
    est = 0
    while True:
        z = ((math.factorial(4*k)*(1103+26390*k))/(math.factorial(k)**4*396**(4*k)))
        est += z

        if float(est) < 1e-15: 
            break
        print z 
        return 1/((est)* (2*math.sqrt(2))/9801)

print estimate_pi()

        

# How many iterations does it take to converge?
# until the last term is 1e-15 or 1103 iterations? not sure ... 
