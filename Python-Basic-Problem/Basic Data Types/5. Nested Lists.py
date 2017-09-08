if __name__ == '__main__':
    marksheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name, score])
    shigh = sorted(list(set([marks for name, marks in marksheet])))[1]
    print("\n".join([name for name,mark in sorted(marksheet) if mark == shigh]))