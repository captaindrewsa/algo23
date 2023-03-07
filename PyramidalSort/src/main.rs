use PyramidalSort::SelectionSort;


fn main() {
    const VECTOR_SIZE: i64 = 100;
    let test_vec = (0..VECTOR_SIZE)
        .map(|_| rand::random::<u8>())
        .collect::<Vec<u8>>();

    // println!("{:#?}", SelectionSort(&test_vec));
    

}
