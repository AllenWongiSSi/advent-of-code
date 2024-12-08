import os

enum = {
    'ASC': 1,
    'DESC': -1,
    'SAME': 0
}
def check_safe(list_row):
    track_sign = enum['SAME']
    if (list_row[0] > list_row[1]):
        # descending order
        track_sign = enum['DESC']
    elif (list_row[0] < list_row[1]):
        # ascending order
        track_sign = enum['ASC']
    else:
        # same number
        return False
    for i in range(1, len(list_row)):
        if (list_row[i-1] > list_row[i] and track_sign == enum['ASC']):
            return False
        elif (list_row[i-1] < list_row[i] and track_sign == enum['DESC']):
            return False
        else:
            diff = list_row[i-1] - list_row[i]
            if (abs(diff) == 0 or abs(diff) > 3):
                return False
    return True

        
def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    nums = [list(map(int, line.split())) for line in lines]
    safe_count = [check_safe(num) for num in nums]
    print(f"Safe count: {safe_count.count(True)}")
    return 0

if __name__ == '__main__':
    main()