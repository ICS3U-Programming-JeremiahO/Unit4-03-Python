#!/usr/bin/env python3
# Created By: Jeremiah Omoike
# Date: November 2 2022
# This program gets a number from a user and then calculates all number to the user then multiplies them by the power of 2


def main():

    # set variables
    User_number_as_string = input("Enter a positive integer here: ")
    # input
    # this part of the program ensures that the user enters a valid input. any erronious
    # input will be detected and instead of the program crashing, the program will display that it is invalid input
    try:
        User_number_as_int = int(User_number_as_string)
        # to make sure that use input is more than zero
        if User_number_as_int < 0:
            print("")
            print(" please input a whole number ")
        # process
        # if user number is more than 0 then the program will progress to the for loop
        elif User_number_as_int >= 0:
            # Loops and lists the program and multiplies the counter time to the power of 2 each time
            # up untill the counter is looped the same times as the user input
            for counter in range(User_number_as_int + 1):
                power_of_two = counter**2
                print()
                print("{}^2 = {}.".format(counter, power_of_two))
    # bottom part of the try catch
    except Exception:
        print()
        print("please input a whole number ")
    finally:
        print()
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
