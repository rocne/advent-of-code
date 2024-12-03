from typing import List

def main():
    print("running day 1")
    left: List[int] = []
    right: List[int] = []
    with open("../input.txt", "r") as f:
        for line in f:
            parts: List[str] = line.split("   ")
            left.append(int(parts[0].strip()))
            right.append((int(parts[1].strip())))
    left.sort()
    right.sort()

    sum: int = 0
    for pair in zip(left, right):
        sum += abs(pair[0] - pair[1])
    print(sum)

if __name__ == "__main__":
    main()