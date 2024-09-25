#!/usr/bin/python3
'''Given an n x n 2D matrix, rotate it 90 degrees clockwise'''

def rotate_2d_matrix(matrix):
    n = len(matrix)

    for s in range(n):
        for t in range(s, n):
            matrix[s][t], matrix[t][s] = matrix[t][s], matrix[s][t]

    for s in range(n):
        matrix[s].reverse()
