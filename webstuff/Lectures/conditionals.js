// 1 use if statements to check data
let number = 5;

// if equal
if (number == 5) {
  console.log("yes");
}

// if not equal
if (number != 5) {
  console.log("no");
}

// 2 use if statements efficiently when looking for 1 answer from multiple options

let name = "jeff";
if (name == 5) {
  console.log("yes");
} else {
  console.log("no");
}

// 3 what if i have more than 2 options

// check to see if i have a banana. console.log statements will allow you to see which if statement worked

let basket = "banana";
if (basket == "apple") {
  console.log(1);
} else if (basket == "pineapple") {
  console.log(2);
} else if (basket == "grape") {
  console.log(3);
} else if (basket == "banana") {
  console.log(4);
} else if (basket == "durian") {
  console.log(5);
}

// why did we not use else? because if basket is not banana, the else statment will still run as if we found the banana.
// else covers all other options

basket = "banana";
if (basket == "apple") {
  console.log(1);
} else if (basket == "pineapple") {
  console.log(2);
} else if (basket == "grape") {
  console.log(3);
} else if (basket == "blueberry") {
  console.log(4);
} else {
  console.log(5);
}

// Common operators
// greater than >
// less than<
// equal to ==
// not equal to !=

// exercise 1: console.log the larger of the two numbers using conditionals to check
let num1 = 50;
let num2 = 30;

// exercise 2: check to see if any of these variables are holding the color "pink"
let c1 = "red";
let c2 = "purple";
let c3 = "pink";
let c4 = "silver";

// exercise 3: create a variable and enter a number. using the chart below, output the result.

//  90-100: A
//  80-89: B
//  70-79: C
//  60-69: D
//  0-59: F
