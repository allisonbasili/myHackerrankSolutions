#  You are given  scores. Store them in a list and find the score of the runner-up.

# my solution

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    m = max(arr)
    l = -9999999
    for i in range(0,n):
        if arr[i]<m and arr[i] > l:
            l = arr[i]
    
    print(l)