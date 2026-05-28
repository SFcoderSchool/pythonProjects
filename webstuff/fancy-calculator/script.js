let currentNumber = "";
let firstNumber = "";
let operation = "";

// --- Wire up digit buttons using addEventListener ---
// Start by doing 0 and 1 then point out quite tedious and pattern so use a for loop

// document.getElementById("btn0").addEventListener("click", function () {
//   pressDigit("0");
// });
// document.getElementById("btn1").addEventListener("click", function () {
//   pressDigit("1");
// });
// document.getElementById("btn2").addEventListener("click", function () {
//   pressDigit("2");
// });
// document.getElementById("btn3").addEventListener("click", function () {
//   pressDigit("3");
// });
// document.getElementById("btn4").addEventListener("click", function () {
//   pressDigit("4");
// });
// document.getElementById("btn5").addEventListener("click", function () {
//   pressDigit("5");
// });
// document.getElementById("btn6").addEventListener("click", function () {
//   pressDigit("6");
// });
// document.getElementById("btn7").addEventListener("click", function () {
//   pressDigit("7");
// });
// document.getElementById("btn8").addEventListener("click", function () {
//   pressDigit("8");
// });
// document.getElementById("btn9").addEventListener("click", function () {
//   pressDigit("9");
// });

for (let i = 0; i < 10; i = i + 1) {
  let button = document.getElementById("btn" + i);
  button.addEventListener("click", function () {
    pressDigit(i + "");
  });
}

document.getElementById("btnDot").addEventListener("click", function () {
  pressDigit(".");
});

// --- Wire up operation buttons ---
document.getElementById("btnAdd").addEventListener("click", function () {
  pressOperation("+");
});
document.getElementById("btnSub").addEventListener("click", function () {
  pressOperation("-");
});
document.getElementById("btnMul").addEventListener("click", function () {
  pressOperation("x");
});
document.getElementById("btnDiv").addEventListener("click", function () {
  pressOperation("÷");
});

// --- Wire up action buttons ---
document.getElementById("btnEquals").addEventListener("click", function () {
  calculate();
});
document.getElementById("btnClear").addEventListener("click", function () {
  clearAll();
});

// --- Functions ---

// function to actually update value
function updateDisplay(value) {
  document.getElementById("display").textContent = value;
}

// clear the display and numbers
function clearAll() {
  currentNumber = "";
  firstNumber = "";
  operation = "";
  document.getElementById("history").textContent = "";
  updateDisplay("0");
}

// update the digit in variable and update visual display
// bring up the "." later on
function pressDigit(digit) {
  if (digit === "." && currentNumber.includes(".")) {
    return;
  }
  currentNumber = currentNumber + digit;
  updateDisplay(currentNumber);
}

// update the display with the operation
function pressOperation(op) {
  if (currentNumber === "") {
    return;
  }
  firstNumber = currentNumber;
  operation = op;
  currentNumber = "";
  updateDisplay(op);
}

// do the actual math
// should have potentially done this in a previous project
function calculate() {
  if (firstNumber === "" || currentNumber === "" || operation === "") {
    return;
  }

  let a = parseFloat(firstNumber);
  let b = parseFloat(currentNumber);
  let result;

  if (operation === "+") {
    result = a + b;
  }
  if (operation === "-") {
    result = a - b;
  }
  if (operation === "x") {
    result = a * b;
  }
  if (operation === "÷") {
    if (b === 0) {
      updateDisplay("Error");
      clearAll();
      return;
    }
    result = a / b;
  }

  document.getElementById("history").textContent =
    firstNumber + " " + operation + " " + currentNumber + " =";

  // CODE FOR WARM UP ------------
  // previousNumber = currentNumber;
  // updatePrevious(previousNumber);
  // CODE FOR WARM UP ------------

  currentNumber = result;
  firstNumber = "";
  operation = "";
  updateDisplay(currentNumber);
}

//CODE FOR WARMUP ----------------------
let previousNumber = "";
function updatePrevious(value) {
  let prev = document.getElementById("previous");
  prev.innerText = "Previous Result -> " + value;
}
