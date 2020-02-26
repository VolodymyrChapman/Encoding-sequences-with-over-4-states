# encoding
Methods of encoding messages using Chaos Game Representations

encoding_messages.py works through steps to encode messages into a single X and Y coordinate. If the cipher used to encode the message is known, the original message can be decoded from the coordinates. The file contains functions for:
1) Creating ciphers by randomising a list of characters
2) Assigning each character with a point on a radius 1 circle (x^2 + y^2 = 1)
3) Assigning each character in a message with the coordinates of the relevant character on the circle
4) I rearranged the chaos game algorithm ( (Xn+1 = (Xn + Zm)/2 ) where Xn is the current X coordinate of the point and Zm is the coordinate of the associated character on the circle) to Sum of Ln/2^(m-n) starting at n=0, where Ln is the coordinate of the associated letter on the circle, n is the position of the letter in the message to be encoded (where the first letter is point 0) and m is the length of the message.
5) Encoding the message to give X and Y coordinates of the final point (which, given that the cipher and length of the message are known, can be used to decode the entire message)
6) A function to display the correct number of decimal places. Given that the smallest decimal will be in the order of 1/(2^m) where m is the length of the message, the function sets and prints the final coordinates to m number of decimal places
