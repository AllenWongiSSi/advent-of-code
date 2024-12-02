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
    " day 1 part 1 answer "
    print(f"Total Distance = {sum(differences)}")
    " day 1 part 2 answer "
    similarity_score_list = [list2.count(l1_element) * int(l1_element) for l1_element in list1]
    print(f"Sum of Similarity Score = {sum(similarity_score_list)}")

if __name__ == "__main__":
    main()