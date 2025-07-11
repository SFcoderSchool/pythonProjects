// Coin Flip
// Flip a coin many times

// Steps:
// 1. generate a random number from 0 to 1
// 2. output the number
// 3. output "heads" or "tails" depending on the number

// 4. add a loop to repeat forever
// 5. create variables to count how many heads appeared
// 6. create variables to count how many tails appeared
// 7. increment to variables respectively where they appear

// 8. stop the loop after a certain amount of repeats
// 9. output the results

let heads = 0;
let tails = 0;
let rounds = 100;
let currentRound = 0;

while (true) {
  currentRound = currentRound + 1;
  let coin = parseInt(Math.random() * 2);
  if (coin === 0) {
    console.log("Heads");
    heads = heads + 1;
  } else {
    console.log("Tails");
    tails = tails + 1;
  }

  if (currentRound === rounds) {
    break;
  }
}

console.log();
console.log(
  "After",
  rounds,
  "rounds",
  heads,
  "heads were flipped and",
  tails,
  "tails were flipped."
);
