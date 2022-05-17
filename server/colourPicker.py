import pandas as pd 
import numpy as np
from skimage import io, color
import matplotlib.pyplot as plt



def find_closest_colour(input_data):
    df = pd.read_csv('color_names.csv')
    ref = input_data.lstrip('#')
    ref_RGB = tuple(int(ref[i:i+2], 16) for i in (0, 2, 4))
    global L1
    global A1
    global B1
    L1 , A1 , B1 = color.rgb2lab(ref_RGB)
    df['lab'] = df.apply(getLAB,axis=1)
    df['dE_94'] = df.apply(getDiff,axis=1)
    df = df.sort_values(by='dE_94', ascending=True).reset_index()
    return df["Name"].get(0) , df["Hex (24 bit)"].get(0)

def getLAB(row):
    R = row['Red (8 bit)']
    G = row['Green (8 bit)']
    B = row['Blue (8 bit)']
    return color.rgb2lab((R,G,B))

def getDiff(row):
    # Constants 
    K_1 = 0.0045
    K_2 = 0.015
    K_L = 1
    K_C = 1
    K_H = 1
    
    L2 = row['lab'][0]
    A2 = row['lab'][1]
    B2 = row['lab'][2]
    
    dL = L1 - L2
    C1 = np.sqrt(A1**2 + B1**2)
    C2 = np.sqrt(A2**2 + B2**2)
    dC = C1 - C2
    dA = A1 - A2
    dB = B1 - B2
    S_L = 1
    S_C = 1 + K_1 * C1
    S_H = 1 + K_2 * C1
    dH = np.sqrt(dA**2 + dB**2 - dC**2)
    
    return np.sqrt(((dL)/(K_L*S_L))**2+((dC)/(K_C*S_C))**2+((dH)/(K_H*S_H))**2)