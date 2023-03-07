use rand;
use simple_sorts::{BubbleSort, InsertionSort, ShellSort};

fn main() {
    const VECTOR_SIZE: i64 = 100;
    let test_vec = (0..VECTOR_SIZE)
        .map(|_| rand::random::<u8>())
        .collect::<Vec<u8>>();
    // println!("{:#?}", BubbleSort(&test_vec));
    // println!("{:#?}", InsertionSort(&test_vec));
    println!("{:#?}", ShellSort(&test_vec));
}

// [1,2,3,4,5,6,7,8,9,10]
