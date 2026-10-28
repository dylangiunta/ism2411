# 1. The most surprising thing about lists is how easy they are to edit, using .remove or .append. 
# Thought it would be more difficult to edit lists coming into it.
# 2. In my job working at a golf course, I have not had to handle the tournaments scoring,
# but I feel like it would be able to help speed up finding things like scoring average, highs and lows etc.
# I do not know how it would have been different in excel because I have not had to use it yet.
# Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory)) 

# Exercise 2 

print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2 
print(inventory[middle]) 

# Exercise 3 

print(inventory[:3]) 
print(inventory[-2:])
print(inventory[::2])

# Exercise 4 

inventory.append("envelope")
inventory.remove("tape")
inventory.sort()
print(inventory)

# Exercise 5 

coords = (40.1728, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print(f"Tuples protect coordinates from being changed by accident") 

print(coords) 

# Exercise 6 

sales = [100,250,75,480,200]

total = sum(sales)
count = (len(sales))
average = total / count
best = max(sales)
worst = min(sales)


print(f"Total: {total}")
print(f"Average : {average}")
print(f"Best: {best}")
print(f"Worst: {worst}")

# Exercise 7 

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9,2))

print(prices)
print(discounted)

# Exercise 8 

sales = [340,127,589,204,467,88,731,315,62,490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")