#!/usr/bin/env python



def bottles_song():
    for i in range(99, 0, -1):
        if i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("You take one down and pass it around, no more bottles of beer on the wall.")

        elif i == 2: 
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"You take one down and pass it around, {i-1} bottle of beer on the wall.")

        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")

    print("No more bottles of beer on the wall, no more bottles of beer. \n " )

    print("How many bottles do you want to count down from? ")
    i = int(input("Enter the number of bottles: "))
    
    

    print(f"{i} of beer on the wall, {i} bottles of beer.")
    print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")

bottles_song()
