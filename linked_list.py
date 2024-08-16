stack = []

class Stack():
    MAX_STACK_LEN = 50
    def __init__(self):
        self.stack_array = [0] * (self.MAX_STACK_LEN / 4)
        self.last_value_index = 0
        
    def reclaim_space(self):
        if len(self.stack_array) > self.MAX_STACK_LEN and len(self.stack_array) > self.last_value_index * 2:
            new_stack = [0] * (len(self.stack_array) / 2)
            for i in range(self.last_value_index):
                new_stack[i] = self.stack_array[i]
            self.stack_array = new_stack
            return True
        return False
                
                
    def pop(self):
        if len(self.stack_array):
            result = self.stack_array[self.last_value_index]
            self.stack_array[self.last_value_index] = None
            self.last_value_index = self.last_value_index - 1
            self.reclaim_space()
            return result
        return False
        
stack = []

def add_val(val):
    stack.append(val)
    return True

def pop_val():
    if len(stack) > 0:
        return stack.pop()
    return False

class SListNode():
    def __init__(self, payload=None, nxt=None):
        self.payload = payload
        self.nxt = nxt

class SLinkList(SListNode):
    def __init__(self):
        super().__init__()
        self.head = self
        self.tail = self
        self.nxt = self.tail
        
    def append(self, payload):
        if payload:
            tail = self.tail
            self.tail = SListNode(payload=payload)
            tail.nxt = self.tail
            return True
        return False
    
    def insert(self, payload, search_payload):
        search_result = self.search(payload=search_payload)
        if search_result:
            node = SListNode(payload=payload)
            node.nxt = search_result.nxt
            search_result.nxt = node
            if search_result == self.tail:
                self.tail = node
            return True
        return False
    
    def search(self, payload):
        return self.recursive_search(payload, self.head.nxt)

    def recursive_search(self, payload, node: SListNode):
        if payload == node.payload:
            return node
        if node == self.tail:
            return False
        return self.recursive_search(payload, node.nxt)
    
    def remove(self, payload):
        if self.head != self.tail:
            prev = self.head
            results = self.remove_search(payload=payload, node=self.head.nxt, prev=prev)
            if results:
                node = results[0]
                prev = results[1]
                prev.nxt = None
                if node != self.tail:
                    prev.nxt = node.nxt
                return node
            
        return False
    
    def remove_search(self, payload, node: SListNode, prev):
        if payload == node.payload:
            return [node, prev]
        if node == self.tail:
            return False
        prev = node
        return self.remove_search(payload, node.nxt, prev)
    
    def pop(self):
        return self.remove(self.tail.payload)
    
    def print_list(self):
        if self.head != self.tail:
            return self.recursive_print(node=self.head.nxt)
        
    def recursive_print(self, node: SListNode):
        print(node.payload)
        if node == self.tail:
            return True
        return self.recursive_print(node=node.nxt)
    
def test_sLinkList():
    empty_ssl = SLinkList()
    def test_append():
        sll = SLinkList()
        test_payload = 'test_payload1'
        
        # append to empty list
        result = sll.append(payload=test_payload)
        assert result
        assert sll.tail.payload == test_payload
        
        # append to non-empty list
        result = sll.append(payload='test_payload2')
        assert result
        assert sll.tail.payload == 'test_payload2'
        
        # append to non-empty list 2
        result = sll.append(payload='test_payload3')
        assert result
        assert sll.tail.payload == 'test_payload3'
        
        return sll
    
    def test_search(empty_ssl: SLinkList, non_empty_sll: SLinkList):
        search_payload = 'found'
        
        # search empty list
        assert empty_ssl.search(search_payload) == False
            
        #search non-empty list
        # find first node
        assert non_empty_sll.search('test_payload1').payload == 'test_payload1'
        # find inner node
        assert non_empty_sll.search('test_payload2').payload == 'test_payload2'
        # find tail
        assert non_empty_sll.search('test_payload3').payload == 'test_payload3'
    
    def test_remove(empty_ssl: SLinkList, non_empty_sll: SLinkList):
        payload_test = 'removed'

        # remove from empty list
        assert empty_ssl.remove(payload_test) == False
        
        # remove tail
        non_empty_sll.append(payload_test)
        assert non_empty_sll.remove(payload_test)
        
        # remove inner
        assert non_empty_sll.remove('test_payload2').payload == 'test_payload2'
        
        # remove first
        assert non_empty_sll.remove('test_payload1').payload == 'test_payload1'
        
        # list with one
        assert non_empty_sll.remove('test_payload3').payload == 'test_payload3'
        
    def test_pop(empty_ssl: SLinkList, non_empty_sll: SLinkList):
        assert empty_ssl.pop() == False
        assert non_empty_sll.pop().payload == 'test_payload3'

    def test_print(empty_ssl: SLinkList, non_empty_sll: SLinkList):
        empty_ssl.print_list()
        non_empty_sll.print_list()
    
    def test_insert(empty_ssl: SLinkList, non_empty_sll: SLinkList):
        assert empty_ssl.insert(payload='test', search_payload='test_payload2') == False
        empty_ssl.print_list()
        
        assert non_empty_sll.insert(payload='test', search_payload='test_payload2') == True
        non_empty_sll.print_list()
        
        assert non_empty_sll.insert(payload='test2', search_payload='test_payload3') == True
        assert non_empty_sll.tail.payload == 'test2'
        non_empty_sll.print_list()
        
    sll = test_append()
    print('Append Test Passed!\n')
    
    test_search(empty_ssl, sll)
    print('Search Test Passed!\n')
    
    test_remove(empty_ssl, sll)
    print('Remove Test Passed!\n')
    
    sll = test_append()
    
    test_pop(empty_ssl, sll)
    print('Pop Test Passed!\n')
    
    sll = test_append()
    
    test_print(empty_ssl=empty_ssl, non_empty_sll=sll)
    print('Print Test Passed!\n')
    
    test_insert(empty_ssl=empty_ssl, non_empty_sll=sll)
    print('Insert Test Passed!\n')
test_sLinkList()