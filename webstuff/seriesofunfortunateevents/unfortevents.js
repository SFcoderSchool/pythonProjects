// series of unfortunate events

function event1() {
  let chance = parseInt(Math.random() * 4 + 1);
  if (chance === 1) {
    console.log("You get hit by a baseball -30 hp");
    hp = hp - 30;
  } else if (chance === 2) {
    console.log("You get a paper cut -10 hp");
    hp = hp - 10;
  } else if (chance === 3) {
    console.log("You step on dog poo -5 hp");
    hp = hp - 5;
  } else {
    console.log("You found a pork bun +10 hp");
    hp = hp + 10;
  }
}

function event2() {
  chance = parseInt(Math.random() * 4 + 1);
  if (chance === 1) {
    console.log("You get bit by a mosquito -20 hp");
    hp = hp - 20;
  } else if (chance === 2) {
    console.log("You caught the flu -40 hp");
    hp = hp - 40;
  } else if (chance === 3) {
    console.log("You get hit by a toyota -80 hp");
    hp = hp - 80;
  } else {
    console.log("You find $10 on the ground +10 hp");
    hp = hp + 10;
  }
}

function event3() {
  chance = parseInt(Math.random() * 4 + 1);
  if (chance === 1) {
    console.log("You get bit by a mosquito -20 hp");
    hp = hp - 20;
  } else if (chance === 2) {
    console.log("You caught the flu -40 hp");
    hp = hp - 40;
  } else if (chance === 3) {
    console.log("You get hit by a toyota -80 hp");
    hp = hp - 80;
  } else {
    console.log("You find $10 on the ground +10 hp");
    hp = hp + 10;
  }
}

let hp = 100;

event1();

console.log("Health:", hp);

if (hp > 0) {
  event2();
} else {
  console.log("Game over");
}

console.log("Health:", hp);

if (hp > 0) {
  event3();
} else {
  console.log("Game over");
}

console.log("Health:", hp);
