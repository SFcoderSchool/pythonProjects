// Recipe Builder
// start with just the ingredients function
// make a recipe and depending on time add more

const prompt = require("prompt-sync")();

function ingredient(name, amountPerServing, unit, servings) {
  let total = amountPerServing * servings;
  return "  - " + total + " " + unit + " of " + name;
}

// --- Recipes ---

function printPasta(servings) {
  console.log("\n=== Tomato Pasta for " + servings + " ===");
  console.log("Ingredients:");
  console.log(ingredient("pasta", 75, "g", servings));
  console.log(ingredient("tomato sauce", 50, "g", servings));
  console.log(ingredient("olive oil", 0.5, "tbsp", servings));
  console.log(ingredient("garlic", 0.5, "cloves", servings));
  console.log(ingredient("parmesan", 10, "g", servings));
}

function printPancakes(servings) {
  console.log("\n=== Pancakes for " + servings + " ===");
  console.log("Ingredients:");
  console.log(ingredient("flour", 50, "g", servings));
  console.log(ingredient("milk", 75, "ml", servings));
  console.log(ingredient("egg", 0.5, "", servings));
  console.log(ingredient("butter", 5, "g", servings));
  console.log(ingredient("sugar", 5, "g", servings));
}

function printFriedRice(servings) {
  console.log("\n=== Fried Rice for " + servings + " ===");
  console.log("Ingredients:");
  console.log(ingredient("rice", 80, "g", servings));
  console.log(ingredient("soy sauce", 1, "tbsp", servings));
  console.log(ingredient("egg", 1, "", servings));
  console.log(ingredient("spring onion", 0.5, "", servings));
  console.log(ingredient("sesame oil", 0.5, "tbsp", servings));
}

function printSoup(servings) {
  console.log("\n=== Vegetable Soup for " + servings + " ===");
  console.log("Ingredients:");
  console.log(ingredient("vegetable stock", 200, "ml", servings));
  console.log(ingredient("carrot", 0.5, "", servings));
  console.log(ingredient("potato", 0.5, "", servings));
  console.log(ingredient("onion", 0.25, "", servings));
  console.log(ingredient("mixed herbs", 0.5, "tsp", servings));
}

// --- User prompt ---

console.log("Welcome to the Recipe Builder!");
console.log("Available recipes:");
console.log("  1 - Tomato Pasta");
console.log("  2 - Pancakes");
console.log("  3 - Fried Rice");
console.log("  4 - Vegetable Soup");

let choice = prompt("Which recipe would you like? Enter 1, 2, 3 or 4:");
let servings = prompt("How many servings?");
servings = parseInt(servings);

if (choice === "1") {
  printPasta(servings);
}
if (choice === "2") {
  printPancakes(servings);
}
if (choice === "3") {
  printFriedRice(servings);
}
if (choice === "4") {
  printSoup(servings);
}
if (choice !== "1" && choice !== "2" && choice !== "3" && choice !== "4") {
  console.log("That wasn't a valid choice!");
}
