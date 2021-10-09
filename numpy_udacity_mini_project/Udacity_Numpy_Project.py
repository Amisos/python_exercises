# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:44:58 2021

@author: MCanA
"""
# import NumPy into Python
import numpy as np

# Create a 1000 x 20 ndarray with random integers in the half-open interval [0, 1)*5000
X=np.random.rand(1000,20)*5000


# print the shape of X
print(X.shape)
# %%

# Average of the values in each column of X
X_avarage=X.mean(0)
# Standard Deviation of the values in each column of X
X_std=X.std(0)


# Print the shape of ave_cols
print("shape of X_avarage ",X_avarage.shape)
# Print the shape of std_cols
print("shape of X_std ",X_std.shape)
# %%

#copy of X(which will be mean normalized)
X_norm=X.copy()

#mean normalization (x-mean)/std
for each in np.arange(X_norm.shape[1]):
    X_norm[:,each]=(X_norm[:,each]-X_avarage[each])/X_std[each]
    

# Print the average of all the values of X_norm
X_norm_avarage=X_norm.mean()
print("avarage of X_norm ",X_norm_avarage)

# Print the average of the minimum value in each column of X_norm
X_norm_min=X_norm.min()
print("minimum of X_norm ",X_norm_min)

# Print the average of the maximum value in each column of X_norm
X_norm_max=X_norm.max()
print("maximum of X_norm ",X_norm_max)
# %%

# We create a random permutation of integers 0 to 1000(X_norm.shape[0] gives number of rows)
random_indices= np.random.permutation(X_norm.shape[0])
#shuffle X_norm(rows/examples) with random_indices
X_shuffled=X_norm[random_indices,:]


#split X_shuffled into three parts(X_train,X_crossVal,X_test)
X_shuffled_split=np.vsplit(X_shuffled,(600,800))

# Create a Training Set (600 row)
X_train =X_shuffled_split[0]

# Create a Cross Validation Set (200 row)
X_crossVal =X_shuffled_split[1]

# Create a Test Set (200 row)
X_test =X_shuffled_split[2]



# Print the shape of X_train
print("shape of X_train ",X_train.shape)

# Print the shape of X_crossVal
print("shape of X_crossVal ",X_crossVal.shape)

# Print the shape of X_test
print("shape of X_test ",X_test.shape)