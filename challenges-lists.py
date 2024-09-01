# Append Size
  # Write your function here
  def append_size(my_list):
    my_list.append(len(my_list))
    return my_list

  # Uncomment the line below when your function is done
  print(append_size([23, 42, 108]))

# Append Sum
  # Write your function here
  def append_sum(my_list):
    count = 3
    while count > 0:
      append_this = my_list[-1] + my_list[-2]
      my_list.append(append_this)
      count -= 1
    return my_list

  # Uncomment the line below when your function is done
  print(append_sum([1, 1, 2]))

# Larger Lists
  # Write your function here
  def larger_list(my_list1, my_list2):
    length1 = len(my_list1)
    length2 = len(my_list2)

    if length1 > length2:
      return my_list1[-1]
    elif length2 > length1:
      return my_list2[-1]
    else:
      return my_list1[-1]

  # Uncomment the line below when your function is done
  print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

  # Refactor
  def larger_list(my_list1, my_list2):
    length1 = len(my_list1)
    length2 = len(my_list2)

    if length1 >= length2:
      return my_list1[-1]
    else:
      return my_list2[-1]

  # Refactor 2
  def larger_list(my_list1, my_list2):
    if len(my_list1) >= len(my_list2):
      return my_list1[-1]
    else:
      return my_list2[-1]
    
#4 More Than N
  # Write your function here
  def more_than_n(my_list, item, n):
    if my_list.count(item) > n:
      return True
    else:
      return False    

  # Uncomment the line below when your function is done
  print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#5 Combine Sort
  # Write your function here
  def combine_sort(my_list1, my_list2):
    my_combine = my_list1 + my_list2
    my_combine = sorted(my_combine)
    return my_combine

  # Uncomment the line below when your function is done
  print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

  # Refactor
  def combine_sort(my_list1, my_list2):
    sorted_combine = sorted(my_list1 + my_list2)
    return sorted_combine

  # Uncomment the line below when your function is done
  print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))