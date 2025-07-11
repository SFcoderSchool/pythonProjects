// Higher Lower Cards
// generate 'Cards' and see if u can guess 1 card is higher / lower than the other card

// Steps
// - generate 2 random numbers from 1 to 13
// - show 1 of the random numbers
// - ask the user if the shown number is either higher or lower than the hidden number

// - check to see if the user got it correct
// - add a loop to repeat the game
// - keep track of score and number of attempts
// - stop the game when the user guesses 3 correct

const prompt = require("prompt-sync")();

let score = 0;
let attempts = 0;

while (true) {
  hidden_card = parseInt(Math.random() * 13 + 1);
  shown_card = parseInt(Math.random() * 13 + 1);

  console.info("Hidden card: ?");
  console.info("Shown card: " + shown_card);
  let answer = prompt("Higher or lower? ");
  console.info("Hidden card: " + hidden_card);
  attempts = attempts + 1;
  if (answer === "higher") {
    if (hidden_card > shown_card) {
      console.info("Correct!");
      score = score + 1;
    } else {
      console.info("Wrong!");
    }
  } else if (answer === "lower") {
    if (hidden_card < shown_card) {
      console.info("Correct!");
      score = score + 1;
    } else {
      console.info("Wrong!");
    }
  }
  if (score === 3) {
    break;
  }
}

console.info("It took you", attempts, "attempts!");
