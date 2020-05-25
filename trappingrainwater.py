def fill(x,y):
    fill(x-1,y)
    fill(x+1,y)
    fill(x,y-1)
    fill(x,y+1)


def floodFill(image,row,col,newColor):
    origColor = image[row][col]
    fill(image,row,col,origColor,newColor)
    return image


def inArea(image,x,y):
    return x>=0 and x < len(image) and y >=0 and y <len(image[0])

def fill(image,x,y,origColor,newColor):
    if not inArea(image,x,y):
        return
    if image[x][y] != origColor:
        return

    image[x][y] = -1
    fill(image,x,y+1,origColor,newColor)
    fill(image,x,y-1,origColor,newColor)
    fill(image,x+1,y,origColor,newColor)
    fill(image,x-1,y,origColor,newColor)
    image[x][y] = newColor
    


if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,1,2]]
    image1 = floodFill(image,1,1,3)
    print(image1)