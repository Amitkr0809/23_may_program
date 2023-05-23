def get_reversed_string(string):
    # Complete this recursive function
    if len(string) == 0:
        return string
    else:
        return get_reversed_string(string[1:]) + string[0]


string = input("enter string : ")

resultant_string = get_reversed_string(string)
# Call the get_reversed_string function
print(resultant_string)