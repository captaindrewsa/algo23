pub fn SelectionSort(vec: &Vec<i32>) -> Vec<i32>{
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

pub fn HeapSort(vec: &Vec<i32>)-> Vec<i32>{

    let mut sorted_vec = vec.clone();

    for idx in 0..=(sorted_vec.len()/2 - 1) {
        //Строим max-heap 
        heapify(idx, sorted_vec.len(), &mut sorted_vec);
    }

    for idx in (0..sorted_vec.len()).rev(){
        let tmp = sorted_vec[0];
        sorted_vec[0] = sorted_vec[idx];
        sorted_vec[idx] = tmp;

        heapify(0, idx, &mut sorted_vec);
    }

    fn heapify(root: usize, size: usize, sorted_vec: &mut Vec<i32>){
        
        let mut Largest = root;
        let Left: usize = (root*2 + 1).try_into().unwrap();
        let Right: usize = (root*2 + 2).try_into().unwrap();
        
        if Left<sorted_vec.len().try_into().unwrap() && sorted_vec[Left]>sorted_vec[Largest]{
            Largest = Left;
        }
        if Right<sorted_vec.len().try_into().unwrap() && sorted_vec[Right]>sorted_vec[Largest]{
            Largest = Right;
        } 
        if Largest==root{
            return;
        }

        let tmp = sorted_vec[Largest];
        sorted_vec[Largest] = sorted_vec[root];
        sorted_vec[root] = tmp;
        
        heapify(Largest, size, sorted_vec);
    }
    
    return sorted_vec;
}