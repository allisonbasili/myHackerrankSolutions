#  You are given  scores. Store them in a list and find the score of the runner-up.

# commented commit 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    m = max(arr) # set max
    l = -9999999 #set min
    for i in range(0,n):
        if arr[i]<m and arr[i] > l:
            l = arr[i] #declare min
    
    print(l)