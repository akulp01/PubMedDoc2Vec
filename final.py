from lateralCount import *
def finalFunction():
    from asyncio.windows_events import NULL
    import pandas as pd
    import numpy as np

    resultArr = [0,0,0]
    specimen = "(specimen)"
    specimenList = []
    termFile = pd.read_csv('C:\\Users\\Will\\Desktop\\Snowmed\\sct2_Description_Snapshot-en_INT_20210731.txt', sep='\t')
    for term in termFile.index:
        if specimen in str(termFile.iloc[term, 7]):
            if termFile.iloc[int(term), 6] == 900000000000003001:
                specimenList.append(term)

    chosenList = np.random.choice(specimenList, 50, replace=False)
    for x in chosenList:
        print(termFile.iloc[x, 7])
        currentTermConceptId = termFile.iloc[x, 4]
        for y in chosenList:
            print(termFile.iloc[y][0])
            compareTermConceptId = termFile.iloc[y, 4]
            if currentTermConceptId != compareTermConceptId:
                returnVal = lateralAnalysisFinal(currentTermConceptId, compareTermConceptId)
                match returnVal:
                    case 1:
                        resultArr[0] += 1
                    case 2:
                        resultArr[1] += 1
                    case 3:
                        resultArr[2] += 1
    
    print(resultArr)


finalFunction()