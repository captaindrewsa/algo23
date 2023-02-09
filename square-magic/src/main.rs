use colored::Colorize;

fn main() {
    let point = "   ".white();
    let dot = "X  ".blue();
    let x_axis = "|  ".yellow();
    let y_axis = "-  ".yellow();

    // println!("{}\n", -10i8);
    
    // for elem in -10i8..10 {
    //     let elem = f32::from(elem) * 0.1;
    //     println!("{elem}");
    // }
    
    
    
    /* Дробный ренж для тригонометрии */
    
    // for y_fmt in (-10i8..10).rev(){
    //     for x_fmt in -10i8..10{
    //         let x = ((f32::from(x_fmt) * 0.1)* 10.0_f32.powi(1)).round()/10.0_f32.powi(1);
    //         let y = ((f32::from(y_fmt) * 0.1)* 10.0_f32.powi(1)).round()/10.0_f32.powi(1);
    //         // println!("{x} ===={y}");
            
    //         if  /* x == y  */  x.sin() >= y {
    //             print!("{}", dot);
    //         } else if x==0.0 {
    //             print!("{}", x_axis);
    //         } else if y==0.0 {
    //             print!("{}", y_axis);
    //         } else {
    //             print!("{}", point);
    //         }
    //     }
    //     println!();
    // }

    /* Целочисленный ренж для простых функций*/
    for y in (-25..25).rev(){
        for x in -25..25{
            // println!("{x}{y}");
            if (x as f32 - y as f32).abs() >10.0 {
                print!("{}", dot);
            } else if x==0{
                print!("{}", x_axis);
            } else if y==0{
                print!("{}", y_axis);
            } else {
                print!("{}", point);
            }
        }
        println!();
    }

    // let mut tmp = String::new();
    // stdin().read_line(&mut tmp).unwrap();
}



