def solve(s):
    # Define the list of consonant letters
    consonants = "bcdfghjklmnpqrstvwxyz"

    # Initialize variables to keep track of the maximum value and the current value
    max_value = 0
    current_value = 0

    # Iterate through each character in the input string
    for char in s:
        # Check if the character is a consonant
        if char in consonants:
            # Calculate the value of the consonant and add it to the current value
            consonant_value = ord(char) - ord('a') + 1
            current_value += consonant_value
        else:
            # If the character is not a consonant, update the max_value if needed
            if current_value > max_value:
                max_value = current_value
            # Reset the current value for the next consonant substring
            current_value = 0

    # Check and update max_value for the last consonant substring
    if current_value > max_value:
        max_value = current_value

    return max_value

# Test cases
print(solve("zodiacs"))   # Output: 26
print(solve("strength"))  # Output: 57
