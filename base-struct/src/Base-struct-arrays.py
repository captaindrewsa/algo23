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
            new_array = [ None for _ in range((idx+1)*self.size_coeff)]
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
            for main_idx in range(self.array.__len__()):
                if tmp_idx == main_idx == idx:
                    continue
                else:
                    new_array[tmp_idx] = self.array[main_idx]
                    tmp_idx+=1
            self.array = new_array
            return tmp_item
        else:
            return IndexError 

class MatrixArray():
    # Учитывая, что переменные в python - ссылки, то можно просто хранить список переменных, которые отсылают списки с данными
    pointer_arary = []
    max_size_data_array = 10
    
    
#  [0   [0  1  2  3  4  5  6  7  8  9]      
#  1    [10 11 12 13 14 15 16 17 18 19]
#  2]   [20 21 22 23 24 25 26 27 28 29]    

    def add(self, item, idx):    
        if self.pointer_arary.__len__() == 0:
            # Создание хранилища с нуля и вставка в нужное место
            tmp = 0
            while tmp<=idx//self.max_size_data_array:
                self.apepnd_new_layer()
                tmp+=1
            self.pointer_arary[idx//self.max_size_data_array][idx%self.max_size_data_array] = item
        
        elif self.pointer_arary.__len__()+self.max_size_data_array < idx:
            # Сделать добавление недостающих слоев и вставку в нужное место
            for _ in range(idx//self.max_size_data_array+1 - self.pointer_arary.__len__()):
                self.apepnd_new_layer()
            self.pointer_arary[idx//self.max_size_data_array][idx%self.max_size_data_array] = item
            
        elif self.pointer_arary.__len__()*self.max_size_data_array > idx >= 0:
            # Сделать вставку в нужные координаты
            # tmp_new_pointer_array = [[None for _ in range(self.max_size_data_array)] for _ in range(self.pointer_arary.__len__())]
            # tmp_idx = 0
            # for new_main_idx in range(self.pointer_arary.__len__()*self.max_size_data_array+1):
            #     if tmp_idx== idx == new_main_idx:
            #         tmp_new_pointer_array[new_main_idx//self.max_size_data_array][new_main_idx%self.max_size_data_array] = item
            #     else:
            #         try:
            #             tmp_new_pointer_array[new_main_idx//self.max_size_data_array][new_main_idx%self.max_size_data_array] = self.pointer_arary[tmp_idx//self.max_size_data_array][tmp_idx%self.max_size_data_array] 
            #         except IndexError:
            #             if self.pointer_arary[tmp_idx//self.max_size_data_array][tmp_idx%self.max_size_data_array] == None:
            #                 continue
            #             else:
            #                 # Добавление нового слоя в конец
            #                 new_layer = [None for _ in range(self.max_size_data_array)]
            #                 new_pointer_array = [None for _ in range(tmp_new_pointer_array.__len__()+1) ]
            #                 tmp2_idx = 0
            #                 for elem in tmp_new_pointer_array:
            #                     new_pointer_array[tmp2_idx]= elem
            #                     tmp2_idx+=1
            #                 new_pointer_array[tmp2_idx]=new_layer
                            
            #                 new_pointer_array[new_pointer_array.__len__()] = [None for _ in range(self.max_size_data_array)]
            #                 new_pointer_array[new_main_idx//self.max_size_data_array][new_main_idx%self.max_size_data_array] = self.pointer_arary[tmp_idx//self.max_size_data_array][tmp_idx%self.max_size_data_array]
            # self.pointer_arary = new_pointer_array
            # IT DOESN'T WORK
            pass
        else:
            print("Index out of range")

    def remove(self, idx):
        pass
    
    def apepnd_new_layer(self):
        new_layer = [None for _ in range(self.max_size_data_array)]
        new_pointer_array = [None for _ in range(self.pointer_arary.__len__()+1) ]
        tmp_idx = 0
        for elem in self.pointer_arary:
            new_pointer_array[tmp_idx]= elem
            tmp_idx+=1
        new_pointer_array[tmp_idx]=new_layer
        self.pointer_arary = new_pointer_array


d =MatrixArray()
# print(d.pointer_arary)
d.add("dog", 0)
d.add("cat", 7)
# d.add("cat", 13)
print(d.pointer_arary)


# c = FactorArray()
# c.add("dog",0)
# c.add("cat", 1)
# c.add("parrot", 2)
# c.add("bug", 9)
# print(c.array)
# print(c.remove(0))
# print(c.array)

# b = VectorArray()
# b.add("dog",0)
# b.add("cat", 2)
# b.add("parrot", 5)
# b.add("bug", 2)
# print(b.remove(0))
# print(b.array)


# a = SingleArray()
# a.add("dog",2)
# a.add("cat", 4)
# a.add("parrot", 5)
# a.add("bug", 2)
# print(a.array)
# print(a.remove(2))
# print(a.array)
