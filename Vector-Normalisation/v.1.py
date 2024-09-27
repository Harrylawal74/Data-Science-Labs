//add comments

import math

def calculate_length(a_list):
    square_sum = 0
    nums = 0
    while nums < len(a_list):
      square_sum += (a_list[nums-1]**2)
      nums +=1

    length = math.sqrt(square_sum)
    return length


    length = math.sqrt(square_sum)
    return length


def normalise(a_list):
    square_sum = 0
    nums = 0
    new_list = 0
    while nums < len(a_list):
      square_sum += (a_list[nums-1]/calculate_length(a_list))
      nums +=1
    new_list += square_sum
    return new_list



a_list = [1, 132, 2]
#new_list = normalise(a_list)
#print(new_list)
#print(calculate_length(new_list))
# this should print 1, or at least something very close to 1
test = normalise(a_list)
print(f'Vector length:  {calculate_length(a_list)}')
print(f'Normalisation is:  {normalise(a_list)}')
