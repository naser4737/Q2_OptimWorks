# Q2_OptimWorks

Question: 2 Minimum Price
Problem Statement: You are given a CSV file consists of restaurent_id, food_item_price and food_item_name and your input is food item names, you need to find the minimum price for the food items in specified restaurants and all the food items should be available in single restaurant or return null

Here are some sample data sets, program inputs, and the expected result:
Input-1: data.csv file, burger tofu_log
Explanation:
Search for restaurants that have both "burger" and "tofu_log".
Restaurant 1: "burger" (4.00) + "tofu_log" (8.00) = 12.00
Restaurant 2: "burger" (5.00) + "tofu_log" (6.50) = 11.50
Restaurant 7: "burger" (3.50) + "tofu_log" (7.00) = 10.50
Expected Output-1: 7, 10.50


Input-2: data.csv file, chef_salad wine_spritzer
Expected Output-2: “No matching restaurant found”
