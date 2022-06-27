from collections import deque

egg_sizes = deque(int(x) for x in input().split(", "))
paper_sizes = [int(x) for x in input().split(", ")]

boxes = 0
current_box = 50
current_box_count = 0
while egg_sizes and paper_sizes:
    box_size = 50
    first_egg = egg_sizes[0]
    last_paper = paper_sizes[-1]
    while egg_sizes and paper_sizes:
        first_egg = egg_sizes[0]
        last_paper = paper_sizes[-1]
        if first_egg <= 0:
            egg_sizes.popleft()
            break

        if first_egg == 13:
            egg_sizes.popleft()
            paper_sizes[-1] = paper_sizes[0]
            paper_sizes[0] = last_paper
            break


        sum = first_egg + last_paper

        if sum <= current_box:
            current_box -= sum
            egg_sizes.popleft()
            paper_sizes.pop()
            current_box_count += 1
        elif sum <= box_size:
            current_box = 50
            current_box -= sum
            egg_sizes.popleft()
            paper_sizes.pop()
            boxes += 1
        else:
            egg_sizes.popleft()
            paper_sizes.pop()

boxes += current_box_count

if boxes >= 1:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_sizes:
    print(f"Eggs left: {', '.join(str(x) for x in egg_sizes)}")

if paper_sizes:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_sizes)}")
