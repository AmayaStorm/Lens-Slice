# Your code below:
#checkpoint 1
toppings= ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
#checkpoint 2
prices= [2, 6, 1, 3, 2, 7, 2]
#checkpoint 3
num_two_dollar_slices=prices.count(2)
print(num_two_dollar_slices)
#check 4
num_pizzas= len(toppings)
print(num_pizzas)
#check 5
print("We sell 7 different kinds of pizza!")
#check 6
pizza_and_prices=[[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3,"sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
#check 7 
print(pizza_and_prices)
#check 8
pizza_and_prices.sort()
print(pizza_and_prices)
#check 9
cheapest_pizza= pizza_and_prices[-7]
print(cheapest_pizza)
#check10
priciest_pizza= pizza_and_prices[6]
print(priciest_pizza)
#check11
pizza_and_prices.pop()
print(pizza_and_prices)
#check12
pizza_and_prices.insert(4, [2.5,"peppers"])
print(pizza_and_prices)
#check13 and 14
three_cheapest= pizza_and_prices[0:3]
print(three_cheapest)
