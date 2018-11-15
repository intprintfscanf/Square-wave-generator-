import matplotlib.pyplot as plt
import numpy as np
#Welcome notation
print("WELCOME TO SQUARE WAVE GENERATOR\n ")
print("  ________           _________")
print(" |        |         |         |")
print(" |        |         |         |")
print(" |        |         |         |")
print("_|        |_________|         |__\n")
print("By AIdoo Stephen Theophilus")

#Number of harmonics calculation
num = int(input('Enter Number of harmonics:\n'))
#Xaxis notation  line
xaxis=np.linspace(0,np.pi*2,100)
#Tharm, variable for total harmonics storage. harm for harmonics varible storage odd is for odd number generation
Tharm = 0.00
#while loop
harm = 0.00
oddharm = 0.00
odd = 3
count = 1
while count < num:

	oddharm =  ((1/odd)*(np.sin(odd*(xaxis))))
	harm+= oddharm
	odd+=2
	count+=1
	if count > num:
		break
Tharm = 0.00
Tharm = ((np.sin(xaxis))+harm)
yaxis=(((4*1)/np.pi)*(Tharm))
#Basic yaxis generation code below
#yaxis=(((4*1)/np.pi)*((np.sin(xaxis))+((1/3)*(np.sin(3*(xaxis))))))

plt.plot(xaxis,yaxis)
plt.ylabel('sin(x)')

plt.show()
