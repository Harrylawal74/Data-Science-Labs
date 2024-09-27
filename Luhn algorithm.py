//The Luhn algorithm is a simple checksum formula used to validate credit card and bank account numbers.

def luhn_algorithm(card_num):
    reverse_card_number = card_num[::-1]
    even_digts = reverse_card_number[1::2]
    even_sum = 0

    for i in range(len(even_digts)):
      numeric = int(even_digts[i])
      if numeric * 2 <= 10:
        even_sum += numeric
      else:
        even_sum += (numeric % 10) + (numeric // 10)

    if even_sum % 10 == 0:
      return (f'Credit card: {card_num} is valid.')
    else:
      return (f'Credit card: {card_num} is not valid!')



def main():
  card_num = "4799273987136272"
  print(luhn_algorithm(card_num))
  card_num = "4799273987136273"
  print(luhn_algorithm(card_num))

main()
