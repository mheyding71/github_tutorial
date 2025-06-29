print("Hello, world!")

def median(input):
  n = len(my_list)
  mid = n // 2
  if n % 2 == 0:
      return (my_list[mid - 1] + my_list[mid]) / 2
  else:
      return my_list[mid]

my_list = [0, 1, 2, 3, 4, 5]
print(median(my_list))