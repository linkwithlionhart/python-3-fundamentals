"""
The goal of this program is to ask the user for the weight of their package and return the method of shipping that is the cheapest as well as how much it will cost to ship their package using Sal's Shippers.
"""

weight = 41.5

# Ground shipping
def gs_reg(weight):
  flat_rate = 20.00
  pound_price = 0.00
  total_charge = 0.00

  if weight > 10:
    pound_price = 4.75
  elif weight > 6 and weight <= 10:
    pound_price = 4.00
  elif weight > 2 and weight <= 6:
    pound_price = 3.00
  else:
    pound_price = 1.50

  total_charge = flat_rate + (weight*pound_price)
  return total_charge

def gs_premium(weight):
  flat_rate = 125.00
  total_charge = 0

  total_charge = flat_rate + (weight * 0)
  return total_charge

def ds_reg(weight):
  flat_rate = 0
  pound_price = 0
  total_charge = 0

  if weight > 10:
    pound_price = 14.25
  elif weight > 6 and weight <= 10:
    pound_price = 12.00
  elif weight > 2 and weight <= 6:
    pound_price = 9.00
  else:
    pound_price = 4.50

  total_charge = flat_rate + (weight*pound_price)
  return total_charge

print('Charge for ground shipping:')
print(gs_reg(weight)) 
print()
print('Charge for ground shipping premium:')
print(gs_premium(weight))
print()
print('Charge for drone shipping:')
print(ds_reg(weight))