import mysql.connector;
from CalculatePageRank_DFE import Node

dbConnection = mysql.connector.connect(host='localhost', user='root', password='')
cursor = dbConnection.cursor(buffered=True)
goToDatabaseString = "USE itf21a_wiki"	
cursor.execute(goToDatabaseString)


def getConnectionsFromSites():
    result = list()
    queryString = f"SELECT pl.pl_title, p.page_title as eingehendeLinks FROM pagelinks pl, page p WHERE pl.pl_from=p.page_id AND pl.pl_title<>p.page_title;"
    cursor.execute(queryString)
    row_count = cursor.rowcount
    if (row_count == 0):
        print("Fehler")
        return False
    rows = cursor.fetchall()
    for row in rows:
        rowString=""
        for field in row:
            rowString += field.decode() + ";"
        result.append(rowString[:-1])

    for row in result:
        print(row)
    return result

def CalculatePageRankFromSites(sites):
    createdNodes = list()
    for row in sites:
        pair = str(row).split(";")
        #Erstelle die Nodes, wenn noch nicht vorhanden
        if not any(x.name == pair[0] for x in createdNodes): createdNodes.append(Node(pair[0]))
        if not any(x.name == pair[1] for x in createdNodes): createdNodes.append(Node(pair[1]))

        #erstelle die Verbindung
        linkedToNode = next(x for x in createdNodes if x.name == pair[0])
        linkedFromNode = next(x for x in createdNodes if x.name == pair[1])

        linkedFromNode.EdgeTo(linkedToNode)

    print (createdNodes)

    createdNodes[0].calculatePageRankNonRecursive()
    createdNodes.sort(key=lambda x: x.pageRank, reverse=True)
    sumOfPageRanks = 0
    for node in createdNodes:
        print(f"{node}, {node.pageRank}")
        sumOfPageRanks += node.pageRank
    print(f"Sum of Pageranks: {sumOfPageRanks}")
    return 


CalculatePageRankFromSites(getConnectionsFromSites())
