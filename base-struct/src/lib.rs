use std::fmt::Display;

pub struct SingleArray<T> {
    array: [T;0]
}

impl<T> SingleArray<T>{
    pub fn new()-> Self{
        SingleArray{
            array: [],
        }
    }

    fn is_empty(&mut self)-> bool{
        if self.array.len()==0{
            true
        } else {
            false
        }
    }

    fn add_one_field_and_copy(&mut self){
    }
}

impl<T> IArray<T> for SingleArray<T>{
    fn add(&mut self, item: T, idx: usize) {
        if self.is_empty(){
        }
    }

    fn remove(&mut self, idx: i32) -> T {
        todo!()
    }
}

pub struct VectorArray {}

pub struct FactorArray {}

pub struct MatrixArray {}

pub trait IArray<T> {
    fn add(&mut self, item: T, idx: usize);
    fn remove(&mut self, idx: i32) -> T;
}
