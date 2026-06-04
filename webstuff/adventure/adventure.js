const prompt = require("prompt-sync")();

// ==============================
//  PLAYER SETUP
// ==============================

let playerName = prompt("Welcome! What is your explorer's name?");
let health = 100;
let fuel = 50;
let crystals = 0;
let shieldsUp = false;

function printStatus() {
  console.log("------------------------------");
  console.log("Explorer : " + playerName);
  console.log("Health   : " + health + " / 100");
  console.log("Fuel     : " + fuel);
  console.log("Crystals : " + crystals);
  console.log("Shields  : " + (shieldsUp ? "ON" : "OFF"));
  console.log("------------------------------");
}

function randomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function randomChance(percent) {
  return randomNumber(1, 100) <= percent;
}

// ==============================
//  ACTIONS
// ==============================

function scanPlanet() {
  console.log("\nScanning the planet... (-5 fuel)");
  fuel = fuel - 5;

  if (fuel < 0) {
    console.log("  Not enough fuel!");
    fuel = 0;
    return;
  }

  let found = randomNumber(0, 3);

  if (found === 0) {
    console.log("  Nothing found. Fuel wasted.");
  } else if (found === 1) {
    let gain = randomNumber(1, 4);
    crystals = crystals + gain;
    console.log("  Found " + gain + " crystals! Total: " + crystals);
  } else if (found === 2) {
    let fuelGain = randomNumber(5, 15);
    fuel = fuel + fuelGain;
    console.log("  Found a fuel pod! +" + fuelGain + " fuel. Total: " + fuel);
  } else {
    console.log("  Strange signal... an alien is coming!");
    encounterAlien();
  }
}

function activateShields() {
  if (fuel < 10) {
    console.log("\n Not enough fuel for shields! (need 10)");
    return;
  }
  shieldsUp = true;
  fuel = fuel - 10;
  console.log("\n Shields activated! (-10 fuel)");
}

function encounterAlien() {
  console.log("\n An alien ship attacks!");
  if (shieldsUp) {
    console.log("  Shields absorb the hit! No damage.");
    shieldsUp = false;
    console.log("  Shields powered down.");
  } else {
    let damage = randomNumber(10, 30);
    health = health - damage;
    console.log("  Direct hit! -" + damage + " health. Now: " + health);
  }
}

function mineAsteroid() {
  console.log("\nMining an asteroid... (-8 fuel)");
  fuel = fuel - 8;

  if (fuel < 0) {
    console.log("  Not enough fuel to mine!");
    fuel = 0;
    return;
  }

  if (randomChance(60)) {
    let gain = randomNumber(2, 6);
    crystals = crystals + gain;
    console.log("  Success! +" + gain + " crystals. Total: " + crystals);
  } else {
    let damage = randomNumber(5, 20);
    health = health - damage;
    console.log(
      "  Debris hit the ship! -" + damage + " health. Now: " + health,
    );
  }
}

function refuel() {
  if (crystals < 3) {
    console.log("\nNeed 3 crystals to trade for fuel. You have: " + crystals);
    return;
  }
  crystals = crystals - 3;
  fuel = fuel + 25;
  console.log("\nTraded 3 crystals for 25 fuel. Fuel now: " + fuel);
}

// ==============================
//  PLAYER CHOICE
// ==============================

function askChoice() {
  console.log("\nWhat do you do?");
  console.log("  1 - Scan planet  (-5 fuel, random reward)");
  console.log("  2 - Mine asteroid  (-8 fuel, 60% crystal chance)");
  console.log("  3 - Activate shields  (-10 fuel, blocks next attack)");
  console.log("  4 - Trade crystals for fuel  (-3 crystals, +25 fuel)");

  let choice = prompt(
    "Choose an action:\n" +
      "1 = Scan planet\n" +
      "2 = Mine asteroid\n" +
      "3 = Activate shields\n" +
      "4 = Trade crystals for fuel",
  );

  if (choice === "1") {
    scanPlanet();
  } else if (choice === "2") {
    mineAsteroid();
  } else if (choice === "3") {
    activateShields();
  } else if (choice === "4") {
    refuel();
  } else {
    console.log("  Unknown choice — turn skipped!");
  }
}

// ==============================
//  OUTCOME CHECK
// ==============================

function isGameOver() {
  if (health <= 0) {
    console.log("\n Ship destroyed. Mission failed.");
    return true;
  }
  if (fuel <= 0) {
    console.log("\nOut of fuel. Drifting in space...");
    return true;
  }
  return false;
}

function getFinalRank() {
  if (crystals >= 15) {
    return " LEGENDARY EXPLORER";
  }
  if (crystals >= 10) {
    return " Master Explorer";
  }
  if (crystals >= 5) {
    return " Skilled Explorer";
  }
  return " Rookie Explorer";
}

// ==============================
//  THE ADVENTURE — 5 rounds
// ==============================

console.log("\nSPACE EXPLORER — The Adventure Begins!");
console.log("Mission: collect as many crystals as you can in 5 rounds!");
printStatus();

for (let round = 1; round <= 5; round++) {
  console.log("\n========== ROUND " + round + " of 5 ==========");
  printStatus();

  if (isGameOver()) {
    break;
  }

  // Random alien encounter on rounds 2 and 4
  if (round === 2 || round === 4) {
    console.log("Danger! An alien ship is nearby this round!");
    encounterAlien();
    if (isGameOver()) {
      break;
    }
  }

  askChoice();
}

// ==============================
//  FINAL RESULT
// ==============================

console.log("\n==============================");
console.log("  MISSION OVER");
console.log("==============================");
printStatus();

if (!isGameOver()) {
  console.log("Final rank: " + getFinalRank());
  console.log("Great flying, " + playerName + "!");
}
