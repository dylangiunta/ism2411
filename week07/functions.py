# Self-Assessment Questions 
#1. The first bug I spotted was the lack of the plus sign for total+= sale. I found it from explaining the code outloud because the total could not increase, or grow without the plus sign. 
# It shows that I have a basic understanding of where things should be in order to see the proper output. 
# 2. apply_discount(price, tier) is a function named apply discount that takes two arguments that represent a price and a tier. You get to decide what the function returns to you after using those two values.  
# A colleague could probably use it without reading the body because the function is fairly simple. 
# 3. Yes, I did use AI to help me complete this lab. I fed it a couple error messages and asked what they mean. I did this in broken sales and did it in the function file.
# I used it on this main file because I kept getting an error of python trying to add a string and an integer together. I found the problem and all it was is that I entered variables in the wrong order in exercise 4 for final_price. 
# AI did help to build my understanding because after it told me what the error meant, I was able to understand what needed to be fixed and it jumped out at me. It shortcutted me once because I wanted to understand the third error in broken sales fully, so I asked for an explanation of the code instead of just the error message. 
# Exercise 1  

def calculate_tax(price,rate):
    return price * rate

tax1 = calculate_tax(100,0.07) # Calling the function
tax2 = calculate_tax(250,0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")

# Exercise 2 
# Function defined with multiple parameters
def apply_discount(price, tier):
    if tier == 'gold': 
        return price * 0.85
    elif tier == 'silver':
        return price * 0.90 
    elif tier == 'bronze':
        return price * 0.95
    else:
        return price 

original_price = 200 

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}") 

# Exercise 3 

def final_price(price,tax_rate , discount_tier ):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax 

# Calling the final price function 

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4 

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]
rate = 0.07
for price, tier in orders:
    total = final_price(price, 0.07, tier  )
    print(f"Price: {price} | Tier: {tier} | Final: ${total:.2f}")

# Exercise 5 Broken Sales file fixed 

 # broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales: 
    total += sale # There needed to be a + next to the = sign in order for the total to accumulate. 
print(f"Total: ${total}")

count = 0
for sale in sales: # There needed to be a : in front of sales. 
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # There only needed to a < instead of <= 
    print(sales[i])
    i += 1

# Exercise 6 
# Scope refers to the area in which a variable exists. In this case, the variable x = 999 only exists inside the scope/ area of the function. 
# We can tell it is inside the area of the function because it is down the branch from def and indented, which shows that it is inside. 
x = 100   # global variable

def double_it():
    x = 999   
    return x * 2

print(x)           
print(double_it()) 
print(x)           