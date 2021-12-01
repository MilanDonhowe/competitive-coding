/*
  A little bit of Rust for day 1
*/
use std::fs;

fn main() {  
  
  let input = fs::read_to_string("input").unwrap();
  let mut input = input.split('\n').filter(|&x| x.len() > 1);

  let prev_reading: &str = input.next().unwrap();

  let mut prev_reading: i32 = prev_reading.parse::<i32>().unwrap();

  let mut curr_reading: i32;
  let mut increases: i32 = 0;

  for reading in input {
    curr_reading = reading.parse::<i32>().unwrap();

    if curr_reading > prev_reading {
      increases += 1;
    }

    prev_reading = curr_reading;
  }

  println!("Part 1: {}", increases);

  // part 2, sliding window
  let input = fs::read_to_string("input").unwrap();
  let mut input = input.split('\n').filter(|&x| x.len() > 1);

  let mut a: i32 = input.next().unwrap().parse::<i32>().unwrap();
  let mut b: i32 = input.next().unwrap().parse::<i32>().unwrap();
  let mut c: i32 = input.next().unwrap().parse::<i32>().unwrap();
  let mut d: i32;
  increases = 0;

  for reading in input {
    d = reading.parse::<i32>().unwrap();
    
    if b+c+d > a+b+c {
      increases += 1;
    }

    a = b;
    b = c;
    c = d;
  }

  println!("Part 2: {}", increases);

}