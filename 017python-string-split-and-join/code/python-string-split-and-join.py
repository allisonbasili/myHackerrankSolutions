# promt: You are given a string. 
# Split the string on a " " (space) 
# delimiter and join using a - hyphen.

def split_and_join(line):
    out = line.split(); # Command splits line
    out = "-".join(out) # Joins line at splits with "-"
    return(out); #returns function

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)