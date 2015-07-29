# this is an attempt to fuse map and bst into a single data-structure to enjoy the benefits of both, i.e.,
# O(1) access time through key & O(log(n)) access time through value


class Node(object):
    def __init__(self, key, val, docIDlist=[], left=None, right=None):
        self.key  = key  # key
        self.val  = val # val can be key itself or some data against which we are scanning
        self.docIdlist = docIDlist # some data list
        self.left = left
        self.right = right


class MapBST(object):
    def __init__(self, mymap, rootBST):
        self.mymap = mymap
        self.rootBST = rootBST

    def __str__(self, key):
        return self.mymap[key]


    def addKV(self, key, val, docIdlist=[]):
        node = Node(key,val,docIdlist)
        # here reference to node object is inserted into MAP and BST. we are not duplicating node object.
        mymap.update({key: node})
        self.addNode(self.rootBST, node)


    def addNode(self, root, node):
        if int(node.val) < int(root.val):
            if root.left:
                self.addNode(root.left, node)
            else:
                root.left=node
        else:
            if root.right:
                self.addNode(root.right, node)
            else:
                root.right=node

    def getValMAP(self, key):
        return self.mymap[key].docIdlist

    def getByVal(self, val):
       if self.rootBST:
           return(self.getValBST(self.rootBST, val))
       else:
           return "empty"

    def getValBST(self, node, val):
        if int(node.val) == int(val):
            return node.docIdlist

        elif int(node.val) < int(val):
            if node.right :
                return self.getValBST(node.right, val)
            else:
                return "key not found"
        else:

            if node.left :
                return self.getValBST(node.left, val)
            else:
                return "key not found"




if __name__ == '__main__':

    # dummy lists to attach to Node object
    l1 = [1,2,2]
    l2 = [3,22]
    l3 = [1212, 122121]


    mymap = {}
    root = Node("five", 5, [l1, l2])
    mapbst = MapBST(mymap, root)

    # I am inserting in this order to make the Binary tree balanced.
    # Sort the list by value first which is 1 2 3 4 5 6 7 9
    # and then insert in this order below to make the tree balanced. pick the middle. go left and go right recursively.

    mapbst.addKV("four", 4, l2)
    mapbst.addKV("sevem", 7, [l1,l2])
    mapbst.addKV("nine", 9, l3)
    mapbst.addKV("six", 6, [l1,l3])
    mapbst.addKV("two", 2, [l3,l2])
    mapbst.addKV("one", 1, [l3,l1])
    mapbst.addKV("three",3, l1)


    print ("Search by VAL " ,mapbst.getByVal(3))

    print ("Search and by KEY ",  mapbst.getValMAP("nine"))






