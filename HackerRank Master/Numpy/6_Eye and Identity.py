import numpy
dimensions = tuple(map(int, input().split()))
print(numpy.eye(dimensions[0], dimensions[1], k=0))

#For Excution in Hacker Rank 
#.replace('1',' 1').replace('0',' 0'))
#as in expected output every eliment is shifted one unit right.
# thats why we have to shift every 1 & 0 one unit right