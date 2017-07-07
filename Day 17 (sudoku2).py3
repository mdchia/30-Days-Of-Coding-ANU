def sudoku2(grid):
    # helpers
    def has_dupes(l):
        l = list(filter(lambda x: x!='.', l))
        #print(l)
        no_dupes = set(l)
        if len(l) == len(no_dupes):
            return False
        return True
    def get_box(x,y):
        coords={1:1,2:1,3:1,4:2,5:2,6:2,7:3,8:3,9:3}
        x=coords[x]
        y=coords[y]
        box_list={(1,1):1,(1,2):2,(1,3):3,(2,1):4,(2,2):5,
                  (2,3):6,(3,1):7,(3,2):8,(3,3):9}
        return box_list[(x,y)]
    # vars
    boxes={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    columns=list(map(list, zip(*grid)))
    for column in columns:
        if has_dupes(column):
            return False
    for y in range(9):
        row=grid[y]
        if has_dupes(row):
            return False
        for x in range(9):
            item=row[x]
            boxes[get_box(y+1,x+1)].append(item)
    #print(boxes.values())
    for box in boxes.values():
        if has_dupes(box):
            return False
    return True

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

print(sudoku2(grid))
