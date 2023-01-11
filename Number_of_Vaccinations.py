#We have a report on the number of flu vaccinations in a class of 20 people.

#It has the following numbers:
#never: 5
#once: 8
#twice: 4
#3 times: 3

#What is the mean number of times those people have been vaccinated?
#Output the result using the print() statement.
#Hint: Think about the data this way: it contains 20 values, each representing the number of vaccinations the corresponding person had.


vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]
print((8+8+9)/20)



#Using the same vaccinations dataset, which includes the number of times people got the flu vaccine.
#The dataset contains the following numbers:
#never: 5
#once: 8
#twice: 4
#3 times: 3

#Calculate and output the variance.
#We will soon learn about easier ways to calculate the variance and other summary statistics using Python. For now, use Python code to calculate the result using the corresponding equation.
#Hint: The variance is the average of the squared differences from the mean.


import numpy as np

a = np.array([0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3])

mean = np.sum(a)/a.size
v = np.sum ((a - mean)**2)/a.size
print(v)