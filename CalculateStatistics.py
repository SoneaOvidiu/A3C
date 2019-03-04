def readData():
    fil=open("Statistics.txt","r")
    linii=fil.readlines()
    rewardList=[]
    timeList=[]
    for elem in linii:
        linie=elem.split(" ")
        rewardList.append(linie[0])
        timeList.append(linie[1])
    fil.close()
    return rewardList,timeList
def AvaregeLastNSteps(steps,List):
    if steps<len(List):
        lista=List[(len(List)-steps):]
        for index in range( len(lista)):
            lista[index]=float(lista[index])
        avarege=sum(lista)/steps
        return avarege
def AvaregeRewardDivTimeNSteps(steps,rewardList,timeList):
    if steps<len(rewardList):
        rewardAvg=AvaregeLastNSteps(steps,rewardList)
        timeAvg=AvaregeLastNSteps(steps,timeList)
        avarege=timeAvg/rewardAvg
        return avarege
def greatestElement(List):
    for index in range(len(List)):
        List[index]=float(List[index])
    return max(List)
def processData():
    reward,time=readData()
    steps=10
    avg=AvaregeLastNSteps(steps,reward)
    avgDivTime=AvaregeRewardDivTimeNSteps(steps,reward,time)
    fisier=open("ProcesedData.txt","a")
    message="""Avarege reward from last %i steps is: %d
The avarege time needed to score a point from the last %i steps is: %d
The greatest reward recorded was: %d
""" % (steps,avg,steps,avgDivTime,greatestElement(reward))
    fisier.write(message)
    fisier.close()