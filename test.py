class Node :
    def __init__(self, value, left=None, right=None) :
        self.left   = left
        self.right  = right
        self.value  = value

class BSTree :
    # 초기 설정
    def __init__(self) -> None:
        self.root = None
    # 추가
    def add (self, value) :
        self.root = self.AddRecursive(self.root, value)
    def AddRecursive(self, current, value):
        if(current is None):
            return Node(value)
        if value < current.value :
            current.left    = self.AddRecursive(current.left, value)
        elif value > current.value :
            current.right   = self.AddRecursive(current.right, value)
        else :
            return current
        return current
    # 검색
    def searchNode(self, value):
        return "찾는 데이터가 있습니다." if self.containsNode(value) else "찾는 데이터가 없습니다."
    def containsNode(self, value):
        return self.containsNodeRecursive(self.root, value)
    def containsNodeRecursive(self, current, value):
        if(current == None):
            return False
        if value == current.value:
            return True
        return self.containsNodeRecursive(current.left, value) if value < current.value else  self.containsNodeRecursive(current.right, value)
    # 삭제
    def deleteRecursive(self, current, value):
        if current == None :
            return None
        if value == current.value:
            if current.left == None and current.right == None :
                return None
            if current.right == None :
                return current.left
            if current.left == None:
                return current.right
            smallestValue = self.findSmallestValue(current.right)
            current.valeu = smallestValue
            current.right = self.deleteRecursive(current.right, smallestValue)
            return current
        if value < current.value :
            current.left = self.deleteRecursive(current.left, value)
            return current
        current.right = self.deleteRecursive(current.right, value)
        return current
    def findSmallestValue(self, root):
        return root.value if root.left == None else self.findSmallestValue(root.left)
    def delete(self, value):
        self.root = self.deleteRecursive(self.root, value)
    # 출력
    def callback(self, value):
        print(value, end=" ")
    def preorder(self, node):
        if(node != None):
            self.callback(node.value)
            self.preorder(node.left)
            self.preorder(node.right)
    def inorder(self, node):
        if(node != None):
            self.inorder(node.left)
            self.callback(node.value)
            self.inorder(node.right)
    def postorder(self, node):
        if(node != None):
            self.postorder(node.left)
            self.postorder(node.right)
            self.callback(node.value)

tree = BSTree()
tree.add(6)
tree.add(4)
tree.add(8)
tree.add(3)
tree.add(5)
tree.add(7)
tree.add(9)

tree.preorder(tree.root)
tree.delete(4)
print()
tree.preorder(tree.root)
tree.delete(6)
print()
tree.preorder(tree.root)
tree.delete(7)
print()
tree.preorder(tree.root)

# 최소한의 동전 개수를 거스름
# print('=======')
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[-1]
# second = data[-2]
#
# count = int(m/ (k+1))*k
# count += m % (k+1)
#
# result = 0
# result += count * first
# result += (m - count) * second
#
# print(result)

# 숫자 카드 게임
# a, b = map(int, input().split())
# data2 = []
#
# min_value = 0
# max_value = 0
# for i in range(a):
#     data2.append(list(map(int, input().split())))
#     min_value = min(data2)
#     max_value = max(max_value, min_value)

# n, m = map(int, input().split())
# count = 0
# while True:
#
#     if n == 1:
#         break
#     # 나눌수 있는 지 확인
#     if (n % m) == 0:
#         n = n //m
#         count += 1
#     else:
#         n -= 1
#         count += 1
#
# print(count)





