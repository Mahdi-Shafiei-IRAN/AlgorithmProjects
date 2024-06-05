class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        return str(self.val)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self.insert_recursive(self.root, key)

    def insert_recursive(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = TreeNode(key)
            else:
                self.insert_recursive(current_node.left, key)
        else:
            if key > current_node.val:
                if current_node.right is None:
                    current_node.right = TreeNode(key)
                else:
                    self.insert_recursive(current_node.right, key)

    def search(self, key):
        return self.search_recursive(self.root, key)

    def search_recursive(self, current_node, key):
        if current_node is None or current_node.val == key:
            return current_node
        if key < current_node.val:
            return self.search_recursive(current_node.left, key)
        return self.search_recursive(current_node.right, key)

    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)

    def delete_recursive(self, current_node, key):
        if current_node is None:
            return current_node

        if key < current_node.val:
            current_node.left = self.delete_recursive(current_node.left, key)
        elif key > current_node.val:
            current_node.right = self.delete_recursive(current_node.right, key)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            successor = self.min_value_node(current_node.right)
            current_node.val = successor.val
            current_node.right = self.delete_recursive(current_node.right, successor.val)

        return current_node

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self.inorder_recursive(self.root, [])

    def inorder_recursive(self, current_node, result):
        if current_node is not None:
            self.inorder_recursive(current_node.left, result)
            result.append(current_node.val)
            self.inorder_recursive(current_node.right, result)
        return result

    def remove_duplicates_loop(self, lst):
        unique_list = []
        seen = set()
        for item in lst:
            if item not in seen:
                unique_list.append(item)
                seen.add(item)
        return unique_list

    def combine(self, other_bst):
        list1 = self.inorder()
        list2 = other_bst.inorder()
        merged_list = self.merge_sorted_lists(list1, list2)
        merged_list = self.remove_duplicates_loop(merged_list)
        new_bst = BST()
        new_bst.root = self.sorted_list_to_bst(merged_list, 0, len(merged_list) - 1)
        return new_bst

    def merge_sorted_lists(self, list1, list2):
        merged_list = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1

        while i < len(list1):
            merged_list.append(list1[i])
            i += 1

        while j < len(list2):
            merged_list.append(list2[j])
            j += 1
        return merged_list

    def sorted_list_to_bst(self, sorted_list, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        node = TreeNode(sorted_list[mid])
        node.left = self.sorted_list_to_bst(sorted_list, start, mid - 1)
        node.right = self.sorted_list_to_bst(sorted_list, mid + 1, end)
        return node

    def find_next_node(self, key):
        node = self.search(key)
        if node is None:
            return None
        if node.right:
            return self.min_value_node(node.right)
        successor = None
        current = self.root
        while current:
            if current.val > key:
                successor = current
                current = current.left
            elif current.val < key:
                current = current.right
            else:
                break
        return successor

    def find_previous_node(self, key):
        node = self.search(key)
        if node is None:
            return None
        if node.left:
            return self.max_value_node(node.left)
        predecessor = None
        current = self.root
        while current:
            if current.val < key:
                predecessor = current
                current = current.right
            elif current.val > key:
                current = current.left
            else:
                break
        return predecessor

    def max_value_node(self, node):
        current = node
        while current.right:
            current = current.right
        return current


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def print_heap(self):
        print("Max Heap:", self.heap)


if __name__ == "__main__":
    # Create two BSTs
    bst1 = BST()
    bst1.insert(50)
    bst1.insert(30)
    bst1.insert(20)
    bst1.insert(40)
    bst1.insert(70)
    bst1.insert(60)
    bst1.insert(80)

    bst2 = BST()
    bst2.insert(25)
    bst2.insert(15)
    bst2.insert(35)
    bst2.insert(65)
    bst2.insert(75)
    bst2.insert(85)

    bstlist = list()

    bstlist.append(bst1)
    bstlist.append(bst2)

    def rverse_list(lst):
        return lst[::-1]

    while True:
        print("\n1-Create BST\n2-Insert to BST\n3-Delete from BST\n4-Merge two BST\n"
              "5-Create MaxHeap\n6-Search Next Node\n7-Search Previous Node\n8-exit\n")
        command = int(input("enter command: "))

        if command == 1:
            bst = BST()
            bstlist.append(bst)
            print(f"BST{len(bstlist)} is Created.")
        elif command == 2:
            print(f"We have {len(bstlist)} BST's.")
            inp = int(input("which BST? "))
            val = int(input("Enter node: "))
            bstlist[inp-1].insert(val)
            print(f"BST after Insert {val} : {bstlist[inp - 1].inorder()}")
        elif command == 3:
            print(f"We have {len(bstlist)} BST's.")
            inp = int(input("which BST? "))
            val = int(input("Enter node: "))
            bstlist[inp - 1].delete(val)
            print(f"BST after Delete {val} : {bstlist[inp - 1].inorder()}")
        elif command == 4:
            print(f"We have {len(bstlist)} BST's.")
            bst1 = int(input("Select BST1: "))
            bst2 = int(input("Select BST2: "))
            combined = bstlist[bst1 - 1].combine(bstlist[bst2-1])
            print(f"Combined BST : {combined.inorder()}")
        elif command == 5:
            maxheap = MaxHeap()
            inp = int(input("Which BST you want convert to MAXHEAP? "))
            bst_nodes = rverse_list(bstlist[inp-1].inorder())
            for node in bst_nodes:
                maxheap.insert(node)
            maxheap.print_heap()
        elif command == 6:
            print(f"We have {len(bstlist)} BST's.")
            inp = int(input("which BST? "))
            val = int(input("Enter node: "))
            print(f"next node is : {bstlist[inp - 1].find_next_node(val)}")
        elif command == 7:
            print(f"We have {len(bstlist)} BST's.")
            inp = int(input("which BST? "))
            val = int(input("Enter node: "))
            print(f"previous node is : {bstlist[inp - 1].find_previous_node(val)}")
        elif command == 8:
            break
