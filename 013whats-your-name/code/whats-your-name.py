#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last

#answer as learned from lecture

def print_full_name(first, last):
    subString1 = "Hello "
    outputString = subString1 + first
    outputString = outputString + " " + last
    outputString = outputString + "! You just delved into python."
    print(outputString)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)