def checking(row, col) :
    if(((col > 72) | (col < 65)) | ((row > 8) | (row < 1))) :
        return False
    else :
        return True

place = input("Input Chess piece [A1-H8]: " ).upper()

col = ord(place[0])
row = int(place[1:])
if(not checking(row, col)) :
    print("Chess piece should be positioned from A1 to H8")
else :
    going = 0
    if(checking(row-1, col-2)) :
        going += 1
    if(checking(row-2, col-1)) :
        going += 1
    if(checking(row-2, col+1)) :
        going += 1
    if(checking(row-1, col+2)) :
        going += 1
    if(checking(row+1, col+2)) :
        going += 1
    if(checking(row+2, col+1)) :
        going += 1
    if(checking(row+2, col-1)) :
        going += 1
    if(checking(row+1, col-2)) :
        going += 1
    print(going)