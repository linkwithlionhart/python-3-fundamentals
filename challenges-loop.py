# Divisible by Ten
  #Write your function here
  def divisible_by_ten(nums):
    count = 0
    for num in nums:
      if num % 10 == 0:
        count += 1
    return count

  #Uncomment the line below when your function is done
  print(divisible_by_ten([20, 25, 30, 35, 40]))

# Greetings
  #Write your function here
  def add_greetings(names):
    greetings = []
    for name in names:
      greetings.append('Hello, ' + name)
    return greetings

  #Uncomment the line below when your function is done
  print(add_greetings(["Owen", "Max", "Sophie"]))

# Delete Starting Even Numbers
  #Write your function here
  def delete_starting_evens(my_list):
    while len(my_list) and my_list[0] % 2 == 0:
      my_list.pop(0)
    return my_list

  #Uncomment the lines below when your function is done
  print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
  print(delete_starting_evens([4, 8, 10]))

# Odd Indices
  #Write your function here
  def odd_indices(my_list):
    new_indice = []
    for i in range(1, len(my_list), 2):
      new_indice.append(my_list[i])
    return new_indice

  #Uncomment the line below when your function is done
  print(odd_indices([4, 3, 7, 10, 11, -2]))

# Exponents
  #Write your function here
  def exponents(bases, powers):
    answers = []
    for base in bases:
      for power in powers:
        answers.append(base**power)
    return answers

  #Uncomment the line below when your function is done
  print(exponents([2, 3, 4], [1, 2, 3]))
 
# Larger Sum
  #Write your function here
  def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0

    for num in lst1:
      sum1 += num
    
    for num in lst2:
      sum2 += num

    if sum1 > sum2:
      return lst1
    elif sum2 > sum1:
      return lst2
    else:
      return lst1

  #Uncomment the line below when your function is done
  print(larger_sum([1, 9, 5], [2, 3, 7]))

# Over 9000
  def over_nine_thousand(lst):
    num_sum = 0
    for num in lst:
      num_sum += num
      if num_sum > 9000:
        break
    return num_sum

  #Uncomment the line below when your function is done
  print(over_nine_thousand([8000, 900, 120, 5000]))

# Max Num
  #Write your function here
  def max_num(nums):
    placeholder = nums[0]
    for i in nums:
      if i > placeholder:
        placeholder = i
    return placeholder

  #Uncomment the line below when your function is done
  print(max_num([50, -10, 0, 75, 20]))

# Same Values
  #Write your function here
  def same_values(lst1, lst2):
    matches = []
    for x in range(len(lst1)):
      if lst1[x] == lst2[x]:
        matches.append(x)
    return matches

  #Uncomment the line below when your function is done
  print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))