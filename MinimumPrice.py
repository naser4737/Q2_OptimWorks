import csv

def min_price_restaurant(csv_file, food_items):
    restaurant_data = {}
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            restaurant_id = int(row['restaurant_id'])
            price = float(row['price'])
            food_item = row['food_item_name']
            
            if restaurant_id not in restaurant_data:
                restaurant_data[restaurant_id] = {}
            restaurant_data[restaurant_id][food_item] = price
    
   
    food_items = food_items.split()  
    matching_restaurants = {}
    
    for restaurant_id, menu in restaurant_data.items():
        if all(item in menu for item in food_items):
           
            total_price = sum(menu[item] for item in food_items)
            matching_restaurants[restaurant_id] = total_price
    
   
    if matching_restaurants:
        min_restaurant = min(matching_restaurants, key=matching_restaurants.get)
        min_price = matching_restaurants[min_restaurant]
        return f"{min_restaurant}, {min_price:.2f}"
    else:
        return "No matching restaurant found"

csv_file = "C:/Users/DELL/OneDrive/Desktop/OptimWorks/Q2_backend/question_two_data.csv"


input_1 = "burger tofu_log"
print(min_price_restaurant(csv_file, input_1))  # Output: 7, 10.50

input_2 = "chef_salad wine_spritzer"
print(min_price_restaurant(csv_file, input_2))  #  Output: No matching restaurant found
