#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Nov 11, 2023
# This program uses a for loop to get the exponent of the user number


def main():
    user_num_str = input("Enter a whole number : ")

    try:
        user_num_int = int(user_num_str)
        if user_num_int < 0:
            print("Invalid number")
        else:
            for counter in range(user_num_int + 1):
                power_of_two = counter**2
                print("{}^2 = {}".format(counter, power_of_two))

    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
