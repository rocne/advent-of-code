from typing import List

def main():
    print("running day 2")
    count: int = 0
    with open("../input.txt", "r") as f:
        for line in f:
            parts: List[int] = list(map(int, line.split(" ")))
            if is_safe(parts):
                count += 1
        print(f"count: {count}")

def is_safe(data: List[int]) -> bool:
    delta: int = data[1] - data[0]
    row_is_increasing: bool = delta > 0
    if abs(delta) <= 0 or abs(delta) > 3:
        return False
    for i in range(1, len(data)):
        delta = data[i] - data[i - 1]
        curr_is_increasing: bool = delta > 0
        if curr_is_increasing != row_is_increasing:
            return False
        if abs(delta) <= 0 or abs(delta) > 3:
            return False
    return True



if __name__ == "__main__":
    main()