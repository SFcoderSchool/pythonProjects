// Times Table Machine

// start with a basic times table from 1 to 10 and then add prompt
// add complexity with a start and stop
// then make a backwards option
// ask user for which direction they want it
// get rid of direction ask and make it such that it will auto pick up or down depending on the numbers

const prompt = require("prompt-sync")();

function timesTableUp(number, start, stop) {
  console.log(
    "\n--- " + number + " times table (" + start + " to " + stop + ") ---",
  );
  for (let i = start; i <= stop; i++) {
    console.log(number + " x " + i + " = " + number * i);
  }
}

function timesTableDown(number, start, stop) {
  console.log(
    "\n--- " + number + " times table (" + start + " down to " + stop + ") ---",
  );
  for (let i = start; i >= stop; i--) {
    console.log(number + " x " + i + " = " + number * i);
  }
}

let choice = parseInt(prompt("Which times table do you want?"));
let startNum = parseInt(prompt("Start at which number?"));
let stopNum = parseInt(prompt("Stop at which number?"));

// let direction = prompt("Count up or down? Type 'up' or 'down':");

// if (direction === "up") {
//   timesTableUp(choice, startNum, stopNum);
// } else if (direction === "down") {
//   timesTableDown(choice, startNum, stopNum);
// } else {
//   console.log("That wasn't 'up' or 'down' — try again!");
// }

if (start <= stop) {
  timesTableUp(choice, start, stop);
} else {
  timesTableDown(choice, start, stop);
}
