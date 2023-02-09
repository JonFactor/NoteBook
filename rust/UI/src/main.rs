use std::io;
fn main() {
    let mut  input = String::new();
    println!("Say Somthing");

    match io::stdin().read_line(&mut input) {
        Ok(_) => {
            println!("You Said :{}", input);
        },
        Err(e) => {
            println!("ERROR: {}", e);
        }
    }
}
