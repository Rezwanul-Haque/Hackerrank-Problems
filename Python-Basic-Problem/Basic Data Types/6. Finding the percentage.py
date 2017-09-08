if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    mark = [i for k,v in student_marks.items() for i in v if k == query_name]
    for i in mark:
        sum += i
    avg = sum / 3
    
    print("%.2f"%avg)   # %.2f for showing 2 places after the decimal point.
