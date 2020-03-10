# Function for Fourier Transformation of CGR data followed by finding the absolute of signals.
# Obtaining real number vectors allows issues associated with complex numbers to be avoided.

import numpy as np
from sympy import *
import sys

def CGRfftAbs(X_coordinates,Y_coordinates):
    # Detect if correct data has been entered
    if len(X_coordinates) != len(Y_coordinates):    
        sys.exit("""Error! Length of X and Y lists are not equal.
                Check correct lists are being passed and try again.""")
        # Break and provide error message in case incorrect data

    # Combining X and Y coordinates into a complex number Z for 1D fft
    Z_coordinates = [] # initiate Z coordinates list
    #Combine X and Y
    for i in range(len(X_coordinates)):
        Z = X_coordinates[i] + I*Y_coordinates[i]
        Z_coordinates.append(Z)
    
    # 1D fft
    FFT_signal = np.fft.fft(Z_coordinates)
    
    #Obtaining absolute values
    Absfft = abs(FFT_signal)

    return Absfft


# Test case: correct case
X = [-1, 0.3, 0.1]
Y = [0.2, -0.4, 0.9]
Absfft_signal = CGRfftAbs(X,Y)


# Test case: error case
X_error = [-1, 0.3, 0.1]
Y_error = [0.2, -0.4, 0.9, 4] #longer than X_error
Absfft_error = CGRfftAbs(X_error,Y_error)


