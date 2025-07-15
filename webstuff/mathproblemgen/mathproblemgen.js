// math problem generator
// generate a random equation and ask the user to solve it

// Steps
// - generate 2 random numbers and store them in variables
// - output the eqation with the 2 numbers and a "+" in between

// - ask the user to solve the eqation with prompt
// - check to see if the user got it correct
// - NOTE: make sure the data types are the same before comparison

// - repeat for subtraction, multiplication

// - repeat for division
// - NOTE: data type needs to be a float
// - round to the closest 2 decimal points by doing some math

// Bonus
// - add randomness to randomly choose an operator for the equation
// - add a loop and keep track of the total correctly answered equation

const prompt = require("prompt-sync")();

let operator = parseInt(Math.random() * 4 + 1);
let num1 = parseInt(Math.random() * 100 + 1);
let num2 = parseInt(Math.random() * 100 + 1);

if (operator === 1) {
  console.log("Addition problem!");
  let answer = prompt(num1 + "+" + num2 + "= ");
  answer = parseInt(answer);
  if (answer === num1 + num2) {
    console.log("You got it right!");
  } else {
    console.log("Wrong, it was", num1 + num2);
  }
} else if (operator === 2) {
  console.log("Subtraction problem!");
  let answer = prompt(num1 + "-" + num2 + "= ");
  answer = parseInt(answer);
  if (answer === num1 - num2) {
    console.log("You got it right!");
  } else {
    console.log("Wrong, it was", num1 - num2);
  }
} else if (operator === 3) {
  console.log("Multiplication problem!");
  num1 = parseInt(Math.random() * 10 + 1);
  num2 = parseInt(Math.random() * 10 + 1);
  let answer = prompt(num1 + "*" + num2 + "= ");
  answer = parseInt(answer);
  if (answer === num1 * num2) {
    console.log("You got it right!");
  } else {
    console.log("Wrong, it was", num1 * num2);
  }
} else if (operator === 4) {
  console.log("Division problem!");
  num1 = parseInt(Math.random() * 10 + 1);
  num2 = parseInt(Math.random() * 10 + 1);
  let answer = prompt(num1 + "/" + num2 + "= ");
  answer = parseFloat(answer);

  answer = answer * 100;
  answer = Math.round(answer);
  answer = answer / 100;

  if (answer === num1 / num2) {
    console.log("You got it right!");
  } else {
    console.log("Wrong, it was", num1 / num2);
  }
}
