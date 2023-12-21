from DFE_CalculatePageRank import Node
import unittest
import math

class NodeTest(unittest.TestCase):

    def setUp(self):
        pass

    def errorMsg(self, errorType, node:Node, expectedValue, tolerance):
        match errorType:
            case "wrongValueRecursive":
                return f"RecursiveCalculationError: The node {node} has the Value {node.pageRank}, but {expectedValue} with a tolerance of {tolerance*100}% was expected"
            case "wrongValueIterative":
                return f"IterativeCalculationError: The node {node} has the Value {node.pageRank}, but {expectedValue} with a tolerance of {tolerance*100}% was expected"
            case _:
                return f"unknown errorType: {errorType}"

    def test_graph1(self):
        print("Starting test_graph1")
        tol = 0.1
        nodeA1 = Node('A1',None,None,1.0)
        nodeB1 = Node('B1',None,None,1.0)
        nodes = [nodeA1, nodeB1]
        nodeB1.EdgeTo(nodeA1)
        nodeB1.EdgeFrom(nodeA1)
        self.calculationTesting(nodes, tol)

    def test_graph2(self):    
        print("Starting test_graph2")
        tol = 0.1
        nodeA2 = Node('A2',None,None,1.0)
        nodeB2 = Node('B2',None,None,1.0)
        nodeC2 = Node('C2',None,None,1.0)
        nodes = [nodeA2, nodeB2, nodeC2]
        nodeA2.EdgeTo(nodeC2)
        nodeC2.EdgeTo(nodeB2)
        nodeB2.EdgeTo(nodeA2)

        self.calculationTesting(nodes, tol)
        
    def test_graph3(self):
        print("Starting test_graph3")
        tol = 0.1
        nodeA3 = Node('A3', None, None, 0.261)
        nodeB3 = Node('B3', None, None, 0.261)
        nodeC3 = Node('C3', None, None, 0.372)
        nodes = [nodeA3,nodeB3,nodeC3]
        nodeA3.EdgeTo(nodeB3)
        nodeA3.EdgeTo(nodeC3)
        nodeB3.EdgeTo(nodeA3)
        nodeB3.EdgeTo(nodeC3)
        self.calculationTesting(nodes, tol)

    def test_graph4(self):
        print("Starting test_graph4")
        tol = 0.1
        nodeA4 = Node('A4', None, None, 0.15)
        nodeB4 = Node('B4', None, None, 0.2775)
        nodeC4 = Node('C4', None, None, 0.385875)
        nodes = [nodeA4,nodeB4,nodeC4]
        nodeA4.EdgeTo(nodeB4)
        nodeB4.EdgeTo(nodeC4)
        self.calculationTesting(nodes, tol)


    def calculationTesting(self, nodes:list['Node'], relTol):
        nodes[0].calculatePageRank()        
        for node in nodes:
            self.assertTrue(math.isclose(node.pageRank, node.expectedValue, rel_tol=relTol), self.errorMsg("wrongValueIterative", node, node.expectedValue, relTol))
            print(f"{node} has the value {node.pageRank}")

        Node.CleanNodes(nodes)

        nodes[0].calculatePageRankNonRecursive()
        for node in nodes:
            self.assertTrue(math.isclose(node.pageRank, node.expectedValue, rel_tol=relTol), self.errorMsg("wrongValueRecursive", node, node.expectedValue, relTol))
            print(f"{node} has the value {node.pageRank}")