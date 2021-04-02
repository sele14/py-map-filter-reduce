import math
import sys
import statistics

# source: https://www.youtube.com/watch?v=hUes6y2b--0&list=WL&index=13&ab_channel=Socratica

print("\n")
print("..... MAP FUNCTION ......")

l = [1, 3, 9, 4, 2]

def area(r):
    # r = int(sys.argv[1])
    """Calculates the area of a cirlce with radius 'r'."""
    return round((math.pi * r**2), 2)

# check area of unit circle
print(area(1))

# check for multiple areas; using map (similar to apply in DFs)
    # note: only works on functions that take an input
print(list(map(area, l)))


##### MAP EXAMPLE on tuples
temps = [("Oslo", 2), ("London", 10), ("Los Angeles", 19),
        ("New York", 8), ("Shanghai", 15)
        ]

# takes tuple as input and returns tuple output
# of the form (city name, degrees F)
c_to_f = lambda data: (data[0], 9/5 * data[1] + 32)

# apply c_to_f function to our temps tuples
print(list(map(c_to_f, temps)))

###### FILTER FUNCTION  ####
print("\n")
print("..... FILTER FUNCTION ......")
prices = [41, 55, 19, 2, 99, 12, 55]
avg = statistics.mean(prices)

print("Average is: ", avg)
print("Values above average are: ")
print(list(filter(lambda p: p > avg, prices)))


print("\n")
print("..... REDUCE FUNCTION ......")
