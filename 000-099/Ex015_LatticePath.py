"""DEFINITION
https://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?
"""
import time;
ts = time.time()

GridDimension = 20

BufferList = [1]
List = [1]

Sol = 0
for i in range(GridDimension):

    BufferList = List.copy()
    List.append(1)
    for j in range(1, len(BufferList),1):
        List[j] = BufferList[j-1] + BufferList[j]
    BufferList = List.copy()
    List.append(1)
    for j in range(1, len(BufferList),1):
        List[j] = BufferList[j-1] + BufferList[j]
    Sol = max(List)
    
ts = time.time() - ts
print("Number of possible path for a Grid of {",GridDimension,";",GridDimension,"} is :",Sol)
print("Time Elapsed :",ts,"s")

