scoops=input('How many scoops of ice cream do you want? ')
number_of_scoops=int(scoops)
if number_of_scoops == 0:
    print("You didn't have any ice cream?")
    print('we have lots of flavors.')

elif number_of_scoops == 1:
    print("A single scoop for you, coming up.")
elif number_of_scoops == 2:
        print("Oh, two scoops for you, coming up!")
elif number_of_scoops >= 3:
            print("Wow, that's a lot of scoops!")
else:
    print("I'm sorry I can't give you negative scoops.")
    
