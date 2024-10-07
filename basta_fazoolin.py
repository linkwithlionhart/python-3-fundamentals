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
    for cost in purchased_items.values():
      bill += cost

Brunch = Menu("Brunch", brunch, "11am", "4pm")
Early_Bird = Menu("Early Bird", early_bird, "3pm", "6pm")
Dinner = Menu("Dinner", dinner, "5pm", "11pm")
Kids = Menu("Kids", kids, "11am", "9pm")

print(Brunch, Early_Bird, Dinner, Kids)
