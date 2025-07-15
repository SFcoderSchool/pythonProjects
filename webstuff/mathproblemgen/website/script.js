let num1;
let num2;
let op;

function gen_problem() {
  let problem;
  op = parseInt(Math.random() * 4) + 1;
  if (op == 1) {
    num1 = parseInt(Math.random() * 100) + 1;
    num2 = parseInt(Math.random() * 100) + 1;
    problem = num1 + " + " + num2;
  } else if (op == 2) {
    num1 = parseInt(Math.random() * 100) + 1;
    num2 = parseInt(Math.random() * 100) + 1;
    problem = num1 + " - " + num2;
  } else if (op == 3) {
    num1 = parseInt(Math.random() * 10) + 1;
    num2 = parseInt(Math.random() * 10) + 1;
    problem = num1 + " * " + num2;
  } else if (op == 4) {
    num2 = parseInt(Math.random() * 100) + 1;
    num1 = parseInt(Math.random() * 10) + num2;
    problem = num1 + " / " + num2;
  }

  document.getElementById("problem").innerHTML = problem;
  document.getElementById("question").style.visibility = "visible";
  document.getElementById("feedback").innerHTML = "";
}

function solve() {
  let answer = document.getElementById("answer").value;
  let feedback;
  if (op == 1) {
    if (answer == num1 + num2) {
      feedback = "Correct!";
    } else {
      feedback = "Incorrect! It was " + (num1 + num2);
    }
  } else if (op == 2) {
    if (answer == num1 - num2) {
      feedback = "Correct!";
    } else {
      feedback = "Incorrect! It was " + (num1 - num2);
    }
  } else if (op == 3) {
    if (answer == num1 * num2) {
      feedback = "Correct!";
    } else {
      feedback = "Incorrect! It was " + num1 * num2;
    }
  } else if (op == 4) {
    if (answer == num1 / num2) {
      feedback = "Correct!";
    } else {
      feedback = "Incorrect! It was " + num1 / num2;
    }
  }

  document.getElementById("feedback").innerHTML = feedback;
}
