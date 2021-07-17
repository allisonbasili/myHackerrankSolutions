#Ms. Gabriel Williams is a botany professor at District College. 
# ne day, she asked her student Mickey to compute the average 
# of all the plants with distinct heights in her greenhouse.
#Complete the average function in the editor below.

## completed challenge 3rd commit

def average(array):
    return sum(set(array))/len(set(array))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)