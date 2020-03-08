# Encoding
Methods of encoding messages (or any sequence of more than 4 possible states) using a circular Chaos Game Representation (CGR) algorithm.
Important note: Unlike square CGR, use of symbolic python (SymPy) is essential for accuracy of the circular chaos game encoding method 
due to the use of irrational numbers. 

text_to_CGR_coordinates.py returns all of the CGR coordinates for an encoded message

text_to_final_CGR_coordinate.py returns only the final X and Y coordinates of an encoded message


Both 
   1) Creating ciphers by randomising a list of characters

   2) Assigning each character in a message with a point (Ln) on a radius 1 circle (x^2 + y^2 = 1). 
      These values are used to determine the final X and Y values (the encoded message) in step 3. 

   3) Encoding of the message using the circular Chaos Game algorithm:
      Note: text_to_CGR_coordinates.py uses the original algorithm: 
            Xn+1 = (Xn + Ln)/2     where Xn is the current X coordinate of the point 
                                   and Ln is the coordinate of the associated character on the circle

            text_to_final_CGR_coordinate.py uses summation of the algorithm to find final X and Y values:
            Xm = Sum of Ln/2^(m-n)     starting at n=0, where Ln is the coordinate of the associated 
                                       letter on the circle, n is the position of the letter in the 
                                       message to be encoded (where the first letter is point 0) and 
                                       m is the length of the message.
 
The Speed_testing folder contains speed test comparisons of the summation method vs original algorithm.
Text used is first 2,490 characters of Frankenstein by Mary Shelley, used under the Project Gutenberg License.  