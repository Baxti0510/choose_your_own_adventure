name = input("Enter your name: ")
print("Welcome", name, "to this adventure")
print()

answer = input("You are on a dirt road, it has come to an end and "
               "\nyou can go left or right. Which way would you like to go? (left/right) ").lower()
print()
if answer == "left":
    answer = input("You came to a river, you can walk around it or swim across? (swim/walk) ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walk many miles and ran out of water and you lost the game.")
    else:
        print("Not a valid option, you lose.")

elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ")
    print()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to him? (yes/no) ").lower()
        print()

        if answer == "yes":
            print("You talked to stranger and they gave you gold and you WIN!!! ")
        elif answer == "no":
            print("You ignored the stranger and they offended and you lost. ")
        else:
            print("Not a valid option, you lose.")
    else:
        print("Not a valid option, you lose.")
else:
    print("Not a valid option, you lose.")

print()
print("Thank you for trying", name)