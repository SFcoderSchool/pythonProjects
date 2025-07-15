// part 1 ----------------------------------------

const prompt = require("prompt-sync")();

let should_continue = true;
while (should_continue === true) {
  let num1 = prompt("Enter your first number: ");
  let op = prompt("Enter your operator: +, -, *, /: ");
  let num2 = prompt("Enter your second number: ");

  num1 = parseFloat(num1);
  num2 = parseFloat(num2);

  if (op === "+") {
    console.log(num1, "+", num2, "=", num1 + num2);
  } else if (op === "-") {
    console.log(num1, "-", num2, "=", num1 - num2);
  } else if (op === "*") {
    console.log(num1, "*", num2, "=", num1 * num2);
  } else if (op === "/") {
    if (num2 === 0) {
      console.log("Cannot divide by 0!");
    } else {
      console.log(num1, "/", num2, "=", num1 / num2);
    }
  }

  let resume = prompt("Continue? [y/n] ");

  if (resume === "n") {
    should_continue = false;
  }
}

// end part 1 ------------------------------------------

// comment out above code and convert to function to use for website

function calc() {
  let n1 = document.getElementById("n1").value;
  let op = document.getElementById("op").value;
  let n2 = document.getElementById("n2").value;

  n1 = parseFloat(n1);
  n2 = parseFloat(n2);

  let result = "";

  if (op == "+") {
    result = n1 + "+" + n2 + "=" + (n1 + n2);
  } else if (op == "-") {
    result = n1 + "-" + n2 + "=" + (n1 - n2);
  } else if (op == "*") {
    result = n1 + "*" + n2 + "=" + n1 * n2;
  } else if (op == "/") {
    result = n1 + "/" + n2 + "=" + n1 / n2;
  }

  document.getElementById("result").innerHTML = result;
}
