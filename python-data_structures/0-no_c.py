def no_c(my_string):
    # Convert the string to a list of characters
    chars = list(my_string)
    
    # Iterate through the characters in reverse order
    index = len(chars) - 1
    while index >= 0:
        if chars[index] == 'c' or chars[index] == 'C':
            # Remove 'c' or 'C' from the list
            del chars[index]
        index -= 1
    
    # Convert the list of characters back to a string
    return ''.join(chars)