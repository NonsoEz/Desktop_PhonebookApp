from collections import Counter

def count_freq():

    # number of items to be counted
    n = int(input("Input the number of elements to be stored in the list: "))
    # initialize empty list to store items to be counted
    myList = []
    # for incrementing numbers of items inputted
    num_inputted = 0
    print(f"Input {n} elements in the list: ")

    # loop through items in range(n)
    for items in range(n):
        while num_inputted < n:
            num = int(input(f"element - {num_inputted}: "))
            # to count the numbers inputted
            num_inputted+= 1
            # append elements inputted to list for counting
            myList.append(num)

            # convert list to dictionary so that Counter method can be used
            #then assign it to counter name
            counter = dict(Counter(myList))

    # loop through counter elements and print out frequency
    print("\nThe frequency of all elements in the list is: ")
    for elem in counter.items():
        print(f"{elem[0]} occurs {elem[1]} times",'')


# function call
count_freq()