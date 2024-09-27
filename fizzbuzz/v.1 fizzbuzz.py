def fizzbuzz(num):
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
  return a_list

def main():
  num = 50
  print(fizzbuzz(num))
