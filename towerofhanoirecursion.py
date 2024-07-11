number_of_disk = 3
a_rod = list(range(number_of_disk, 0, -1))
other_rod = []
another_rod = []
print(f"\nINITIAL STATE IS {a_rod} {other_rod} {another_rod}\n")
def move(disk_count, source, auxiliary, target):
    if disk_count <= 0:
        return 
    else:
        move(disk_count - 1, source, target, auxiliary)
        target.append(source.pop())
        print(a_rod, other_rod, another_rod, '\n')
        move(disk_count - 1, auxiliary, source, target)
move(number_of_disk, a_rod, other_rod, another_rod)