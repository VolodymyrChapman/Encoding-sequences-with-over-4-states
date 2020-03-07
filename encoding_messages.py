import math 
import numpy as np
import string
import random as ran
import string

# Making ciphers:
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

#Testing the multiple cipher function
cipher_list = cipher_multi(20, mixed_letters)
print("First cipher in list:{}".format(cipher_list[0]))






# Encoding: 
# 1) Make a list of corresponding X and Y values for each character in the message (which corner the letters are in)
# 2) Use the Xn+1 = (Xn + Ln)/2 encoding pattern to find the X and Y coordinates of the final point.
# Can work backwards from this final value to decode the message


# 1) Making lists of X and Y coordinates for each letter of the message 
def coordinate_setter(unprocessed_message, cipher):
    message = unprocessed_message.upper()           # convert all letters in message to uppercase in case any in lowercase
    X = []                     # initialise X and Y lists
    Y = []
    for letter in message:
       position = cipher.index(letter)    # Position of the letter within the cipher 
                                          # used to determine which direction desired 
                                          # letter is in on chaos plot

       angle = (2*position*math.pi)/len(cipher)  # angle from (0,1) position (12 O'clock)

       # Rounded with numpy so no floating point arithmetic rounding errors
       Yn = np.around(np.cos(angle), decimals=(len(message)+1)) #decimals cut at len(message+1) as final coordinate has same
                                                                # number of decimal places as message (as a result of X/(2^length))
       Xn = np.around(np.sin(angle), decimals=(len(message)+1))
       Y.append(Yn)
       X.append(Xn)
    return X, Y


# Testing the coordinate setter function - requires cipher_multi function 
# and mixed_letters list from making_ciphers.py file
cipher_list = cipher_multi(20, mixed_letters)
chosen_cipher = cipher_list[15]
message = "Hey buddy, how's it going?"
X_test,Y_test = coordinate_setter(message, chosen_cipher)


#2) Using the Xn+1 = (Xn + Ln)/2 encoding pattern over letter coordinates to find the 
# final X and Y values (which can be used to decode the message) 
def encoder(coordinates):
    encoded_value = 0                       # Start the value at 0

    for i in range(len(coordinates)):   
        power = len(coordinates) - i        #Find the power of 2 to divide by, which equal to length of sequence - position of the letter, starting from 0. 
        value = coordinates[i]/2**power
        encoded_value += value            
    return encoded_value

#test encoder function with X and Y
encoded_X = encoder(X_test) # Will show limited numbers of decimal places
encoded_Y = encoder(Y_test) # Expected decimal places are equal to the message length


# Function utlilising the "{0:.xf}".format(number) method, where x = desired number of decimal places
# and 'number' is the number that you would like to display 

def decimal_place_cutter(message, encoded_data):
    dp = len(message) # desired number of decimal places
    prefix = "\"{0:."
    suffix = "f}\""
    decimal_place = prefix + str(dp) + suffix
    decimal_place.format(encoded_data)

 # Test decimal place cutting

decimal_place_cutter(message, encoded_X)
