import string
import random as ran
import string
from sympy import *

# The file is divided into three parts:
#                                    1) Creating encoding protocols (ciphers), needed to determine the numerical value of each letter in a message
#                                    2) Using a chosen cipher to set appropriate coordinates for each letter in a message
#                                    3) Using a modified, circle-based chaos game representation algorithm to encode the message into
#                                       single, final X and Y values - if the encoding cipher is known, the encoding process can be reversed to 
#                                       retrieve the original message

# Notes:
#       - Test cases are provided and clearly labelled with 'test case:' comments. These are not essential and can be commented out if just the functions are desired.
#       - Symbolic mathematics is used to reduce the impact of floating point errors, which I have found to significantly affect
#         encoding if not used. If final values are preferred as floats, please use the   float() function to convert symbolic 
#         numbers to floats. 
#         Given the impact of floating point errors on the working of this technique, this should only be used for final X and Y values.
#         Please refer to the SymPy documentation for clarification on symbolic maths in Python.


# 1) Making ciphers:
# Generating a range of ciphers that can be used to encode a message. A user can then choose which cipher to use.
#Making a list of letters 
letter_list = list(string.ascii_uppercase)
letter_list.extend(["." , "," ," ", "!" , "?", "'"]) # extending with punctuation

# Make a cipher function - input is a list of characters in the desired abundance - this
#function jumbles these letters randomly to make a cipher

def cipher(letters):
    mixed_letters = letters[:]
    ran.shuffle(mixed_letters)
    return mixed_letters

# Make a cipher using out letter list
mixed_letters = cipher(letter_list)

# Cipher function to make  desired number of ciphers, 
# all in a list so they're not created individually

def cipher_multi(number, letters):
    ciphers = []
    for i in range(number):
        new_cipher = cipher(letters)
        ciphers.append(new_cipher)
    return ciphers


#Test case: multiple cipher function
cipher_list = cipher_multi(20, mixed_letters)
#print("First cipher in list:{}".format(cipher_list[0]))



# 2) Encoding of a message using a chosen cipher: 
#  - Make a list of corresponding X and Y values for each character in the message (which corner the letters are in)

# Making lists of X and Y coordinates for each letter of the message 
def coordinate_setter(unprocessed_message, cipher):
    message = unprocessed_message.upper()           # convert all letters in message to uppercase in case any in lowercase
    X = []                     # initialise X and Y lists
    Y = []
    for letter in message:
       position = cipher.index(letter)    # Position of the letter within the cipher 
                                          # used to determine which direction desired 
                                          # letter is in on chaos plot

       angle = (2*position*pi)/len(cipher)  # angle from (0,1) position (12 O'clock)
       
       Yn = cos(angle) 
       Xn = sin(angle)

       Y.append(Yn)
       X.append(Xn)
    return X, Y

# Test case: coordinate setter function 
cipher_list = cipher_multi(20, mixed_letters)
chosen_cipher = cipher_list[15]
message = "Hey buddy, how's it going?"
X_test,Y_test = coordinate_setter(message, chosen_cipher)




#3) Using the Xn+1 = (Xn + Ln)/2 encoding pattern over letter coordinates to find the 
# final X and Y values (which can be used to decode the message) 

# - Use the Xn+1 = (Xn + Ln)/2 encoding pattern to find the X and Y coordinates of the final point.
# Can work backwards from this final value to decode the message
def encoder(coordinates):
    encoded_value = 0                       # Start the value at 0

    for i in range(len(coordinates)):   
        power = len(coordinates) - i        #Find the power of 2 to divide by, which equal to length of sequence - position of the letter, starting from 0. 
        value = coordinates[i]/2**power
        encoded_value += value            
    return encoded_value

#test case: encoder function with X and Y
encoded_X = encoder(X_test) 
encoded_Y = encoder(Y_test)