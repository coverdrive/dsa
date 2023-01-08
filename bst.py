from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Generic, TypeVar

X = TypeVar('X')


@dataclass
class BSTNode(Generic[X]):
    key: X
    left: BST
    right: BST
    parent: BST

    def assertParentLinks(self) -> None:
        if self.left is not None:
            assert self.left.parent == self, "parent link broken"
            self.left.assertParentLinks()
        if self.right is not None:
            assert self.right.parent == self, "parent link broken"
            self.right.assertParentLinks()

    def displayBST(self, level=0) -> str:
        ret_val: str = ''
        if self.right is not None:
            ret_val += self.right.displayBST(level + 1)
        ret_val += ' ' * 4 * level + '-> ' + str(self.key) + '\n'
        if self.left is not None:
            ret_val += self.left.displayBST(level + 1)
        return ret_val

    def __repr__(self) -> str:
        return self.displayBST()


BST = Optional[BSTNode]


def create_empty_BST() -> BST:
    return None


def create_single_node_BST(elem: X) -> BSTNode:
    return BSTNode(
        key=elem,
        parent=None,
        left=None,
        right=None
    )


def search(bst: BST, elem: X) -> BST:
    if bst is None or elem == bst.key:
        return bst
    elif elem < bst.key:
        return search(bst.left, elem)
    else:
        return search(bst.right, elem)


def minimum(bstNode: BSTNode) -> BSTNode:
    if bstNode.left is None:
        return bstNode
    else:
        return minimum(bstNode.left)


def maximum(bstNode: BSTNode) -> BSTNode:
    if bstNode.right is None:
        return bstNode.key
    else:
        return maximum(bstNode.right)


def successor(bstNode: BSTNode) -> BST:
    if bstNode.right is not None:
        return minimum(bstNode.right)
    else:
        n: BSTNode = bstNode
        p: BST = n.parent
        while p is not None and n == p.right:
            n = p
            p = p.parent
        return p


def predecessor(bstNode: BSTNode) -> BST:
    if bstNode.left is not None:
        return minimum(bstNode.left)
    else:
        n: BSTNode = bstNode
        p: BST = n.parent
        while p is not None and n == p.left:
            n = p
            p = p.parent
        return p


def insert(bstNode: BSTNode, elem: X) -> BSTNode:
    single_node: BSTNode = create_single_node_BST(elem)
    if elem <= bstNode.key:
        if bstNode.left is None:
            bstNode.left = single_node
            single_node.parent = bstNode
        else:
            insert(bstNode.left, elem)
    else:
        if bstNode.right is None:
            bstNode.right = single_node
            single_node.parent = bstNode
        else:    
            insert(bstNode.right, elem)
    return bstNode


def delete(bstNode: BSTNode, deleteNode: BSTNode) -> BST:
    if deleteNode.left is None and deleteNode.right is None:
        replacementNode = None
    elif deleteNode.left is None:
        replacementNode = deleteNode.right
    elif deleteNode.right is None:
        replacementNode = deleteNode.left
    else:
        replacementNode = successor(deleteNode)
        if replacementNode != deleteNode.right:
            replacementNode.parent.left = replacementNode.right
            if replacementNode.right is not None:
                replacementNode.right.parent = replacementNode.parent
            replacementNode.right = deleteNode.right
            replacementNode.right.parent = replacementNode
        replacementNode.left = deleteNode.left
        replacementNode.left.parent = replacementNode

    parentNode: BST = deleteNode.parent
    if replacementNode is not None:
        replacementNode.parent = parentNode
    if parentNode is None:
        return replacementNode
    else:
        if deleteNode == parentNode.left:
            parentNode.left = replacementNode
        else:
            parentNode.right = replacementNode
        return bstNode


if __name__ == '__main__':
    node: BSTNode = create_single_node_BST(5)
    node = insert(node, 2)
    node = insert(node, 7)
    node = insert(node, 3)
    node = insert(node, 15)
    node = insert(node, 1)
    node = insert(node, 6)
    node = insert(node, 12)
    node = insert(node, 9)
    node = insert(node, 10)
    node = insert(node, 11)
    print(node)
    node.assertParentLinks()
    print("------------")
    node = delete(node, node.right)
    print(node)
    node.assertParentLinks()
    print("------------")
    n = minimum(node)
    while n is not None:
        print(n.key)
        n = successor(n)

