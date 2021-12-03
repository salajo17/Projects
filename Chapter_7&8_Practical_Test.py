class Candy:
  def candy_input():
      candy_dict = {}
      while True:
          inp_name = input("Input your candy name (Leave it blank to quit ''): ")
          if inp_name.lower().strip() == '':
              break
          try:
              inp_price = float(input("Enter your candy price (If you don't know enter 0): "))
              if inp_price == 0:
                  inp_price = 'unknown'
              candy_dict[inp_name] = inp_price
          except ValueError:
              print("Needs to be a number")
      return candy_dict

  def candy_sort(candy_dict):
      price_dict = {}
      solution = {}
      for key, value in list(candy_dict.items()):
          if value != 'unknown':
              price_dict[key] = value
              del candy_dict[key]
      for k, v in sorted(candy_dict.items(), key=lambda x: x, reverse=False):
          solution[k] = v
      for key, value in sorted(price_dict.items(), key=lambda x: x[1], reverse=False):
        if value not in solution:
          solution[key] = value
        else:
          print(key, value)
      for key, value in sorted(price_dict.items(), key=lambda x: x, reverse=False):
          solution[key] = value
      print(f'\nThese are the candies:')
      for k, v in solution.items():
          print(f'{k.title()} = {v}')

candy = Candy.candy_input()
Candy.candy_sort(candy)
