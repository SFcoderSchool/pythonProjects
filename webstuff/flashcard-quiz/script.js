// start with flipping the card to show answer
// make sure the css is done and manually checked before the js
// then work on unflipping
// if time introduce addeventlistener for the last card instead of onclick

let flippedCount = 0;

// let button4 = document.getElementById("button4");
// button4.addEventListener("click", function () {
//   flipCard(4);
// });

function flipCard(cardId) {
  let card = document.getElementById("card" + cardId);

  if (card.classList.contains("flipped")) {
    hideAnswer(cardId);
    markUnflipped(card);
    decreaseCount();
  } else {
    showAnswer(cardId);
    markFlipped(card);
    increaseCount();
  }
}

function showAnswer(card) {
  let question = document.getElementById("question" + card);
  let answer = document.getElementById("answer" + card);

  question.classList.add("hidden");
  answer.classList.remove("hidden");
}

function markFlipped(card) {
  card.classList.add("flipped");
}

function increaseCount() {
  flippedCount = flippedCount + 1;
  document.getElementById("scoreDisplay").textContent = flippedCount;
}

function hideAnswer(card) {
  let question = document.getElementById("question" + card);
  let answer = document.getElementById("answer" + card);

  question.classList.remove("hidden");
  answer.classList.add("hidden");
}

function markUnflipped(card) {
  card.classList.remove("flipped");
}

function decreaseCount() {
  flippedCount = flippedCount - 1;
  document.getElementById("scoreDisplay").textContent = flippedCount;
}
