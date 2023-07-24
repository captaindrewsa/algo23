pub fn BubbleSort(vec: &Vec<u8>) -> Vec<u8> {
    let mut sorted_vec = vec.clone();
    let mut max_non_sorted_idx = sorted_vec.len() - 1;
    while max_non_sorted_idx > 0 {
        for idx in 0..max_non_sorted_idx {
            if sorted_vec[idx] <= sorted_vec[idx + 1] {
                continue;
            } else {
                let tmp = sorted_vec[idx];
                sorted_vec[idx] = sorted_vec[idx + 1];
                sorted_vec[idx + 1] = tmp;
            }
        }
        max_non_sorted_idx -= 1;
    }
    return sorted_vec;
}

pub fn InsertionSort(vec: &Vec<u8>) -> Vec<u8> {
    let mut sorted_vec = vec.clone();
    for mut mileidx in 1..sorted_vec.len() {
        while mileidx > 0 {
            if sorted_vec[mileidx] < sorted_vec[mileidx - 1] {
                let tmp = sorted_vec[mileidx - 1];
                sorted_vec[mileidx - 1] = sorted_vec[mileidx];
                sorted_vec[mileidx] = tmp;
                mileidx -= 1;
            } else {
                break;
            }
        }
    }

    return sorted_vec;
}

pub fn ShellSort(vec: &Vec<u8>) -> Vec<u8> {
    let mut sorted_vector = vec.clone();
    let mut step: usize = vec.len() / 2;
    
    while step > 0 {
        for mut idx in step..vec.len() {
            while idx >= step && sorted_vector[idx - step] > sorted_vector[idx] {
                let tmp = sorted_vector[idx];
                sorted_vector[idx] = sorted_vector[idx - step];
                sorted_vector[idx - step] = tmp;
                idx -= step;
            }
        }
        step /= 2;
    }

    return sorted_vector;
}
