# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 23:58:52 2021

@author: karthik
"""

import pandas as pd

import os
cwd = os.getcwd()

A_DataFrame = pd.read_csv("Dictionary-in-csv\A.csv", encoding= 'unicode_escape')
B_DataFrame = pd.read_csv("Dictionary-in-csv\B.csv", encoding= 'unicode_escape')
C_DataFrame = pd.read_csv("Dictionary-in-csv\C.csv", encoding= 'unicode_escape')
D_DataFrame = pd.read_csv("Dictionary-in-csv\D.csv", encoding= 'unicode_escape')
E_DataFrame = pd.read_csv("Dictionary-in-csv\E.csv", encoding= 'unicode_escape')
F_DataFrame = pd.read_csv("Dictionary-in-csv\F.csv", encoding= 'unicode_escape')
G_DataFrame = pd.read_csv("Dictionary-in-csv\G.csv", encoding= 'unicode_escape')
H_DataFrame = pd.read_csv("Dictionary-in-csv\H.csv", encoding= 'unicode_escape')
I_DataFrame = pd.read_csv("Dictionary-in-csv\I.csv", encoding= 'unicode_escape')
J_DataFrame = pd.read_csv("Dictionary-in-csv\J.csv", encoding= 'unicode_escape')
K_DataFrame = pd.read_csv("Dictionary-in-csv\K.csv", encoding= 'unicode_escape')
L_DataFrame = pd.read_csv("Dictionary-in-csv\L.csv", encoding= 'unicode_escape')
M_DataFrame = pd.read_csv("Dictionary-in-csv\M.csv", encoding= 'unicode_escape')
N_DataFrame = pd.read_csv("Dictionary-in-csv\\N.csv", encoding= 'unicode_escape')
O_DataFrame = pd.read_csv("Dictionary-in-csv\O.csv", encoding= 'unicode_escape')
P_DataFrame = pd.read_csv("Dictionary-in-csv\P.csv", encoding= 'unicode_escape')
Q_DataFrame = pd.read_csv("Dictionary-in-csv\Q.csv", encoding= 'unicode_escape')
R_DataFrame = pd.read_csv("Dictionary-in-csv\R.csv", encoding= 'unicode_escape')
S_DataFrame = pd.read_csv("Dictionary-in-csv\S.csv", encoding= 'unicode_escape')
T_DataFrame = pd.read_csv("Dictionary-in-csv\T.csv", encoding= 'unicode_escape')
U_DataFrame = pd.read_csv("Dictionary-in-csv\\U.csv", encoding= 'unicode_escape')
V_DataFrame = pd.read_csv("Dictionary-in-csv\V.csv", encoding= 'unicode_escape')
W_DataFrame = pd.read_csv("Dictionary-in-csv\W.csv", encoding= 'unicode_escape')
X_DataFrame = pd.read_csv("Dictionary-in-csv\X.csv", encoding= 'unicode_escape')
Y_DataFrame = pd.read_csv("Dictionary-in-csv\Y.csv", encoding= 'unicode_escape')
Z_DataFrame = pd.read_csv("Dictionary-in-csv\Z.csv", encoding= 'unicode_escape')


A_DataFrame.columns = ["WTM"]
B_DataFrame.columns = ["WTM"]
C_DataFrame.columns = ["WTM"]
D_DataFrame.columns = ["WTM"]
E_DataFrame.columns = ["WTM"]
F_DataFrame.columns = ["WTM"]
G_DataFrame.columns = ["WTM"]
H_DataFrame.columns = ["WTM"]
I_DataFrame.columns = ["WTM"]
J_DataFrame.columns = ["WTM"]
K_DataFrame.columns = ["WTM"]
L_DataFrame.columns = ["WTM"]
M_DataFrame.columns = ["WTM"]
N_DataFrame.columns = ["WTM"]
O_DataFrame.columns = ["WTM"]
P_DataFrame.columns = ["WTM"]
Q_DataFrame.columns = ["WTM"]
R_DataFrame.columns = ["WTM"]
S_DataFrame.columns = ["WTM"]
T_DataFrame.columns = ["WTM"]
U_DataFrame.columns = ["WTM"]
V_DataFrame.columns = ["WTM"]
W_DataFrame.columns = ["WTM"]
X_DataFrame.columns = ["WTM"]
Y_DataFrame.columns = ["WTM"]
Z_DataFrame.columns = ["WTM"]


A_DataFrame = A_DataFrame.append(B_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(C_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(D_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(E_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(F_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(G_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(H_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(I_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(J_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(K_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(L_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(M_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(N_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(O_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(P_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(Q_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(R_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(S_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(T_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(U_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(V_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(W_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(X_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(Y_DataFrame, ignore_index = True)
A_DataFrame = A_DataFrame.append(Z_DataFrame, ignore_index = True)


# Error in entry number 146516, deleting row 146516
A_DataFrame = A_DataFrame.drop(146516)

A_DataFrame["word"]  = A_DataFrame.apply(lambda word : word["WTM"].split('(')[0], axis = 1)
A_DataFrame["wtype"] = A_DataFrame.apply(lambda word : word["WTM"].split("(")[1].split(")")[0], axis = 1) 
A_DataFrame["meaning"] = A_DataFrame.apply(lambda word : word["WTM"].split(')')[1], axis = 1)
A_DataFrame.drop(["WTM"] , axis=1, inplace=True)
