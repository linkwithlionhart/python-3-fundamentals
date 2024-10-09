"""
You’ve started a position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.
"""
# Making the Menus
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
  
  def __repr__(self):
    return f"The {self.name} menu is available from {self.start_time} to {self.end_time}."

  def calculate_bill(self, purchased_items):
    self.bill = 0 # reset bill
    for purchase in purchased_items:
      if purchase in self.items:
        self.bill += self.items[purchase]
    return self.bill

Brunch = Menu("Brunch", brunch, 1100, 1600)
Early_Bird = Menu("Early Bird", early_bird, 1500, 1800)
Dinner = Menu("Dinner", dinner, 1700, 2300)
Kids = Menu("Kids", kids, 1100, 2100)

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
    menu_list = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        # menu_list.append([menu.name, menu.items])
        menu_list.append(menu)
    return menu_list

menus = [Brunch, Early_Bird, Dinner, Kids]
flagship_store = Franchise("1232 West End Road", menus)

new_installment = Franchise("12 East Mulberry Street", menus)

# print(flagship_store, new_installment)
# print(flagship_store.menus, new_installment.menus)
# print(flagship_store.available_menus(1200))
# print(new_installment.available_menus(1700))

# Creating Businesses!
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

Arepas = Menu("Arepas", arepas_menu, 1000, 2000)
menus.append(Arepas)
arepas_place = Franchise("189 Fitzgerald Avenue", menus)

arepa_biz = Business("Take a' Arepa", arepas_place)

print(arepa_biz.name)
print(arepa_biz.franchises)
# print(arepa_biz.franchises.menus)
print(arepa_biz.franchises.available_menus(1200))
# print(arepa_biz.franchises.available_menus(1700))
print(Arepas.calculate_bill(["arepa pabellon", "pernil arepa", "guayanes arepa", "jamon arepa"]))

# Code Review
"""
Avoid modifying the `menus` list directly when adding new menus to prevent unintended side effects. Instead, create a new list for each franchise.

arepas_menus = menus + [Arepas]
"""

"""
Consider using list comprehensions for more concise and efficient code when filtering available menus.

menu_list = [menu for menu in self.menus if menu.start_time <= time <= menu.end_time]
"""
