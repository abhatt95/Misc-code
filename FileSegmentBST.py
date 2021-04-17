
class Request():

    def __init__(self,limits):
        self.start = limits[0] 
        self.end = limits[1] 

    def is_overlap(self,request):
        if self.start <= request.start <= self.end \
            or self.start <= request.end <= self.end:
            return True
        return False

    def __str__(self):
        return "Start : {} End: {}".format(self.start,self.end)

    def get_non_overlappingpart(self,request):
        points = [request.start,request.end]
        max_p,min_p = max(points),min(points)
        left,right = None,None
        if min_p < self.start:
            left = Request((min_p,self.start))

        if self.end < max_p:
            right = Request((self.end,max_p))

        return (left,right)

class Node():
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None 


class BST():

    def __init__(self):
        self.toSend = []

    def insert(self,root,request):
        if not root:
            root = Node(request) 
            if request not in self.toSend:
                self.toSend.append(request)
            return root

        if root.data.is_overlap(request):
            left_child,right_child = root.data.get_non_overlappingpart(request)
            if left_child: 
                root.left = self.insert(root.left,left_child)
            if right_child: 
                root.right = self.insert(root.right,right_child) 
            return root

        if root.data.start > request.end:
            root.left = self.insert(root.left,request)
            return root
        if root.data.end < request.start:
            root.right = self.insert(root.right,request)
            return root
        return root

    def print(self,root):
        print("*** Printing tree in BFS order ***")
        q = [root]
        while q:
            current = q.pop()
            print(current.data)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)


b = BST()

requests = [(10,20),(1,5),(22,30),(15,25),(2,3),(40,50)]
root = None
for req in requests:
    request = Request(req)
    root = b.insert(root,request)
    print("After inserting - ")
    print(request)
    #b.print(root)
    print(" ** Send back ** ")
    for req in b.toSend:
        print(req)
    b.toSend = []