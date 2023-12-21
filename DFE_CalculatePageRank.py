import math
class Node:
    name: str
    oldPageRank : float
    pageRank : float
    isPageRankExact: bool
    inNodes : list['Node']
    outNodes : list['Node']
    expectedValue : float
    d = 0.85

    def __init__(self, name, inNodes = None, outNodes = None, expectedValue = None):
        self.pageRank = 1
        self.isPageRankExact = False
        self.name = name
        if(expectedValue != None):
            self.expectedValue = expectedValue
        else:
            self.expectedValue = -1
        if inNodes != None:
            self.inNodes = inNodes 
        else:
            self.inNodes = []
        if outNodes != None:
            self.outNodes  = outNodes  
        else:
            self.outNodes  = []  
        
    def __str__(self):
        return self.name

    def calculatePageRank(self):

        if all(x.isPageRankExact for x in self.inNodes) and self.isPageRankExact: 
            return self.pageRank
        
        inNodeValue = 0
        self.oldPageRank = self.pageRank
        for inNode in self.inNodes:
            inNodeValue += inNode.pageRank / len(inNode.outNodes)
        self.pageRank = 1 - self.d + (self.d * inNodeValue)
        
        if math.isclose(self.oldPageRank, self.pageRank):
            self.isPageRankExact = True
        
        for inNode in self.inNodes:
            inNode.calculatePageRank()
        for outNode in self.outNodes:
            outNode.calculatePageRank()
        return self.pageRank

    def calculatePageRankNonRecursive(self, iterations = 15):
        allNodes = self.getAllNodes(list())
        i=0
        while i < iterations :
            for node in allNodes:
                inNodeValue = 0
                for inNode in node.inNodes:
                    inNodeValue += inNode.pageRank / len(inNode.outNodes)
                node.pageRank = 1 - node.d + (node.d * inNodeValue)
            i+=1
        return

    def getAllNodes(self, nodeList : list['Node']):
        newNodes = list(['Node'])
        for inNode in self.inNodes:
            if inNode not in nodeList:
                nodeList.append(inNode)
                newNodes.append(inNode)
        for outNode in self.outNodes:
            if outNode not in nodeList:
                nodeList.append(outNode)
                newNodes.append(outNode)

        for node in newNodes:
            linkedNodes = node.getAllNodes(nodeList)
            for linkedNode in linkedNodes:
                if(linkedNode not in nodeList):
                    nodeList.append(linkedNode)
                
        return nodeList
    
    def EdgeTo(self, toNode : 'Node'):
        self.outNodes.append(toNode)
        toNode.inNodes.append(self)
        return toNode

    def EdgeFrom(self, fromNode : 'Node'):
        self.inNodes.append(fromNode)
        fromNode.outNodes.append(self)
        return fromNode
    
    @staticmethod
    def CleanNodes(nodes:list['Node']):
        for node in nodes:
            node.pageRank=1
            node.isPageRankExact=False