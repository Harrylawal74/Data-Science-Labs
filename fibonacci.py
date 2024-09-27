def fibonacci(num):
  an_0 = 1
  an_1 = 1
  an = 0
  fib_list = []
  fib_list.append(0)
  fib_list.append(an_0)
  fib_list.append(an_1)
  
  while num-3 > 0:
    an = an_0 + an_1
    an_0 = an_1
    an_1 = an
    fib_list.append(an)
    num -= 1
  print(len(fib_list))
  
  return fib_list

num = 20
print(fibonacci(num))
