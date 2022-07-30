#%% libraries

import copy 


##################################################################3
#%%
def read_convert_data(filename):
    mat_adj = []
    with open(filename, 'r') as f :
        for i,line in enumerate(f) : 
            if not i :
                continue
            row = list(line.rstrip())
            row = list(filter(lambda a: a != ' ', row))
            row = [int(i) for i in row]
            row = [ i if i else float('inf') for i in row]
            mat_adj.append(row)
        
    return mat_adj


#######################################################################
#%%
#chaque element en position (i,j) represente le plus court chemin entre i et j
def display_chemins(chemins): 
    n=len(chemins)
    print(n)
    for i in range(n):
        for j in range(n):
            print(chemins[i][j], end=" ")
        
        print("\n")
# %%

##########################################################################
def floyd_warshall(W0):
    W = copy.deepcopy(W0)

    n = len(W0)
    
    #initiation de la matrice des chemins plus courts 
    chemins = copy.deepcopy(W0)


    for i in range(n):
        for j in range(n):
            if chemins[i][j] != float('inf'):
                chemins[i][j] = [i,j]
    
    # Floyd-Warshall
    for k in range (n):
        for i in range(n):
            for j in range(n):
               if W[i][j] > W[i][k] + W[k][j]:        
                     W[i][j] = W[i][k] + W[k][j]
                     chemins[i][j] = chemins[i][k] + chemins[k][j][1:]
   
  
    return W, chemins

#############################################################################
# %%

W = read_convert_data('matrices/mat5.dat')
w,chemins = floyd_warshall(W)

display_chemins(chemins)
# %%
