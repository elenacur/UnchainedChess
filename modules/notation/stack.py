class Stack:
    def __init__(self, capacity=None):
        self.__items = [] #list of the items in the stack
        self.__capacity = capacity

    #getters
    def get_items(self):
        return self.__items
    
    def get_capacity(self):
        return self.__capacity

    #setters
    def set_items(self, p_items):
        self.__items = p_items

    def set_capacity(self, p_capacity):
        self.__capacity = p_capacity


    #methods

    #adds an item to the top of the stack
    def push(self, item):
        if self.is_full():
            print("Stack is full")
        else:
            self.__items.append(item)

    #removes the item at the top of the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.__items.pop() #return and remove top item
    
    #returns the item at the top of the stack
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.__items[-1]

    #checks if the stack is empty
    def is_empty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    #checks if the stack is full
    def is_full(self):
        if self.__capacity == None:
            return False
        if len(self.__items) >= self.__capacity:
            return True

    #returns the size of the stack
    def size(self):
        return len(self.__items)

    #outputs the items in the stack to the console
    def print_stack(self):
        return ("Stack: " + str(self.__items))
