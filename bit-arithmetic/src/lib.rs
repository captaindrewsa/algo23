fn king_move(pos: u32) -> u64{

    let king_position = 1u64 << pos;
    let king_no_a : u64 = 0x101010101010101 & king_position;
    let king_no_h: u64 = 0x8080808080808080 & king_position;
    
    let move_mask = 
    (king_no_a>>7)|(king_position>>8)|(king_no_h>>9)|
    (king_no_a<<1)         |          (king_no_h>>1)|
    (king_no_a<<9)|(king_position<<8)|(king_no_h<<7);
    return move_mask;
}
pub fn king_issue(pos:u32){
    let mut mask = king_move(pos);
    let mut number_of_move=0;
    while mask>0 {
        number_of_move+=mask&1;
        mask = mask>>1;
    }


    println!("{}", king_move(pos));
    println!("{number_of_move}")
}

fn knight_move(pos: u32)-> u64{

    let knight_position = 1u64 << pos;

    
    let move_mask = 
    (knight_position>>6)|(knight_position>>15)|(knight_position>>17)|(knight_position>>10)|
    (knight_position<<6)|(knight_position<<15)|(knight_position<<17)|(knight_position<<10);
    return move_mask;
}
