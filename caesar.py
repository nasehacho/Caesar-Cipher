# define message variable and key value variable 
message = "SECRET"
k = 10 

# defining function "encrypt" and its arguments "message" and "k"
def encrypt(message, k):
    # result placeholder
    encrypted = ""
    # creating a for loop that iterate onto each letter of our message 
    for x in message:
        # utilize the ord() function to implement the ASCII code onto the alphabetic characters in our message 
        char_num = ord(x)
        # implement the caesar cipher by adding our key value, 10 to the char__num we have so far
        shift_code = char_num + k 
        # to make sure the shifting restarts when we hit the letter "z", implement and "if statement" to only return alphabetic characters
        # after 90 on the ASCII table, there are no uppercase alphabetic letters therefore, numbers after 90 on the table should be changed
        if shift_code > 90:
            # there are 26 letters in the alphabet, once we hit "z" subtracting by 26 will bring us back to "A"
            shift_code = shift_code - 26 
        # convert the number code back into alphabetic characters using the chr() function
        caesar_code = chr(shift_code)
        # add only caesar_code function onto the message to only bring back our encrypted text
        encrypted = encrypted + caesar_code
    return encrypted 
# calling the function and printing out a statement as to what the encrypted message is
encrypted = encrypt(message, k)    
print("Your encrypted word is", encrypted)

def decrypt(encrypted, k):
    decrypted = ""
    for x in encrypted:
        char_num = ord(x)
        # we want to "unshift" our code to bring back the original message, therefore, we subtract from the key value 
        shift_code = char_num - k 
        # to incorporate only alphabetic letters again, we add an "if statement" to only incorporate uppercase letters of the ASCII table 
        if shift_code < 65:
            # add 26 instead of subtract because we want to keep it in the upper case alphabet
            shift_code = shift_code + 26 
        caesar_code = chr(shift_code)
        decrypted = decrypted + caesar_code
    return decrypted 

decrypted = decrypt(encrypted,k)
print("Your decrypted word is", decrypted)