"""
Advent of Code 2024 Day 1
"""
def main():
    with open("input.txt", "r") as f:
        data = f.readlines()
    
    data = [line_data.split() for line_data in data]
    list1, list2 = zip(*data)
    
    list1 = sorted(list1)
    list2 = sorted(list2)

    differences = [abs(int(a) - int(b)) for a,b in zip(list1, list2)]
    print(sum(differences))

if __name__ == "__main__":
    main()