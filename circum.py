#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Oct 2021
# This program calculates the time to Mars

import constants


def main():
    # this function calculates the circumference of a circle

    # input
    radius = int(input("Enter radius of circle (cm): "))

    # process
    circumference = radius*constants.TAU

    # output
    print(f"Circumference of circle with a radius of {radius} cm is roughly: {circumference} cm")

    print("\nDone.")


if __name__ == "__main__":
    main()