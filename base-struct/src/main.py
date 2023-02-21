class SingleArray():
    array = []
    
    def add(self, item, idx):
        if self.array.__len__() == 0:
            new_array = [ None for _ in range(idx+1)]
            new_array[idx] = item
            self.array = new_array
        
        elif self.array.__len__()-1 < idx:
            new_array = [ None for _ in range(idx+1)]
            tmp_idx = 0
            for elem in self.array:
                new_array[tmp_idx] = elem
                tmp_idx+=1

            for _ in range(idx - self.array.__len__()):
                new_array[tmp_idx] = None
                tmp_idx+=1

            new_array[tmp_idx] = item
            self.array = new_array
        
        elif self.array.__len__() > idx >= 0:
            new_array = [None for _ in range(self.array.__len__())]
            tmp_idx = 0
            for elem in self.array:
                if tmp_idx != idx:
                    new_array[tmp_idx] = elem
                    tmp_idx+=1
                else:
                    new_array[tmp_idx] = item
                    tmp_idx+=1
            self.array = new_array
        else:
            print("Index out of range")
    
    def remove(self, idx):
        if self.array.__len__()>idx and idx>=0:
            new_array = [None for _ in range(self.array.__len__()-1)]
            tmp_item = self.array[idx]
            tmp_idx = 0
            for elem in self.array:
                if idx == tmp_idx:
                    tmp_idx+=1
                    continue
                else:
                    new_array[tmp_idx-1] = elem
                    tmp_idx+=1
            self.array = new_array
            return tmp_item
        else:
            return IndexError

class VectorArray():
    array = []
    size_coeff = 5

    def add(self, item, idx):
        if self.array.__len__() == 0:
            new_array = [ None for _ in range(idx+self.size_coeff)]
            new_array[idx] = item
            self.array = new_array
        
        elif self.array.__len__()-1 < idx:
            new_array = [ None for _ in range(idx+self.size_coeff)]
            tmp_idx = 0
            for elem in self.array:
                new_array[tmp_idx] = elem
                tmp_idx+=1

            for _ in range(idx - self.array.__len__()):
                new_array[tmp_idx] = None
                tmp_idx+=1

            new_array[tmp_idx] = item
            self.array = new_array
        
        elif self.array.__len__() > idx >= 0:
            new_array = [None for _ in range(self.array.__len__())]
            tmp_idx = 0
            for elem in self.array:
                if tmp_idx != idx:
                    new_array[tmp_idx] = elem
                    tmp_idx+=1
                else:
                    new_array[tmp_idx] = item
                    tmp_idx+=1
            self.array = new_array
        else:
            print("Index out of range")

    def remove(self, idx):
        if self.array.__len__()>idx and idx>=0:
            new_array = [None for _ in range(self.array.__len__()-1)]
            tmp_item = self.array[idx]
            tmp_idx = 0
            for elem in self.array:
                if idx == tmp_idx:
                    tmp_idx+=1
                    continue
                else:
                    new_array[tmp_idx-1] = elem
                    tmp_idx+=1
            self.array = new_array
            return tmp_item
        else:
            return IndexError

class FactorArray():
    array = []
    size_coeff = 2

    def add(self, item, idx):
        if self.array.__len__() == 0:
            new_array = [ None for _ in range(idx*self.size_coeff)]
            new_array[idx] = item
            self.array = new_array
        
        elif self.array.__len__()-1 < idx:
            new_array = [ None for _ in range(idx*self.size_coeff)]
            tmp_idx = 0
            for elem in self.array:
                new_array[tmp_idx] = elem
                tmp_idx+=1

            for _ in range(idx - self.array.__len__()):
                new_array[tmp_idx] = None
                tmp_idx+=1

            new_array[tmp_idx] = item
            self.array = new_array
        
        elif self.array.__len__() > idx >= 0:
            new_array = [None for _ in range(self.array.__len__())]
            tmp_idx = 0
            for elem in self.array:
                if tmp_idx != idx:
                    new_array[tmp_idx] = elem
                    tmp_idx+=1
                else:
                    new_array[tmp_idx] = item
                    tmp_idx+=1
            self.array = new_array
        else:
            print("Index out of range")

    def remove(self, idx):
        if self.array.__len__()>idx and idx>=0:
            new_array = [None for _ in range(self.array.__len__()-1)]
            tmp_item = self.array[idx]
            tmp_idx = 0
            for elem in self.array:
                if idx == tmp_idx:
                    tmp_idx+=1
                    continue
                else:
                    new_array[tmp_idx-1] = elem
                    tmp_idx+=1
            self.array = new_array
            return tmp_item
        else:
            return IndexError 

class MatrixArray():
    # Учитывая, что переменные в python - ссылки, то можно просто хранить список переменных, в которых лежат списки с данными
    pointer_arary = []
    max_size_data_array = 10
    
    
#  [0   [0  1  2  3  4  5  6  7  8  9]      
#  1    [10 11 12 13 14 15 16 17 18 19]
#  2]   [20 21 22 23 24 25 26 27 28 29]    

    def add(self, item, idx):    
        if self.pointer_arary.__len__() == 0:
            tmp = 0
            while tmp<=idx//self.max_size_data_array:
                data_array = [None for _ in range(self.max_size_data_array)]
                
                tmp+=1
            




    def remove(self, idx):
        return 200
    

# c = VectorArray()
# c.add("dog",0)
# c.add("cat", 2)
# c.add("parrot", 5)
# c.add("OLYA", 2)
# print(c.remove(0))
# print(c.array)

# b = VectorArray()
# b.add("dog",0)
# b.add("cat", 2)
# b.add("parrot", 5)
# b.add("OLYA", 2)
# print(b.remove(0))
# print(b.array)


# a = SingleArray()
# a.add("dog",2)
# a.add("cat", 4)
# a.add("parrot", 5)
# a.add("OLYA", 2)
# print(a.array)
# print(a.remove(2))
# print(a.array)
