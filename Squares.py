#!/usr/bin/env python
# coding: utf-8

# In[1]:


def recursivepattern(var, matrix, n=1):
    temp = str([str(i) for i in matrix])
    nor = len(matrix)//2
    for i in range(nor - var, nor + var+1):
        for j in range(nor - var, nor + var+1):
            if abs(i-nor) + abs(j-nor) >= var:
                matrix[i][j] = '*'
            else:
                matrix[i][j] = ' '
    if temp == str([str(i) for i in matrix]):
        for i in matrix:
            for j in i:
                print(j, end=" ")
            print("")
        return matrix
    else:
        recursivepattern(var//2, matrix, n+1)


# In[2]:


if __name__ == '__main__':
    n = int(input("Enter the number: "))
    matrix = [[' ' for i in range(2**n+1)] for j in range(2**n+1)]
    recursivepattern(2**(n-1), matrix)


# In[ ]:



