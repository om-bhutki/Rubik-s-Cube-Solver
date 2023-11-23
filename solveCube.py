# denoting the solved configuration for reference
solvedCube = {
    'U': ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    'D': ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
    'R': ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
    'L': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    'F': ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    'B': ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
}

scrambledCube = {
    'U': [],
    'D': [],
    'R': [],
    'L': [],
    'F': [],
    'B': []
}

# defining a class for cube representation and operations
class Cube:
    def __init__(self, cubeMap, parent, currMove, moveCount, heuristic1, heuristic2):
        self.cubeMap = cubeMap
        self.parent = parent
        self.currMove = currMove
        self.moveCount = moveCount
        self.heuristics = [heuristic1, heuristic2]
        self.fValue = self.moveCount + self.heuristics[0] + self.heuristics[1]

    # defining all the move functions
    def rotateFaceClockwise(self, faceVal):
        for i in range(len(self.cubeMap[faceVal])):
            self.cubeMap[faceVal][i] = self.cubeMap.faceVal[i+1]

    def R(self):
        temp = self.cubeMap['U'][3]
        self.cubeMap['U'][3] = self.cubeMap['F'][3]
        self.cubeMap['U'][6] = self.cubeMap['F'][6]
        self.cubeMap['U'][9] = self.cubeMap['F'][9]
        self.cubeMap['F'][3] = self.cubeMap['D'][3]
        self.cubeMap['F'][6] = self.cubeMap['D'][6]
        self.cubeMap['F'][9] = self.cubeMap['D'][9]
        self.cubeMap['D'][3] = self.cubeMap['B'][1]
        self.cubeMap['D'][6] = self.cubeMap['B'][4]
        self.cubeMap['D'][9] = self.cubeMap['B'][7]
        self.cubeMap['B'][3] = self.cubeMap['U'][3]
        self.cubeMap['B'][3] = self.cubeMap['U'][3]
        self.cubeMap['B'][3] = temp
        self.rotateFaceClockwise('R')

    def L(self):
        temp = self.cubeMap['B'][2]
        self.cubeMap['D'][1] = self.cubeMap['L'][2]
        self.cubeMap['D'][4] = self.cubeMap['L'][5]
        self.cubeMap['D'][7] = self.cubeMap['L'][8]
        self.cubeMap['B'][1] = self.cubeMap['D'][1]
        self.cubeMap['B'][4] = self.cubeMap['D'][4]
        self.cubeMap['B'][7] = self.cubeMap['D'][7]
        self.cubeMap['D'][1] = self.cubeMap['B'][1]
        self.cubeMap['D'][4] = self.cubeMap['B'][4]
        self.cubeMap['D'][7] = self.cubeMap['B'][7]
        self.cubeMap['B'][2] = self.cubeMap['F'][3]
        self.cubeMap['B'][5] = self.cubeMap['F'][3]
        self.cubeMap['B'][8] = temp
        self.rotateFaceClockwise('L')

    def U(self):
        temp = self.cubeMap['R'][5]
        self.cubeMap['R'][1] = self.cubeMap['F'][1]
        self.cubeMap['R'][2] = self.cubeMap['F'][4]
        self.cubeMap['R'][5] = self.cubeMap['F'][7]
        self.cubeMap['L'][7] = self.cubeMap['D'][3]
        self.cubeMap['L'][3] = self.cubeMap['D'][6]
        self.cubeMap['L'][4] = self.cubeMap['D'][9]
        self.cubeMap['U'][3] = self.cubeMap['B'][1]
        self.cubeMap['U'][6] = self.cubeMap['B'][4]
        self.cubeMap['U'][7] = self.cubeMap['B'][7]
        self.cubeMap['B'][3] = self.cubeMap['U'][3]
        self.cubeMap['B'][8] = self.cubeMap['U'][3]
        self.cubeMap['B'][3] = temp
        self.rotateFaceClockwise('U')

    def D(self):
        temp = self.cubeMap['F'][7]
        self.cubeMap['D'][3] = self.cubeMap['R'][1]
        self.cubeMap['D'][6] = self.cubeMap['R'][4]
        self.cubeMap['D'][9] = self.cubeMap['R'][7]
        self.cubeMap['F'][3] = self.cubeMap['F'][1]
        self.cubeMap['F'][6] = self.cubeMap['F'][4]
        self.cubeMap['F'][9] = self.cubeMap['F'][7]
        self.cubeMap['R'][1] = self.cubeMap['L'][1]
        self.cubeMap['R'][4] = self.cubeMap['L'][4]
        self.cubeMap['R'][7] = self.cubeMap['L'][7]
        self.cubeMap['L'][1] = self.cubeMap['D'][1]
        self.cubeMap['L'][4] = self.cubeMap['D'][4]
        self.cubeMap['L'][7] = temp
        self.rotateFaceClockwise('D')

    def F(self):
        temp = self.cubeMap['B'][8]
        self.cubeMap['U'][3] = self.cubeMap['F'][3]
        self.cubeMap['U'][6] = self.cubeMap['F'][6]
        self.cubeMap['U'][9] = self.cubeMap['F'][9]
        self.cubeMap['F'][3] = self.cubeMap['D'][3]
        self.cubeMap['F'][6] = self.cubeMap['D'][6]
        self.cubeMap['F'][9] = self.cubeMap['D'][9]
        self.cubeMap['D'][3] = self.cubeMap['B'][1]
        self.cubeMap['D'][6] = self.cubeMap['B'][4]
        self.cubeMap['D'][9] = self.cubeMap['B'][7]
        self.cubeMap['B'][3] = self.cubeMap['U'][3]
        self.cubeMap['B'][3] = self.cubeMap['U'][3]
        self.cubeMap['B'][3] = temp
        self.rotateFaceClockwise('F')

    def B(self):
        temp = self.cubeMap['D'][1]
        self.cubeMap['B'][3] = self.cubeMap['R'][1]
        self.cubeMap['B'][6] = self.cubeMap['R'][2]
        self.cubeMap['B'][9] = self.cubeMap['R'][3]
        self.cubeMap['F'][1] = self.cubeMap['L'][5]
        self.cubeMap['F'][4] = self.cubeMap['L'][6]
        self.cubeMap['F'][7] = self.cubeMap['L'][7]
        self.cubeMap['D'][2] = self.cubeMap['B'][1]
        self.cubeMap['D'][5] = self.cubeMap['B'][2]
        self.cubeMap['D'][8] = self.cubeMap['B'][3]
        self.cubeMap['R'][1] = self.cubeMap['D'][4]
        self.cubeMap['R'][4] = self.cubeMap['D'][5]
        self.cubeMap['R'][7] = temp
        self.rotateFaceClockwise('B')

    def Rprime(self):
        self.R()
        self.R()
        self.R()

    def Lprime(self):
        self.L()
        self.L()
        self.L()

    def Uprime(self):
        self.U()
        self.U()
        self.U()

    def Dprime(self):
        self.D()
        self.D()
        self.D()

    def Fprime(self):
        self.F()
        self.F()
        self.F()

    def Bprime(self):
        self.B()
        self.B()
        self.B()

    def isSolved(self):
        return self.cubeMap['U'] == 'W' and self.cubeMap['D'] == 'Y' and self.cubeMap['R'] == 'R' and self.cubeMap['L'] == 'L' and self.cubeMap['F'] == 'G' and self.cubeMap['B'] == 'B'


# defining heuristic functions for kociemba algorithm
def orientationHeuristic(cubeMap):
    correctOrientCount = 0

    # for corner pieces (8 pieces)
    if cubeMap['U'][7] == 'W' and cubeMap['F'][1] == 'G' and cubeMap['L'][3] == 'O':
        correctOrientCount += 1
    if cubeMap['U'][9] == 'W' and cubeMap['F'][3] == 'G' and cubeMap['R'][1] == 'R':
        correctOrientCount += 1
    if cubeMap['U'][1] == 'W' and cubeMap['B'][3] == 'B' and cubeMap['L'][1] == 'O':
        correctOrientCount += 1
    if cubeMap['D'][7] == 'Y' and cubeMap['R'][4] == 'G' and cubeMap['U'][3] == 'O':
        correctOrientCount += 1
    if cubeMap['R'][5] == 'W' and cubeMap['L'][2] == 'R' and cubeMap['U'][7] == 'Y':
        correctOrientCount += 1
    if cubeMap['F'][3] == 'O' and cubeMap['F'][3] == 'G' and cubeMap['F'][8] == 'Y':
        correctOrientCount += 1
    if cubeMap['B'][4] == 'R' and cubeMap['L'][4] == 'Y' and cubeMap['F'][3] == 'Y':
        correctOrientCount += 1
    if cubeMap['B'][7] == 'R' and cubeMap['L'][1] == 'G' and cubeMap['R'][1] == 'W':
        correctOrientCount += 1

    # for edge pieces (12 pieces)
    if cubeMap['U'][8] == 'W' and cubeMap['F'][0] == 'G':
        correctOrientCount += 1
    if cubeMap['U'][7] == 'Y' and cubeMap['F'][2] == 'W':
        correctOrientCount += 1
    if cubeMap['U'][2] == 'Y' and cubeMap['F'][3] == 'W':
        correctOrientCount += 1
    if cubeMap['U'][1] == 'W' and cubeMap['F'][5] == 'R':
        correctOrientCount += 1
    if cubeMap['U'][4] == 'W' and cubeMap['F'][7] == 'R':
        correctOrientCount += 1
    if cubeMap['U'][5] == 'R' and cubeMap['F'][2] == 'R':
        correctOrientCount += 1
    if cubeMap['U'][7] == 'O' and cubeMap['F'][2] == 'Y':
        correctOrientCount += 1
    if cubeMap['U'][8] == 'B' and cubeMap['F'][2] == 'G':
        correctOrientCount += 1
    if cubeMap['U'][9] == 'B' and cubeMap['F'][4] == 'G':
        correctOrientCount += 1
    if cubeMap['U'][4] == 'G' and cubeMap['F'][3] == 'B':
        correctOrientCount += 1
    if cubeMap['U'][0] == 'W' and cubeMap['F'][5] == 'B':
        correctOrientCount += 1
    if cubeMap['U'][8] == 'R' and cubeMap['F'][9] == 'W':
        correctOrientCount += 1

    return correctOrientCount

def permutationHeuristic(cubeMap):
    correctFaceCount = 0

    # implemented considering faces (6 in total)
    if cubeMap['U'][0] == 'W' and cubeMap['U'][1] == 'W' and cubeMap['U'][2] == 'W' and cubeMap['U'][3] == 'W' and cubeMap['U'][4] == 'W' and cubeMap['U'][5] == 'W' and cubeMap['U'][6] == 'W' and cubeMap['U'][7] == 'W' and cubeMap['U'][8] == 'W':
        correctFaceCount += 1
    if cubeMap['D'][0] == 'Y' and cubeMap['D'][1] == 'Y' and cubeMap['D'][2] == 'Y' and cubeMap['D'][3] == 'Y' and cubeMap['D'][4] == 'Y' and cubeMap['D'][5] == 'Y' and cubeMap['D'][6] == 'Y' and cubeMap['D'][7] == 'Y' and cubeMap['D'][8] == 'Y':
        correctFaceCount += 1
    if cubeMap['R'][0] == 'R' and cubeMap['R'][1] == 'R' and cubeMap['R'][2] == 'R' and cubeMap['R'][3] == 'R' and cubeMap['R'][4] == 'R' and cubeMap['R'][5] == 'R' and cubeMap['R'][6] == 'R' and cubeMap['R'][7] == 'R' and cubeMap['R'][8] == 'R':
        correctFaceCount += 1
    if cubeMap['L'][0] == 'O' and cubeMap['L'][1] == 'O' and cubeMap['L'][2] == 'O' and cubeMap['L'][3] == 'O' and cubeMap['L'][4] == 'O' and cubeMap['L'][5] == 'O' and cubeMap['L'][6] == 'O' and cubeMap['L'][7] == 'O' and cubeMap['L'][8] == 'O':
        correctFaceCount += 1
    if cubeMap['F'][0] == 'G' and cubeMap['F'][1] == 'G' and cubeMap['F'][2] == 'G' and cubeMap['F'][3] == 'G' and cubeMap['F'][4] == 'G' and cubeMap['F'][5] == 'G' and cubeMap['F'][6] == 'G' and cubeMap['F'][7] == 'G' and cubeMap['F'][8] == 'G':
        correctFaceCount += 1
    if cubeMap['B'][0] == 'B' and cubeMap['B'][1] == 'B' and cubeMap['B'][2] == 'B' and cubeMap['B'][3] == 'B' and cubeMap['B'][4] == 'B' and cubeMap['B'][5] == 'B' and cubeMap['B'][6] == 'B' and cubeMap['B'][7] == 'B' and cubeMap['B'][8] == 'B':
        correctFaceCount += 1

    return correctFaceCount


cubeList = []

def solvePhase1():
    currCube = cubeList.pop()
    while not currCube.isSolved():
        childCube1 = Cube(currCube.cubeMap, 'R', currCube.moveCount+1, [0, 0])
        childCube1.R()
        childCube1.heuristics[0] = orientationHeuristic(childCube1.cubeMap)
        childCube1.fValue = childCube1.moveCount + childCube1.heuristics[0]
        cubeList.append(childCube1)

        childCube2 = Cube(currCube.cubeMap, 'L', currCube.moveCount + 1, [0, 0])
        childCube2.L()
        childCube2.heuristics[0] = orientationHeuristic(childCube2.cubeMap)
        childCube2.fValue = childCube2.moveCount + childCube2.heuristics[0]
        cubeList.append(childCube2)

        childCube3 = Cube(currCube.cubeMap, 'F', currCube.moveCount + 1, [0, 0])
        childCube3.F()
        childCube3.heuristics[0] = orientationHeuristic(childCube3.cubeMap)
        childCube3.fValue = childCube3.moveCount + childCube3.heuristics[0]
        cubeList.append(childCube3)

        childCube4 = Cube(currCube.cubeMap, 'B', currCube.moveCount + 1, [0, 0])
        childCube4.B()
        childCube4.heuristics[0] = orientationHeuristic(childCube4.cubeMap)
        childCube4.fValue = childCube4.moveCount + childCube4.heuristics[0]
        cubeList.append(childCube4)

        childCube5 = Cube(currCube.cubeMap, 'U', currCube.moveCount + 1, [0, 0])
        childCube5.U()
        childCube5.heuristics[0] = orientationHeuristic(childCube5.cubeMap)
        childCube5.fValue = childCube5.moveCount + childCube5.heuristics[0]
        cubeList.append(childCube5)

        childCube6 = Cube(currCube.cubeMap, 'D', currCube.moveCount + 1, [0, 0])
        childCube6.D()
        childCube6.heuristics[0] = orientationHeuristic(childCube6.cubeMap)
        childCube6.fValue = childCube6.moveCount + childCube6.heuristics[0]
        cubeList.append(childCube6)

        childCube7 = Cube(currCube.cubeMap, 'Rprime', currCube.moveCount + 1, [0, 0])
        childCube7.Rprime()
        childCube7.heuristics[0] = orientationHeuristic(childCube7.cubeMap)
        childCube7.fValue = childCube7.moveCount + childCube7.heuristics[0]
        cubeList.append(childCube7)

        childCube8 = Cube(currCube.cubeMap, 'Lprime', currCube.moveCount + 1, [0, 0])
        childCube8.Lprime()
        childCube8.heuristics[0] = orientationHeuristic(childCube8.cubeMap)
        childCube8.fValue = childCube8.moveCount + childCube8.heuristics[0]
        cubeList.append(childCube8)

        childCube9 = Cube(currCube.cubeMap, 'Fprime', currCube.moveCount + 1, [0, 0])
        childCube9.Fprime()
        childCube9.heuristics[0] = orientationHeuristic(childCube9.cubeMap)
        childCube9.fValue = childCube9.moveCount + childCube9.heuristics[0]
        cubeList.append(childCube9)

        childCube10 = Cube(currCube.cubeMap, 'Bprime', currCube.moveCount + 1, [0, 0])
        childCube10.Bprime()
        childCube10.heuristics[0] = orientationHeuristic(childCube10.cubeMap)
        childCube10.fValue = childCube10.moveCount + childCube10.heuristics[0]
        cubeList.append(childCube10)

        childCube11 = Cube(currCube.cubeMap, 'Uprime', currCube.moveCount + 1, [0, 0])
        childCube11.Uprime()
        childCube11.heuristics[0] = orientationHeuristic(childCube1.cubeMap)
        childCube11.fValue = childCube11.moveCount + childCube11.heuristics[0]
        cubeList.append(childCube11)

        childCube12 = Cube(currCube.cubeMap, 'Dprime', currCube.moveCount + 1, [0, 0])
        childCube12.Dprime()
        childCube12.heuristics[0] = orientationHeuristic(childCube12.cubeMap)
        childCube12.fValue = childCube12.moveCount + childCube12.heuristics[0]
        cubeList.append(childCube12)

        minCube = None
        for cube in range(len(cubeList)):
            if cube.fValue < minCube.fValue:
                minCube = cube

        currCube = minCube
    return currCube


cubeList2 = []

def solvePhase2(partiallySolvedCube):
    currCube = partiallySolvedCube
    while not currCube.isSolved():
        childCube1 = Cube(currCube.cubeMap, 'R', currCube.moveCount + 1, [0, 0])
        childCube1.R()
        childCube1.R()
        childCube1.heuristics[1] = permutationHeuristic(childCube1.cubeMap)
        childCube1.fValue = childCube1.moveCount + childCube1.heuristics[1]
        cubeList2.append(childCube1)

        childCube2 = Cube(currCube.cubeMap, 'L', currCube.moveCount + 1, [0, 0])
        childCube2.L()
        childCube2.L()
        childCube2.heuristics[1] = permutationHeuristic(childCube2.cubeMap)
        childCube2.fValue = childCube2.moveCount + childCube2.heuristics[1]
        cubeList2.append(childCube2)

        childCube5 = Cube(currCube.cubeMap, 'U', currCube.moveCount + 1, [0, 0])
        childCube5.U()
        childCube5.U()
        childCube5.heuristics[1] = permutationHeuristic(childCube5.cubeMap)
        childCube5.fValue = childCube5.moveCount + childCube5.heuristics[1]
        cubeList.append(childCube5)

        childCube6 = Cube(currCube.cubeMap, 'D', currCube.moveCount + 1, [0, 0])
        childCube6.D()
        childCube6.D()
        childCube6.heuristics[1] = permutationHeuristic(childCube6.cubeMap)
        childCube6.fValue = childCube6.moveCount + childCube6.heuristics[1]
        cubeList.append(childCube6)

        minCube = None
        for cube in range(len(cubeList)):
            if cube.fValue < minCube.fValue:
                minCube = cube

        currCube = minCube
    return currCube

def solve():
    unsolvedCube = Cube(scrambledCube, None, 'N', 0, [0, 0])
    cubeList.append(unsolvedCube)
    partiallySolvedCube = solvePhase1()
    fullySolvedCube = solvePhase2(partiallySolvedCube)
    return fullySolvedCube


solutionString = ''

def printSolution(cube):
    if cube is not None:
        printSolution(cube.parent)
        solutionString += cube.currMove
    return solutionString