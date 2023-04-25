use std::{collections::LinkedList};
struct KeyValueStorage{
    size_storage: i32,
    storage: Vec<Vec<(String, i32)>>
}

impl Default for KeyValueStorage{
    fn default() -> Self {
        let mut tmp: Vec<Vec<(String, i32)>> = Vec::new();

        Self{ size_storage: todo!(), storage: todo!() }
    }
}

impl KeyValueStorage{
    
    pub fn get(&mut self){}
    pub fn add(&mut self, key: &str, value: i32){
        let key_hash = self.get_hash_code(key);
        let position = self.hash(key_hash, self.storage.len() as u32);


    }
    pub fn repl(&mut self){}
    pub fn del(&mut self){}

    fn get_hash_code(&self, string: &str)-> u32{

        let mut sum = 0;
        for char in string.chars(){
            sum+= char as u32;
        }
        
        return sum
    }
    
    fn hash(&mut self, value: u32, lengh_storage: u32)-> u32{
        return value % lengh_storage 
    }

}




fn main() {
    let mut a: LinkedList<i32> = LinkedList::new();
    a.push_back(255);
    a.push_back(32);
    a.push_back(212312);

    println!("");
}
