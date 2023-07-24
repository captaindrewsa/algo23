use std::{collections::VecDeque};
#[derive(Default)]
struct KeyValueStorage{
    size_storage: u32,
    storage: Vec<VecDeque<(String, i32)>>
}

// impl Default for KeyValueStorage{
//     fn default() -> Self {
//         let mut tmp: Vec<VecDeque<(String, i32)>> = Vec::new();
//         let size_storage = 10u32;

//         Self{ size_storage: size_storage, storage:  }
//     }
// }

impl KeyValueStorage{
    
    pub fn get(&mut self){
        
    }
    
    pub fn add(&mut self, key: &str, value: i32){
        let key_hash = self.get_hash_code(key);
        let position = self.hash(key_hash, self.storage.len() as u32);



    }
    pub fn repl(&mut self){}
    pub fn del(&mut self){}

    fn get_hash_code(&self, string: &str)-> usize{

        let mut sum = 0;
        for char in string.chars(){
            sum+= char as usize;
        }
        
        return sum
    }
    
    fn hash(&mut self, value: usize, lengh_storage: usize)-> usize{
        return value % lengh_storage 
    }

}




fn main() {

    println!("");
}
