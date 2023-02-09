fn main() {
    // basic
    println!("Hello, world!");
    // formating
    println!("Hello, {}", "Jon");
    // expressions
    println!("3+6={}", 3+6);
    // positions
    println!("{0} has a {1} and {0}", "Jon", 29);
    // named pos
    println!("{jon} is {factor}", jon=1, factor=2);
    // traits
    println!("b:{:b}, h:{:x}, o:{:o}",50,50,50);

}
