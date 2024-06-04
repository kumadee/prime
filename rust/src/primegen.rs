fn is_prime(num: u32) -> bool {
    // below type casting is not accurate for big integers.
    // let last = (num as f32).sqrt() as u32;
    if num > 2 && num % 2 == 0 {
        return false;
    }

    // for x in (3..=last).step_by(2) {
    for x in (3..).take_while(|y| y * y <= num).step_by(2) {
        if num % x == 0 {
            return false;
        }
    }
    return true;
}

pub fn count_prime(num: u32, start: u32, show: bool) -> u32 {
    let mut count = 1;
    let mut _start: u32 = 3;
    if start > 2 {
        count = 0;
        _start = start;
        if start % 2 == 0 {
            _start += 1;
        }
    }
    for n in (_start..=num).step_by(2) {
        if is_prime(n) {
            count = count + 1;
            if show {
                println!("{}", n);
            }
        }
    }
    return count;
}
