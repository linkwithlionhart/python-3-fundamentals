"""
You’ve started a position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.
"""

brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    self.bill = 0
  
  def __repr__(self):
    return f"The {self.name} menu is available from {self.start_time} to {self.end_time}."

  def calculate_bill(self, purchased_items):
    for purchase in purchased_items:
      if purchase in self.items:
        self.bill += self.items[purchase]
    return self.bill

Brunch = Menu("Brunch", brunch, "11", "4pm")
Early_Bird = Menu("Early Bird", early_bird, "3pm", "6pm")
Dinner = Menu("Dinner", dinner, "5pm", "11pm")
Kids = Menu("Kids", kids, "11am", "9pm")

# print(Brunch, Early_Bird, Dinner, Kids)
# print(Brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
# print(Early_Bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

# Creating the Franchises
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return f"Address: {self.address}."
  # Takes time and returns available menus
  def available_menus(self, time):
    pass

flagship_store = Franchise("1232 West End Road", [Brunch, Early_Bird, Dinner, Kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# print(flagship_store, new_installment)
print(flagship_store.menus)

# Next: convert times to military and if input time in range, return relevant menu. Easiest to do without involving a module.

