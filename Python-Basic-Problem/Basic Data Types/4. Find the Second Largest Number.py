if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = set(arr)     #set is python data type which removes all dublicate values.
    max_value = max(arr)
    arr.remove(max_value)
    s_max = max(arr)
    print(s_max)