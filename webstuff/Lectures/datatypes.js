console.log("Hello World"); // strings

console.log(1); // numbers

console.log(1 + 1); // valid arithmetic with numbers

console.log(1 + "1"); // strange arithmetic that occurs in JS

let x = 3; // variables
console.log(x * 2); // calculations with variables

console.log(x + x); // adding itself

console.log(x, x); // output multiple variables

let y = 4;

console.log(x * y); // working with multiple variables

console.log(x * "8"); // strange calculation that occurs in JS

console.log("8" + x); // still strange calculation; string first, concat. Number first, add.

console.log(true); // boolean type; explicit boolean

console.log(3 == "3"); // strange operation with == in JS; equality without caring for types. Implicit boolean
console.log(3 === "3"); // how we should compare values in JS. Important to reiterate as == is dangerous and probably can address early enough to avoid students from using == habitually in JS. Instead using ===.

console.log(3 === 3); // true statement

const name = "John"; // const means declaring a constant variable with a single value. This will never change.

let user = "John"; // let declares a variable, variables declared with let can be reassigned
user = "Jane"; // This is okay.

// name = "Jane" // This is not.

const prompt = require("prompt-sync")(); // import prompt
let age = prompt("Enter your age: "); // ask the user for their age
age = parseInt(age); // turn the age into a number
console.log("You will be", age + 10, "years old in 10 years"); // output their age in 10 years

// exercise1: identify these values
10;
("423");
potato;
("sink");

// exercise2: output the sum of 10 and 2

// exercise3: combine your first and last name as separate strings

// exercise4: create a variable and store your name. Output "goodbye [name]"
