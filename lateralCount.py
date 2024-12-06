#Input 2 IDs - All Above 90 - With same number parents - check lateral

def in_list(list1, list2, list1a, list2b):
    for i in list1:
        if i not in list2:
            list1a.append(i)
    for i in list2:
        if i not in list1:
            list2b.append(i)
    return True

def parent_Count(conceptId):
    import pandas as pd
    parentCount = 0
    conceptFile = pd.read_csv('C:\\Users\\Will\\Desktop\\Snowmed\\sct2_Concept_Snapshot_INT_20210731.txt', sep='\t')
    relationshipFile = pd.read_csv('C:\\Users\\Will\\Desktop\\Snowmed\\sct2_Relationship_Snapshot_INT_20210731.txt', sep='\t')
    termFile = pd.read_csv('C:\\Users\\Will\\Desktop\\Snowmed\\sct2_Description_Snapshot-en_INT_20210731.txt', sep='\t')
    relationships1 = relationshipFile.index[relationshipFile['sourceId'] == int(conceptId)].tolist()
    for item in relationships1:
        if relationshipFile.iloc[int(item), 2] == 1 and relationshipFile.iloc[item, 7] == 116680003:
            destinationId = relationshipFile.iloc[int(item), 5]
            conceptterms = conceptFile.index[conceptFile['id'] == int(destinationId)].tolist()
            for concept in conceptterms:
                if (conceptFile.iloc[int(concept), 2] == 1):
                    parentCount += 1
    return parentCount

def lateral_Count(conceptId):
    global returnList
    import pandas as pd
    conceptFile = pd.read_csv('C:\\Users\\Will\\Desktop\\Snowmed\\sct2_Concept_Snapshot_INT_20210731.txt', sep='\t')
    relationshipFile = pd.read_csv('C:\\Users\\Will\\Desktop\\Snowmed\\sct2_Relationship_Snapshot_INT_20210731.txt', sep='\t')
    lateralCount = 0
    lateralList = []
    relationships1 = relationshipFile.index[relationshipFile['sourceId'] == int(conceptId)].tolist()
    for item in relationships1:
        if relationshipFile.iloc[int(item), 2] == 1 and relationshipFile.iloc[item, 7] != 116680003:
            destinationId = relationshipFile.iloc[int(item), 5]
            conceptterms = conceptFile.index[conceptFile['id'] == int(destinationId)].tolist()
            for concept in conceptterms:
                if (conceptFile.iloc[int(concept), 2] == 1):
                    lateralCount += 1
                    lateralList.append(int(destinationId))
    returnList = lateralList
    return lateralCount




def lateralAnalysis(conceptId1, conceptId2):
    from asyncio.windows_events import NULL
    import re
    import pandas as pd
    import gensim.downloader as api
    from sklearn.metrics.pairwise import cosine_similarity

    from gensim.test.utils import get_tmpfile
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
    fname = get_tmpfile("C:\\Users\\Will\\Desktop\\meshModel.mod")
    model = Doc2Vec.load(fname) 

    termFile = pd.read_csv('C:\\Users\\Will\\Desktop\\Snowmed\\sct2_Description_Snapshot-en_INT_20210731.txt', sep='\t')

    terms1 = termFile.index[termFile['conceptId'] == int(conceptId1)].tolist()
    terms2 = termFile.index[termFile['conceptId'] == int(conceptId2)].tolist()

    for term in terms1:
        if termFile.iloc[int(term),6] == 900000000000003001:
            term1 = term
            break

    for term in terms2:
        if termFile.iloc[int(term),6] == 900000000000003001:
            term2 = term
            break

    conceptName1 = termFile.iloc[term1, 7]
    conceptName2 = termFile.iloc[term2, 7]

    print(conceptName1)
    print(conceptName2)

    sentences = [str(conceptName1), str(conceptName2)]
    # creates the vectors necessary to compute cosine similarity
    vectors = [model.infer_vector([word for word in sent]).reshape(1, -1) for sent in sentences]

    # compute cosine similarity
    similarity = []
    for i in range(len(sentences)):
        row1 = []
        for j in range(len(sentences)):
            row1.append(cosine_similarity(vectors[i], vectors[j])[0][0])
        similarity.append(row1)
    
    print(similarity[1][0])

    if similarity[1][0] >= .9:
        print("Meets similarity requirement")

        parentCount1 = parent_Count(conceptId1)
        parentCount2 = parent_Count(conceptId2)
        print(parentCount1)
        print(parentCount2)

        if parentCount1 == parentCount2:
            print("Parent counts match")
            lateralCount1 = 0
            lateralCount2 = 0
            lateral1List = []
            lateral2List = []
            returnList = []

            lateralCount1 = lateral_Count(conceptId1)
            lateral1List = returnList
            lateralCount2 = lateral_Count(conceptId2)
            lateral2List = returnList

            if lateralCount1 == lateralCount2 and all(item in lateral1List for item in lateral2List) and all(item in lateral2List for item in lateral1List):
                print("The lateral relationship counts match and all relationships are the same")
            else:
                print("Relationships Uneven")
                list2Miss = []
                list1Miss = []
                in_list(lateral1List, lateral2List, list2Miss, list1Miss)
                print()
                print("First Concept Missing:")
                for conceptId in list1Miss:
                    term = termFile.index[termFile['conceptId'] == int(conceptId)].tolist()
                    conceptName = termFile.iloc[term[0], 7]
                    print(str(conceptId) + "   " + str(conceptName))
                print()
                print("Second Concept Missing:")
                for conceptId in list2Miss:
                    term = termFile.index[termFile['conceptId'] == int(conceptId)].tolist()
                    conceptName = termFile.iloc[term[0], 7]
                    print(str(conceptId) + "   " + str(conceptName))

        else:
            print("Parent counts do not match")
    else:
        print("Does not meet .9 similarity requirement")

#lateralAnalysis(52116001, 52123000)









def lateral_Count(conceptId):
    global returnList
    import pandas as pd
    conceptFile = pd.read_csv('C:\\Users\\Will\\Desktop\\Snowmed\\sct2_Concept_Snapshot_INT_20210731.txt', sep='\t')
    relationshipFile = pd.read_csv('C:\\Users\\Will\\Desktop\\Snowmed\\sct2_Relationship_Snapshot_INT_20210731.txt', sep='\t')
    lateralCount = 0
    lateralList = []
    relationships1 = relationshipFile.index[relationshipFile['sourceId'] == int(conceptId)].tolist()
    for item in relationships1:
        if relationshipFile.iloc[int(item), 2] == 1 and relationshipFile.iloc[item, 7] != 116680003:
            destinationId = relationshipFile.iloc[int(item), 5]
            conceptterms = conceptFile.index[conceptFile['id'] == int(destinationId)].tolist()
            for concept in conceptterms:
                if (conceptFile.iloc[int(concept), 2] == 1):
                    lateralCount += 1
                    lateralList.append(int(destinationId))
    returnList = lateralList
    return lateralCount




def lateralAnalysisFinal(conceptId1, conceptId2):
    from asyncio.windows_events import NULL
    import re
    import pandas as pd
    import gensim.downloader as api
    from sklearn.metrics.pairwise import cosine_similarity
    import csv

    from gensim.test.utils import get_tmpfile
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
    fname = get_tmpfile("C:\\Users\\Will\\Desktop\\meshModel.mod")
    model = Doc2Vec.load(fname) 

    termFile = pd.read_csv('C:\\Users\\Will\\Desktop\\Snowmed\\sct2_Description_Snapshot-en_INT_20210731.txt', sep='\t')

    resultArr = [0, 0, 0]

    terms1 = termFile.index[termFile['conceptId'] == int(conceptId1)].tolist()
    terms2 = termFile.index[termFile['conceptId'] == int(conceptId2)].tolist()

    for term in terms1:
        if termFile.iloc[int(term),6] == 900000000000003001:
            term1 = term
            break

    for term in terms2:
        if termFile.iloc[int(term),6] == 900000000000003001:
            term2 = term
            break

    conceptName1 = termFile.iloc[term1, 7]
    conceptName2 = termFile.iloc[term2, 7]

    sentences = [str(conceptName1), str(conceptName2)]
    # creates the vectors necessary to compute cosine similarity
    vectors = [model.infer_vector([word for word in sent]).reshape(1, -1) for sent in sentences]

    # compute cosine similarity
    similarity = []
    for i in range(len(sentences)):
        row1 = []
        for j in range(len(sentences)):
            row1.append(cosine_similarity(vectors[i], vectors[j])[0][0])
        similarity.append(row1)

    if similarity[1][0] >= .9:

        parentCount1 = parent_Count(conceptId1)
        parentCount2 = parent_Count(conceptId2)

        if parentCount1 == parentCount2:
            lateralCount1 = 0
            lateralCount2 = 0
            lateral1List = []
            lateral2List = []
            returnList = []

            lateralCount1 = lateral_Count(conceptId1)
            lateral1List = returnList
            lateralCount2 = lateral_Count(conceptId2)
            lateral2List = returnList

            if lateralCount1 == lateralCount2 and all(item in lateral1List for item in lateral2List) and all(item in lateral2List for item in lateral1List):
                resultFinalSpecimen = open('C:\\Users\\Will\\Desktop\\resultFinalSpecimen.csv', 'a')
                writer = csv.writer(resultFinalSpecimen, lineterminator='\n')
                writer.writerow([conceptId1, conceptName1])
                writer.writerow([conceptId2, conceptName2])
                writer.writerow([])
                resultFinalSpecimen.close()
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1