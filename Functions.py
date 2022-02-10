# *** In the name of Allah ***
def func2(self):
    """<< < Dashboard >> >
    Choose any- 1.InsertFront
                  2.InsertLast
                  3.InserAt
                  4.InsertBeforeValue
                  5.InsertSortedOrder
                  6.UpdateFront
                  7.UpdateLast
                  8.UpdateAt
                  9.UpdateValue
                  10.DeleteFront
                  11.Deletelast
                  12.DeleteAt
                  13.DeleteValue
                  14.SearchIndexOfValue
                  15.ValueOfIndex
                  16.Printlist
                  17.Exit"""
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev = None

class circularDoublyLinkedList:
    def __init__(self):
        self.head=None
    def listlength(self):
        if self.head is None:
            return 0
        currentnode=self.head
        length=0
        while True:
            length+=1
            currentnode=currentnode.next
            if currentnode==self.head:
                break
        return length

    def insertFront(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node

        else:
            new_node = node(data)
            self.head.prev = new_node
            new_node.next = self.head
            cur=self.head
            while True:
                cur=cur.next
                if cur.next==self.head:
                    return
            self.head=new_node
            cur.next=self.head
            self.head.prev=cur.next

    def insertLast(self, data):
        new_node=node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            cur=self.head
            while True:
                cur=cur.next
                if cur.next==self.head:
                    break
            cur.next=new_node
            new_node.prev=cur
            new_node.next=self.head
            self.head.prev=new_node.next
    def insertAt(self,data,position):
        new_node = node(data)
        if position < 1 or position > self.listlength():
            print(position, "is Invalid position")
        elif position == 1:
            self.insertFront(data)
        else:
            cur = self.head
            c = 0
            while cur.next:
                if c == position - 1:
                    prev = cur.prev
                    prev.next = new_node
                    new_node.next = cur
                    new_node.prev = prev
                    cur.prev = new_node
                    return
                c += 1
                cur = cur.next
    def insertBeforeValue(self,position,data):
        # if position < 0 or position >= self.listlength():
        #     print(position, "is Invalid position")
        #     return
        cur=self.head
        c=0
        while cur:
            if cur.data==position: #c==0 and
                self.insertFront(data)
                return
            elif cur.data==data:
                new_node=node(data)
                prev=cur.prev
                prev.next=new_node
                cur.prev = new_node
                new_node.next=cur
                new_node.prev=prev
                return
            cur=cur.next
            #c=1
        print("The value does not exist.")

    def insertSortedOrder(self,data):
        if self.head == None:
            return
        else:
            current = self.head
            while current.next:
                nxt= current.next;
                while nxt:
                    if current.data > nxt.data:
                        current.data,nxt.data = nxt.data,current.data
                    nxt = nxt.next
                current = current.next

        current = None
        new_node=node(data)

        if self.head == None:
            head.self = new_node

        elif self.head.data >= new_node.data:
            new_node.next = self.head
            new_node.next.prev = new_node
            self.head = new_node

        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next

            new_node.next = current.next

            if current.next:
                new_node.next.prev = new_node

            current.next = new_node
            new_node.prev = current

    def deleteFront(self):
        cur=self.head
        if cur.next==self.head:
            cur=None
            self.head=None
            return
        else:
            nxt=cur.next
            while True:
                cur = cur.next
                if cur.next== self.head:
                    break
            cur.next=nxt
            nxt.prev=cur.next
            self.head.next=nxt
            self.head.prev=cur.next
            cur=None
            self.head=nxt
            return
        print("Value is deleted successfully.")

    def deleteLast(self):
        cur = self.head
        while True:
            cur = cur.next
            if cur.next == self.head:
                break
        prev = cur.prev
        prev.next = self.head
        self.head.prev=prev
        cur.prev = None
        cur.next=None
        cur = None
        print("Value is deleted successfully.")

    def deleteValue(self,key):
        cur = self.head
        c=0
        while True:
            if cur.data==key and cur==self.head:
                c=1
                if cur.next==self.head:
                    cur = None
                    self.head = None
                    return
                else:
                   self.deleteFront()
                   return
            elif cur.data==key:
                c=1
                nxt=cur.next
                prev=cur.prev
                prev.next=nxt
                nxt.prev=prev
                cur.prev=None
                cur.next=None
                cur=None
                return

            elif cur.data==key and cur.next== self.head:
                c=1
                self.deleteLast()
                break
                return
            cur = cur.next
        if c==0:
            print("The value is not present in the list.")
            return
        print("Value is deleted successfully.")

    def deleteAt(self,position):
        cur = self.head
        if position<0 or position>self.listlength():
            print(position,"is Invalid position")
        elif position == 1:
            self.deleteFront()
            return
        elif position==self.listlength():
            self.deleteLast()
            return
        else:
            c = 0
            while True:
                if c == position - 1:
                    prev = cur.prev
                    prev.next = cur.next
                    cur.next.prev=prev
                    cur.next=None
                    cur.prev=None
                    cur=None
                    return
                c += 1
                cur = cur.next
                if cur==self.head:
                    break
        print("Value is deleted successfully.")

    def printList(self):
        l=self.listlength()
        if l:
            cur=self.head
            while True:
                print(cur.data,end=" ")
                cur=cur.next
                if cur==self.head:
                    print()
                    break
        else:
            print("List is empty",end="\n")

    def searchIndexOfValue(self,position):
        if position<0 or position>=self.listlength():
            print(position,"is Invalid position")
            return
        cur=self.head
        length=0
        while True:
            if length==position:
                print("The value of the position ",position,"is",cur.data)
                return
            length+=1
            cur=cur.next
            if cur==self.head:
                break

    def valueOfIndex(self,value):
        cur = self.head
        length = 0
        while True:
            if cur.data == value:
                print("The index of the value ", value,"is", length)
                return
            length += 1
            cur = cur.next
            if cur==self.head:
                break
        print("The value does not exist.")

    def updateFront(self, data):
        cur = self.head
        cur.data = data
        print("Value is updated successfully.")

    def updateLast(self, data):
        cur = self.head
        while True:
            cur = cur.next
            if cur.next==self.head:
                break
        cur.data = data
        print("Value is updated successfully.")

    def updateAt(self, position, data): # 0 indexed
        if position < 0 or position >= self.listlength():
            print(position, "is Invalid position")
            return
        cur = self.head
        length = 0
        while True:
            if length == position:
                cur.data = data
                return
            length += 1
            cur = cur.next
            if cur==self.head:
                break
        print("Value is updated successfully.")

    def updateValue(self, value, update_value):
        cur = self.head
        c=0
        while True:
            if cur.data == value:
                c=1
                cur.data = update_value
                print("Value is updated.")
                return
            cur = cur.next
            if cur==self.head:
                break
        if c==0:
            print("The value is not present in the list.")
        print("Value is updated successfully.")

dlist=circularDoublyLinkedList()
print(func2.__doc__)
while True:
    choice = int(input())
    if choice==1:
        b=input("Enter the number: ")
        dlist.insertFront(b)
    elif choice==2:
        b = input("Enter the number: ")
        dlist.insertLast(b)
    elif choice==3:
        b=input("Enter the data: ")
        c=int(input("Enter the position: "))
        dlist.insertAt(b,c)
    elif choice == 4:
        b = int(input("Enter the position: "))
        c = input("Enter the new data you want to add: ")
        dlist.insertBeforeValue(b,c)
    elif choice == 5:
        b = input("Enter the new data: ")
        dlist.insertSortedOrder(b)
    elif choice == 6:
        b = input("Enter the data you want to update: ")
        dlist.updateFront(b)
    elif choice == 7:
        b = input("Enter the data you want to update: ")
        dlist.updateLast(b)
    elif choice == 8:
        b = input("Enter the data you want to update: ")
        c=int(input("Enter the position where you want to update: "))
        dlist.updateAt(c,b)
    elif choice == 9:
        b = input("Enter the data you want to update: ")
        c = input("Enter the new data: ")
        dlist.updateValue(b,c)
    elif choice == 10:
        dlist.deleteFront()
    elif choice == 11:
        dlist.deleteLast()
    elif choice == 12:
        b = int(input("Enter the deleted position: "))
        dlist.deleteAt(b)
    elif choice == 13:
        b = input("Enter the data you want to delete: ")
        dlist.deleteValue(b)
    elif choice == 14:
        b = int(input("Enter the position to get value: "))
        dlist.searchIndexOfValue(b)
    elif choice == 15:
        b = input("Enter the value to get index: ")
        dlist.valueOfIndex(b)
    elif choice == 16:
        dlist.printList()
    else:
        print("The programme is exiting")
        exit()

