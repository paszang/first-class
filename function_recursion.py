def sum_of_digits(n):
    if  n< 10:       # Base case: if n is single_digit number, return n 
        return n  

    else:     #Recursive case: calculate the sum of digits
        last_digit = n % 10          #Get the last sum of digits
        remaining_digits = n // 10   #Get the remaining digits by integer division with 10

        return last_digit + sum_of_digits(remaining_digits) #Recursively call the function with the remaining digits
                                                            #and add the last digit to the result 
    
print(sum_of_digits(123))

