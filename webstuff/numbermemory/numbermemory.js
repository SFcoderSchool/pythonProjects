// Number Memory Game
//

const prompt = require("prompt-sync")();

let numbers = "";

while (true) {
  let randomnum = parseInt(Math.random() * 10);
  numbers = numbers + randomnum;

  console.log(numbers);
  prompt("Enter when ready:");

  console.clear();
  let user = prompt("What was the number string? ");

  if (user === numbers) {
    console.log("correct");
  } else {
    console.log("incorrect");
    console.log("correct answer was", numbers);
    break;
  }
}
