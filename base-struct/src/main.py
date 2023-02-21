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
        if self.array.__len__()>idx & idx>=0:
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
        if self.array.__len__()>idx & idx>=0:
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
