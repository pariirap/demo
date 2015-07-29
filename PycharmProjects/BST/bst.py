# this is an attempt to fuse map and bst into a single data-structure to enjoy the benefits of both, i.e.,
# O(1) access time through key & O(log(n)) access time through value



class Node(object):
    def __init__(self, key, val, left=None, right=None):
        self.val  = val
        self.data = "my data "
        self.left = left
        self.right = right


class BST(object):
    def __init__(self,rootBST):
        self.rootBST = rootBST


    def addKV(self, val):

        node = Node(val)
        self.addNode(self.rootBST, node)


    def addNode(self, root, node):
        if int(node.key) < int(root.key):
            if root.left:
                self.addNode(root.left, node)
            else:
                root.left=node
        else:
            if root.right:
                self.addNode(root.right, node)
            else:
                root.right=node



    def getValBST(self, node, key):
        if int(node.key) == int(key):
            #print ("rt ", int(node.key), node.val)
            return node.val
            #return str(node.val)
        elif int(node.key) < int(key):
            #print (int(node.key))
            if node.right :
                return self.getValBST(node.right, key)
            else:
                return "key not found"
        else:
            #print (int(node.key))
            if node.left :
                return self.getValBST(node.left, key)
            else:
                return "key not found"






if __name__ == '__main__':
    l1 = [1,2,2]
    l2 = [3,22]

    mymap1 = {5:[l1,l2], 4:[232,23,12,11],7:[1,1,2,2], 9:"hi pari"}
    print (mymap1[5])
    mymap = {1:1}
    root = Node(5, [l1, l2])
    mapbst = MapBST(mymap, root)
    #mapbst.addKV(5, l1)





    mapbst.addKV(4, l2)
    mapbst.addKV(7, [l1,l2])
    mapbst.addKV(9, "nine")
    mapbst.addKV(6, "six")
    mapbst.addKV(2, "two")
    mapbst.addKV(1, "one")
    mapbst.addKV(3, "three")

    #for key,value in sorted(mapbst.mymap.items()):
        #print ("K ", key, value)

    str1 = mapbst.getValMAP(6)
    print(mapbst.getByVal(3))
    print ("str is ", str1,  mapbst.getValMAP(1))
    #print (str2)







#index=Index(mymap, node)
