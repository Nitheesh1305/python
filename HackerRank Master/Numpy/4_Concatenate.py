import numpy

inp = input().split()
N, M, P = map(int, inp)

running_list = []

for i in range(0, N+M):
    running_list.append([x for x in input().split()])

print(numpy.array(running_list, int))