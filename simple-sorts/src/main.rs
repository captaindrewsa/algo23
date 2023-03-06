use simple_sorts::{BubbleSort, InsertionSort};

fn main() {
    let test_vec = vec![1,5,3,45,7,7,4,3,5,7,8,0,76,4];
    // println!("{:#?}", BubbleSort(&test_vec));
    println!("{:#?}", InsertionSort(&test_vec));
}
