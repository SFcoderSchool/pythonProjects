// number guessing
// attempt to guess the given number

// steps
// - NOTE: worry about the hidden attribute last
// - create the setup button and function
// - generate a random number and output it
// - store the number for later (NOTE: outside the function)

// - create the guess button and input / label
// - make the guess function
// - take their input and check to see if it matches the random number
// - NOTE: make sure the data matches
// - output a hint until they get it correct

// - add proper ids and alter hidden attribute accordingly

let number = 0;
let started = false;
document.getElementById("game").hidden = true;

function setup() {
  number = parseInt(Math.random() * 100) + 1;
  started = true;
  document.getElementById("game").hidden = false;
  document.getElementById("setup").hidden = true;
}

function guess() {
  let hint = "";
  let user = document.getElementById("guess").value;
  user = parseInt(user);
  if (user > number) {
    hint = "too high";
  } else if (user < number) {
    hint = "too low";
  } else {
    hint = "You got it!";
    document.getElementById("setup").hidden = false;
  }

  document.getElementById("hint").innerHTML = hint;
}
