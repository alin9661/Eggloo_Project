# Eggloo_Project

This project consists of the various combinations that waffles can be made using the ice cream flavors, toppings, and drizzles avaliable.  
To make a cone the ingredients must be made in a specific sequence where we are limited to having 1 ice cream flavor, 2 toppings, and 1 drizzle per cone. The total number of combinations can be calculated using combinatorics where we are given 7 ice cream flavors, 9 toppings, and 4 drizzles (Each combination also includes the cone itself). We can work out this number by considering the different cases for which somebody can construct a cone.

Case 1: Just cone + ice cream  
Case 2: Cone + ice cream + drizzle  
Case 3: Cone + ice cream + 1 topping  
Case 4: Cone + ice cream + 1 topping + drizzle  
Case 5: Cone + ice cream + 2 topping  
Case 6: Cone + ice cream + 2 topping + drizzle  

Since we don't care for order (i.e putting Fruity Pebbles and then Oreo toppings is the same as Oreo and Fruity Pebbles) without replacement, the number of ways to choose 2 toppings from 10 toppings (9 toppings + possibility of picking no topping) is 45  
Therefore to find the total number of combinations from 7 ice creams, 10 toppings, 5 drizzles (+1 topping and drizzle for the possibility of no topping or no drizzle) is 7(5 + 5(10 choose 2)) = **1610 different waffle cones**

![image](https://user-images.githubusercontent.com/90729424/180626783-db062dd4-b734-42a5-9732-03dd003dbd43.png)
