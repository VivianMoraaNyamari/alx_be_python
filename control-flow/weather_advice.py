# prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

#provide clothing recommendation using if-elif-else
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.") 
elif  weather == "rainy":
    print("Dont forget your umbrella and a raincoat.")
elif weather == "cold":
    print(" Make sure to wear a warm coat and a scarf.")
else:
    print("sorry, I dont have recommendations for this weather.")