
def makeCompatable(pre):
    # temp = ([pos for pos, char in enumerate(pre) if char == ' '])
    # print(temp[0])
    # print(pre.find(' '))

    post = ''
    if (pre.count(' ') == 1):
        temp = list(pre)
        temp[pre.find(' ')] = '-'
        post = ''.join(temp)
        return post
    else:
        temp = ([pos for pos, char in enumerate(pre) if char == ' '])
        tempList = list(pre)
        tempList.pop(temp[0])
        tempList[temp[1] - 1] = '-'
        post = ''.join(tempList)
        return post

        

# makeCompatable('Kansas City Chiefs')