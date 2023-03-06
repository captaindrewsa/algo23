
pub fn BubbleSort(vec: &Vec<i32>) -> Vec<i32>{
    let mut sorted_vec = vec.clone();
    let mut max_non_sorted_idx = sorted_vec.len()-1;
    while max_non_sorted_idx>0 {
        for idx in 0..max_non_sorted_idx{
            if sorted_vec[idx]<=sorted_vec[idx+1]{
                continue;
            } else {
                let tmp = sorted_vec[idx];
                sorted_vec[idx] = sorted_vec[idx+1];
                sorted_vec[idx+1] = tmp;
            }
        }
        max_non_sorted_idx-=1;
    }
    return sorted_vec;
}

pub fn InsertionSort(vec: &Vec<i32>) -> Vec<i32>{
    let mut sorted_vec = vec.clone();
    let mut milestone_idx = 2;
    while milestone_idx<sorted_vec.len()-1 {
        
        for idx in (0..milestone_idx).rev(){
            if sorted_vec[milestone_idx]<=sorted_vec[milestone_idx-1]{
                let tmp = sorted_vec[milestone_idx];
                sorted_vec[milestone_idx] = sorted_vec[milestone_idx+1];
                sorted_vec[milestone_idx+1] = tmp;
                continue;
            } else {
                break;
            }
            
        }
        
        
        milestone_idx+=1;
    }


    return sorted_vec;
}