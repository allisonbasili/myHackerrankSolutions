##The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
##Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# answer!
n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

total = sum(student_marks[query_name])
average = total/3
print("%.2f"%(average))