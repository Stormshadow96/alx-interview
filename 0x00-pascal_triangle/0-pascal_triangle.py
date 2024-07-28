#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        # Start with a row of 1s
        row = [1] * (i + 1)
        
        # Each element in the row (except for the 1s on the edges) is the sum of the two elements above it
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)
    
    return triangle
