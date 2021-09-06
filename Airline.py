
"""
Chef has 3 bags that she wants to take on a flight. They weigh A, B, and C kgs respectively. She wants to check-in exactly two of these bags and carry the remaining one bag with her.
The airline restrictions says that the total sum of the weights of the bags that are checked-in cannot exceed D kgs and the weight of the bag which is carried cannot exceed E kgs.
Find if chef can take all the three bags on the plane.
"""

def SOL():
    T = int(input())
    for i in range(T):
        A,B,C,D,E = map(int,input().split())
        M = min(A,B,C)
        N = A + B + C - M
        if(M>E):
            s = "NO"
        else:
            if(N>D):
                s = "NO"
            else:
                s = "YES"
        print(s)
SOL()
