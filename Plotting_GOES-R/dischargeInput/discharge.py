import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def lockandload(fileName):
    #LOAD CSV
    filename = "frxst_pts_out_1p00.csv"
    df = pd.read_csv(filename)
    data = df.values
    return data


def plot(data):
    #PLOT THE STUFF


stuff = lockandload()
