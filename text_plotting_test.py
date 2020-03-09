import string
import random as ran
import string
from sympy import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#Testing circular CGR plotting with first 2,490 characters of Mary Shelley's Frankenstein
#For more detail on the purpose of each function, please consult the text_to_CGR_coordinates.py file.

# 1) Making ciphers:
def Cipher(letters):
    mixed_letters = letters[:]
    ran.shuffle(mixed_letters)
    return mixed_letters


# 2) Encoding of a message using a chosen cipher: 
def CoordinateSetter(unprocessed_message, cipher):
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

#3) Using the Xn+1 = (Xn + Ln)/2 encoding pattern over letter coordinates to find the CGR coordinates
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

# Plotting real text:

# Initiate list of letters
letter_list = list(string.ascii_uppercase)
letter_list.extend(["." , "," ," ", "!" , "?", "'", ";", "\n", "-", "—"]) # extending with punctuation
test_cipher = Cipher(letter_list)   # create an encoding cipher
print(test_cipher)  #print cipher used - cipher starts at top of the radius 1 circle; each subsequent character is at a (2*pi)/(cipher length)
               # angle clockwise around the circle (with respect to the origin (0,0) )


# Input text
sample_text = """You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. 
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

# Retrieve CGR coordinates for text:
encoded_X, encoded_Y = MessageToCGR(sample_text, test_cipher)

#plot a guide circle to show associated letters
guide_circle = patches.Circle((0,0), radius=1, fill = False, ls = '-', color = 'k')
#Add associated letters on the guide circle
test_cipher_string = ''.join(test_cipher)
circle_X, circle_Y = CoordinateSetter(test_cipher_string, test_cipher)

# Plot guide circle, coordinates of each letter and annotations for letters
fig, ax = plt.subplots()
ax.add_artist(guide_circle)
ax.plot(circle_X,circle_Y, 'ro')
#Annotate each letter on the circle
for i in range(len(test_cipher)):
    circle_xy = [circle_X[i], circle_Y[i]]
    plt.annotate(xy = circle_xy, s = test_cipher[i])

# plot sample text CGR
ax.plot(encoded_X,encoded_Y, 'b.')