def add_fizzbuzz(num):
  print(f"We are playing FizzBuzz up to {num}")
  a_list = []


  for i in range(1, num):
    if i%3 == 0 and i%5 == 0:
      a_list.append("FizzBuzz")
    elif i%3 == 0:
      a_list.append("Fizz")
    elif i%5 == 0:
      a_list.append("Buzz")
    else:
      a_list.append(i)
  

  sum = 0
  for i in range(len(a_list)):
    if type(a_list[i]) == int:
      sum += a_list[i]


  return sum


num = 50
print(add_fizzbuzz(num))
