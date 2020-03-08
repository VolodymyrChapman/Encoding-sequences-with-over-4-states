import string
import random as ran
import string
from sympy import *

# The file is divided into five parts:
#        1) Creating encoding protocols (ciphers), needed to determine the numerical value of each letter in a message
#        2) Using a chosen cipher to set appropriate coordinates for each letter in a message
#        3) Using a modified, circle-based chaos game representation algorithm to encode the message into
#           X and Y values - if the encoding cipher is known, the encoding process can be reversed to 
#           retrieve the original message
#        4) Pipeline function to conduct steps 2) and 3) for testing of encoding
#        5) Testing with text 

# 1) Making ciphers:
# Make a cipher function - input is a list of characters in the desired abundance - this
#function jumbles these letters randomly to make a cipher

def Cipher(letters):
    mixed_letters = letters[:]
    ran.shuffle(mixed_letters)
    return mixed_letters

# Cipher function to make  desired number of ciphers, 
# all in a list so they're not created individually

def CipherMulti(number, letters):
    ciphers = []
    for i in range(number):
        new_cipher = Cipher(letters)
        ciphers.append(new_cipher)
    return ciphers



# 2) Encoding of a message using a chosen cipher: 
#  - Make a list of corresponding X and Y values for each character in the message (which corner the letters are in)

# Making lists of X and Y coordinates for each letter of the message 
def CoordinateSetter(unprocessed_message, cipher):
    message = unprocessed_message.upper()  # convert all letters in message to uppercase in case any in lowercase
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


#3) Using the Xn+1 = (Xn + Ln)/2 encoding pattern over letter coordinates to find the 
# final X and Y values (which can be used to decode the message) 

# - Use the Xn+1 = (Xn + Ln)/2 encoding pattern to find the X and Y coordinates of the final point.
# Can work backwards from this final value to decode the message
def Encoder(coordinates):
    encoded_coordinates = [0]                       # Initiate list for coordinates

    for i in range(len(coordinates)):   
        
        encoded_value = (encoded_coordinates[-1] + coordinates[i])/2
        encoded_coordinates.append(encoded_value)            
    return encoded_coordinates


# 4) Pipeline for CoordinateSetter() and Encoder()

def MessageToCGR(message, cipher):
    X, Y = CoordinateSetter(message, cipher)
    encoded_X = Encoder(X)
    encoded_Y = Encoder(Y)
    
    return encoded_X, encoded_Y


# 5) Speed testing using first 2,490 characters of Mary Shelley's 
#    Frankenstein (used under the Project Gutenberg license)

#Making a cipher using a letter list
letter_list = list(string.ascii_uppercase)
letter_list.extend(["." , "," ," ", "!" , "?", "'", ";", "\n", "-", "—"]) # extending with punctuation
cipher = Cipher(letter_list)


Sample_text = """You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. 
I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking.
I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, 
which braces my nerves and fills me with delight. Do you understand this feeling? This breeze, which has travelled from the regions 
towards which I am advancing, gives me a foretaste of those icy climes. Inspirited by this wind of promise, my daydreams become more fervent 
and vivid. I try in vain to be persuaded that the pole is the seat of frost and desolation; it ever presents itself to my imagination as the 
region of beauty and delight. There, Margaret, the sun is for ever visible, its broad disk just skirting the horizon and diffusing a 
perpetual splendour. There—for with your leave, my sister, I will put some trust in preceding navigators—there snow and frost are banished; 
and, sailing over a calm sea, we may be wafted to a land surpassing in wonders and in beauty every region hitherto discovered on the habitable 
globe. Its productions and features may be without example, as the phenomena of the heavenly bodies undoubtedly are in those undiscovered solitudes. 
What may not be expected in a country of eternal light? I may there discover the wondrous power which attracts the needle and may regulate a thousand 
celestial observations that require only this voyage to render their seeming eccentricities consistent for ever. I shall satiate my ardent curiosity 
with the sight of a part of the world never before visited, and may tread a land never before imprinted by the foot of man. These are my enticements, 
and they are sufficient to conquer all fear of danger or death and to induce me to commence this laborious voyage with the joy a child feels when 
he embarks in a little boat, with his holiday mates, on an expedition of discovery up his native river. But supposing all these conjectures to be 
false, you cannot contest the inestimable benefit which I shall confer on all mankind, to the last generation, by discovering a passage near the 
pole to those countries, to reach which at present so many months are requisite; or by ascertaining the secret of the magnet, which, if at all 
possible, can only be effected by an undertaking such as mine."""

# time process
%timeit time = MessageToCGR(Sample_text, cipher)

#4.8 s ± 8.68 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)