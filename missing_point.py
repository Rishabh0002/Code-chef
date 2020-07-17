"""
Chef has N axis-parallel rectangles in a 2D Cartesian coordinate system.
These rectangles may intersect, but it is guaranteed that all their 4N vertices are pairwise distinct.
Unfortunately, Chef lost one vertex, and up until now, none of his fixes have worked
(although putting an image of a point on a milk carton might not have been the greatest idea after all…).
Therefore, he gave you the task of finding it! You are given the remaining 4N−1 points and you should find the missing one input.
"""


x = []
y = []
miss_x = []
miss_y = []

T = int(input())
if(T<=100):
    for i in range(T):
        N = int(input())
        if(N>=1 and N<=200000):
            for j in range((N*3)+(N-1)):
                ele_x = int(input())
                ele_y = int(input())
                x.append(ele_x)
                y.append(ele_y)

            for item_x in x:
                count = 0
                for m in range(len(x)):
                    if item_x == x[m]:
                        count = count+1
                if(count % 2 != 0 and item_x not in miss_x):
                    miss_x.append(item_x)
            for item_y in y:
                count = 0
                for m in range(len(y)):
                    if item_y == y[m]:
                        count = count+1
                if(count % 2 != 0 and item_y not in miss_y):
                    miss_y.append(item_y)
            print(miss_x,miss_y)






                    




