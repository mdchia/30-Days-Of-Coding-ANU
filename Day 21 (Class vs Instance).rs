impl Person {
    fn new(initialAge: i32) -> Person {
        // Add some more code to run some checks on initialAge
        if initialAge < 0 {
            println!("Age is not valid, setting age to 0.");
            return Person { age: 0 };
        } else {
            return Person { age: initialAge };
        }
    }

    fn amIOld(&self) {
        // Do some computations in here and print out the correct statement to the console
        let lb:i32 = 13;
        let ub:i32 = 18;
        if &self.age < &lb {
            println!("You are young.");
        } else if (&lb <= &self.age) && (&self.age < &ub){
            println!("You are a teenager.");
        } else {
            println!("You are old.");
        }
    }

    fn yearPasses(&mut self) {
        // Increment the age of the person in here
        self.age+=1;
    }
}
 
