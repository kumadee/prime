use primegen::count_prime;
use std::env;
use std::sync::mpsc;
use std::thread;

mod primegen;

fn create_chunks(num: u32, size: u8) -> Vec<u32> {
    let mut result = Vec::with_capacity(usize::from(size));
    let chunk_size = num / (size as u32);
    for i in 0..(size as u32) {
        let last_value = if i + 1 == (size as u32) {
            (i + 1) * chunk_size + (num % (size as u32))
        } else {
            (i + 1) * chunk_size
        };
        result.push(last_value);
    }
    return result;
}

fn main() {
    let threads: u8 = 4;
    let (tx, rx) = mpsc::channel();
    let args: Vec<String> = env::args().collect();
    if args.len() > 1 {
        if let Ok(limit) = &args[1].parse() {
            let mut c: u32 = 0;
            let chunks = create_chunks(*limit, threads);
            for t in 0..threads {
                let start = if 0 == t {
                    0
                } else {
                    chunks[usize::from(t) - 1] + 1
                };
                let num = chunks[usize::from(t)];
                let tx1 = tx.clone();
                thread::spawn(move || {
                    let z = count_prime(num, start, false);
                    tx1.send(z).unwrap();
                });
            }
            // FIXME: workaround to close the receiver
            thread::spawn(move || {
                tx.send(0).unwrap();
            });

            for recvd in rx {
                c += recvd;
            }
            println!("Total primes for {} natural numbers is {}.", limit, c);
        }
    }
}
