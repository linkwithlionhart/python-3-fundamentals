"""
The goal of this program is to organize subjects and grades with lists and list methods.
"""

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [
  ["physics",	98],
  ["calculus",	97],
  ["poetry",	85],
  ["history",	88]
]

print(gradebook)
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)

gradebook[-1][-1] += 5
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook[2])

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)