# Encoding
Methods of encoding messages (or any sequence of more than 4 possible states) using circular Chaos Game Representation algorithm

encoding_messages.py works through steps to encode messages into a single X and Y coordinate. If the cipher used to encode the message is known, the original message can be decoded from the coordinates. The file contains functions for:
1) Creating ciphers by randomising a list of characters

2) Assigning each character in a message with a point (Ln) on a radius 1 circle (x^2 + y^2 = 1). These values are used to determine the final X and Y values (the encoded message) in step 3. 

3) Encoding of the message using an extended Chaos Game algorithm, using a rearranged chaos game algorithm:
Original algorithm: 
Xn+1 = (Xn + Ln)/2                     where Xn is the current X coordinate of the point and Ln is the coordinate of the associated character on the circle

Rearranged algorithm to give only final value of X:
 Xm = Sum of Ln/2^(m-n)                 starting at n=0, where Ln is the coordinate of the associated letter on the circle, n is the position of the letter in the message to be encoded (where the first letter is point 0) and m is the length of the message.
 
 Note: use of symbolic python (SymPy) is essential for accuracy of this circular chaos game encoding method, unlike traditional chaos game encoding
