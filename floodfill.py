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

def fill(image,x,y,origColor,newColor)：
    if not inArea(image,x,y):
        return
    


if __name__ == '__main__':
    # nums = [i for i in range(10,0,-1)]
    # print(nums)
    # print(subarraysum(nums,9))
    num1 = '12'
    num2 = '32'
    result = multiply(num1,num2)
    print(result)