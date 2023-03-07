pub fn SelectionSort(vec: &Vec<u8>) -> Vec<u8>{
    let mut sorted_vec = vec.clone();
    for idx in 0..sorted_vec.len(){
        let mut new_item =sorted_vec[idx]; //новый самый маленький итем
        let mut new_idx = idx; //Индекс самого маленького
        
        for non_sotded_idx in (idx+1)..sorted_vec.len(){
            if new_item>sorted_vec[non_sotded_idx]{
                new_item = sorted_vec[non_sotded_idx];
                new_idx = non_sotded_idx;
                continue;
            } else {
                continue;
            }
        }
        sorted_vec[new_idx] = sorted_vec[idx];
        sorted_vec[idx] = new_item;
         
    }
    return sorted_vec
}