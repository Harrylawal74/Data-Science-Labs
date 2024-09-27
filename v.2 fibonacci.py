def fibonacci2(num):
  an_0 = 0
  an_1 = 1
  an = 0
  while num-2 > 0:
    an = an_0 + an_1
    an_0 = an_1
    an_1 = an
    num -= 1
  return an


num = 20
print(fibonacci2(num))
