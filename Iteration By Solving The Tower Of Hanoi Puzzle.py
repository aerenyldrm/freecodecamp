number_of_disk = 3
maximum_move_number = 2 ** number_of_disk - 1
rod_pool = {
    'A': list(range(number_of_disk, 0, -1)),
    'B': [],
    'C': []
}
# above is to construct initial state
def moveAccordingly(a_rod, other_rod):
    forward = False
    if not rod_pool[other_rod]:
        forward = True
    elif rod_pool[a_rod] and rod_pool[a_rod][-1] < rod_pool[other_rod][-1]:
        forward = True
    else: pass
    if forward:
        print(f"Moving disk {rod_pool[a_rod][-1]} from {a_rod} to {other_rod}")
        rod_pool[other_rod].append(rod_pool[a_rod].pop())
    else:
        print(f"Moving disk {rod_pool[other_rod][-1]} from {other_rod} to {a_rod}")
        rod_pool[a_rod].append(rod_pool[other_rod].pop())
# above is a function to bring movement accordingly
def move(maximum_move_count, source, auxiliary, target):
    print('\n', rod_pool,'\n', sep='')
    for count in range(maximum_move_count):
        remainder = (count + 1) % 3
        if remainder == 1:
            if maximum_move_count % 2 != 0:
                print(f"Move {count + 1} is valid between {source} and {target}")
                moveAccordingly(source, target)
            else:
                print(f"Move {count + 1} is valid between {source} and {auxiliary}")
                moveAccordingly(source, auxiliary)
        elif remainder == 2:
            if maximum_move_count % 2 != 0:
                print(f"Move {count + 1} is valid between {source} and {auxiliary}")
                moveAccordingly(source, auxiliary)
            else:
                print(f"Move {count + 1} is valid between {source} and {target}")
                moveAccordingly(source, target)
        elif remainder == 0:
            print(f"Move {count + 1} is valid between {auxiliary} and {target}")
            moveAccordingly(auxiliary, target)
        else: pass
        print(rod_pool, '\n', sep='')
# above is a function which is essential procedure
move(maximum_move_number, 'A', 'B', 'C')
# above is to call function