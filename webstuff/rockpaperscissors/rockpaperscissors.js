// Rock Paper Scissors
// Play rock paper scissors against the computer

// Steps:
// - generate a random number from 1 to 3 and output it
// - depending on the number, output computer chose rock, paper, scissors

// - ask the user to choose rock paper or scissors
// - check to see if the user chose rock
// - if they did then check what the computer randomly chose
// - output whether the user won loss or tied
// - turn this into a function and call the function if the user chose "rock"

// - repeat for paper and scissors

// Bonus:
// - add score and repeat
// - add point when they win, take point away when they lose

const prompt = require("prompt-sync")();

function cpuOutcome() {
  if (cpu === 1) {
    console.log("CPU chose rock!");
  } else if (cpu === 2) {
    console.log("CPU chose paper!");
  } else {
    console.log("CPU chose scissors!");
  }
}

function rockResults() {
  if (cpu === 1) {
    console.log("CPU chose rock! Tied game!");
  } else if (cpu === 2) {
    console.log("CPU chose paper! You lose!");
  } else {
    console.log("CPU chose scissors! You win!");
  }
}

function paperResults() {
  if (cpu === 1) {
    console.log("CPU chose rock! You win!");
  } else if (cpu === 2) {
    console.log("CPU chose paper! Tied game!");
  } else {
    console.log("CPU chose scissors! You lose!");
  }
}

function scissorResults() {
  if (cpu === 1) {
    console.log("CPU chose rock! You lose!");
  } else if (cpu === 2) {
    console.log("CPU chose paper! You win!");
  } else {
    console.log("CPU chose scissors! Tied game!");
  }
}

let cpu = parseInt(Math.random() * 3 + 1);
let user = prompt("Enter your move: (rock, paper, or scissors) ");

console.log("You chose", user);
cpuOutcome();

if (user === "rock") {
  rockResults();
} else if (user === "paper") {
  paperResults();
} else {
  scissorResults();
}
