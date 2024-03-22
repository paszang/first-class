def reverse_string(s):
    # Base case: if the string is empty or has only one character, return s
    if len(s) <= 1:
        return s
    # Recursive case: concatenate the last character with the reversed substring of the string excluding the last character
    else:
        return s[-1] + reverse_string(s[:-1])

# Example usage:
input_string = "Tupac , Shakur!"
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)
