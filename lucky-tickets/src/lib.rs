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
