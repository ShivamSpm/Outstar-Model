"""

Name: Shivam Mahajan
id: spm9398

"""


from linearAlgebra import *

theta = [0.4,0.3,0.2,0.1]
x = [0]
wOFi = [0.51, 0.52, 0.53, 0.54]
xOFi = [0.7, 0.75, 0.78, 0.79]

xB = [0]
wOFiB = [0.51, 0.52, 0.53, 0.54]
xOFiB = [0.7, 0.75, 0.78, 0.79]

def I0(index):

    if index == 1:
        return 2

    elif index % 10 == 0 or index % 10 == 9:
        return 2

    return 0

def inputsIb(i,index):
    if i==1:
        return 0
    elif i == 2:
        return 0.8

    elif i%20 == 1:


        if index == 0:
            return 0.8
        elif index == 1:
            return 0.6
        elif index==2:
            return 0.4

        else:
            return 0.2


    elif i%20 == 11:

        if index == 0:
            return 0.5
        elif index == 1:
            return 0.5
        elif index==2:
            return 0.3

        else:
            return 0.7

    else:
        return 0



def I(index):

    if index==3:
        return 2


    elif index != 1:
        if index % 10 == 1 or index % 10 == 2:
            return 2

    return 0

def inputsI(i,index):
    value = I(index)
    return value * theta[i]


def eulerOutStar(h,tb,A,x0, F):
    t = 0
    # x = x0
    c = 0
    x0Lst = []
    XiList = []
    WiList = []
    timeStepLst = []
    while t < tb:

        l = []
        for i in range(len(F)):
            # l.append(x[i])
            if i==0:
                x[i] = x[i] + h * (F[i](x, t) + I0(c))
            elif i > 0 and i < 5:

                xOFi[i-1] = xOFi[i-1] + h * (F[i](x, t) + x[0]*wOFi[i-1] + inputsI(i-1,c))

                # print(inputsI(i - 1, t))

            else:
                wOFi[i-5] = wOFi[i-5] + h * x[0]*(F[i](x, t) + xOFi[i-5])

        if c%100 == 0:
            timeStepLst.append(c)
            lstX=[]
            lstWt = []
            x0Lst.append(x[0])
            for index in range(len(xOFi)):
                lstX.append(xOFi[index]/sum(xOFi))

            for jndex in range(len(wOFi)):
                lstWt.append(wOFi[jndex]/sum(wOFi))
            WiList.append(lstWt)
            XiList.append(lstX)

        c+=1

        t = t + h

    return x0Lst, XiList, WiList,timeStepLst

def eulerOutStarBpart(h,tb,A,x0, F):
    t = 0
    # x = x0
    c = 0
    x0Lst = []
    XiList = []
    WiList = []
    timeStepLstB = []
    while t < tb:

        l = []
        for i in range(len(F)):
            # l.append(x[i])
            if i == 0:
                xB[i] = xB[i] + h * (F[i](x, t) + I0(c))

            elif i > 0 and i < 5:

                xOFiB[i - 1] = xOFiB[i - 1] + h * (F[i](x, t) + xB[0] * wOFiB[i - 1] + inputsIb(c, i-1))


            else:
                wOFiB[i - 5] = wOFiB[i - 5] + h * xB[0] * (F[i](x, t) + xOFiB[i - 5])

        if c % 100 == 0:
            timeStepLstB.append(c)

            lstX = []
            lstWt = []

            x0Lst.append(xB[0])

            for index in range(len(xOFiB)):
                lstX.append(xOFiB[index] / sum(xOFiB))

            for jndex in range(len(wOFiB)):
                lstWt.append(wOFiB[jndex] / sum(wOFiB))
            WiList.append(lstWt)
            XiList.append(lstX)

        c += 1
        t = t + h

    return x0Lst, XiList, WiList, timeStepLstB

def main():

    functions = [lambda x,t: -5 * x[0],lambda x,t: -5 * xOFi[0],lambda x,t: -5 * xOFi[1],lambda x,t: -5 * xOFi[2]
                 ,lambda x,t: -5 * xOFi[3],lambda x,t: -.1 * wOFi[0],lambda x,t: -.1 * wOFi[1],lambda x,t: -.1 * wOFi[2],lambda x,t: -.1 * wOFi[3]]

    functionsB = [lambda x, t: -5 * xB[0], lambda x, t: -5 * xOFiB[0], lambda x, t: -5 * xOFiB[1], lambda x, t: -5 * xOFiB[2]
        , lambda x, t: -5 * xOFiB[3], lambda x, t: -.1 * wOFiB[0], lambda x, t: -.1 * wOFiB[1], lambda x, t: -.1 * wOFiB[2],
                 lambda x, t: -.1 * wOFiB[3]]

    x0Lst, XiList,WiList,timeStepLst = eulerOutStar(0.1,1000,update, [0],functions)
    x0LstB, XiListB, WiListB, timeStepLstB = eulerOutStarBpart(0.1, 1000, update, [0], functionsB)
    xwLst = XiList
    xwLstB = XiListB
    for index in range(len(WiList)):
        for jndex in range(len(WiList[0])):

            xwLst[index].append(WiList[index][jndex])
    for ind in range(len(WiListB)):
        for jnd in range(len(WiListB[0])):

            xwLstB[ind].append(WiListB[ind][jnd])

    plt.plot(timeStepLst, xwLst)
    plt.title('Question 1(a)')
    plt.legend(['X1','X2','X3','X4','W1','W2','W3','W4'],loc="best")
    plt.show()
    plt.plot(timeStepLstB, xwLstB)
    plt.title('Question 1(b)')
    plt.legend(['X1', 'X2', 'X3', 'X4', 'W1', 'W2', 'W3', 'W4'], loc="best")
    plt.show()


if __name__ == '__main__':
    main()


