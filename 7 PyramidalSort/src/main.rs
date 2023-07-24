use PyramidalSort::{SelectionSort, HeapSort};


fn main() {
    const VECTOR_SIZE: i64 = 7;
    let test_vec = (0..VECTOR_SIZE)
        .map(|_| rand::random::<i32>())
        .collect::<Vec<i32>>();

    // println!("{:#?}", SelectionSort(&test_vec));
    println!("{:#?}", HeapSort(&test_vec));

}
