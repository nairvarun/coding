fn main() {
    'c: for c in 1..1000 {
        for b in 1..c {
            for a in 1..b {
                if a*a + b*b == c*c {
                    if a + b + c == 1000 {
                        println!("{}", a*b*c);
                        break 'c;
                    }
                }
            }
        }
    }
}