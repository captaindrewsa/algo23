pub fn simple_solver_for_six() -> i32 {
    let mut count = 0;
    for a1 in 0..=9 {
        for a2 in 0..=9 {
            for a3 in 0..=9 {
                for b1 in 0..=9 {
                    for b2 in 0..=9 {
                        for b3 in 0..=9 {
                            if a1 + a2 + a3 == b1 + b2 + b3 {
                                count += 1;
                            } else {
                                continue;
                            }
                        }
                    }
                }
            }
        }
    }

    return count;
}
// Ественственно он не работает)
pub fn simple_solver_for_ten() -> i32 {
    let mut count = 0;
    for a1 in 0..=9 {
        for a2 in 0..=9 {
            for a3 in 0..=9 {
                for a4 in 0..=9 {
                    for a5 in 0..=9 {
                        for b1 in 0..=9 {
                            for b2 in 0..=9 {
                                for b3 in 0..=9 {
                                    for b4 in 0..=9 {
                                        for b5 in 0..=9 {
                                            if a1 + a2 + a3 + a4 + a5 == b1 + b2 + b3 + b4 + b5 {
                                                count += 1;
                                            } else {
                                                continue;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return count;
}

pub fn test_recursion(number_in_row: i32) -> i32 {
    struct FibonaciCond {
        value_now: i32,     //5 8
        value_before1: i32, //3 5
        value_before2: i32, //2 3
        ordinal_number: i32,
    }

    impl Default for FibonaciCond {
        fn default() -> Self {
            Self {
                value_now: 1,
                value_before1: 1,
                value_before2: 0,
                ordinal_number: 3,
            }
        }
    }

    impl FibonaciCond {
        fn calculate(&self) -> Self {
            let res = self.value_before1 + self.value_before2;
            Self {
                value_now: res,
                value_before1: self.value_now,
                value_before2: self.value_before1,
                ordinal_number: self.ordinal_number + 1,
            }
        }
    }

    let mut stack_of_task: Vec<FibonaciCond> = Vec::new();

    while stack_of_task.len() > 0 {
        let task = stack_of_task.pop().unwrap();
        if task.ordinal_number == number_in_row {}
    }

    return 0;
}
