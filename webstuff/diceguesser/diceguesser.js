const prompt = require("prompt-sync")(); // import prompt to allow us to ask the user for user input in the terminal

let dice = parseInt(Math.random() * 6 + 1); // generate a random number, multiply the number by 6 to get the range between 0 and 5, add 1 to update the range between 1 and 6. Turn the number from a decimal into an integer. Store it all in dice.

// console.log(dice); // temporarily output the dice to test our code.

let guess = prompt("What do you think the dice rolled? Enter your guess: "); // Ask the user for their guess using the prompt function we imported earlier. Prompt returns a string (Think input in Python)
guess = parseInt(guess); // Turn the user's guess into a number to allow us to compare values. While the check can use ==, we should be consistent with teaching our students about types being the same when comparing values or they will likely make more mistakes around types comparisons later.

if (guess === dice) {
  // check if the user guessed the number rolled by the dice
  console.log("Correct! You got it!"); // if it was, output correct
} else {
  // if the user guessed incorrectly, output the message informing them that they were wrong.
  console.log("Good try, unfortunately it was", dice);
}
