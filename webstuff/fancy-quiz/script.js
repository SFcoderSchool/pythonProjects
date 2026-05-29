// Quiz Game

let totalQuestions = 10;
let currentIndex = 0;
let score = 0;

// --- Questions stored as plain variables ---
let q1 = "What planet is closest to the Sun?";
let q2 = "How many sides does a hexagon have?";
let q3 = "What is the capital of Japan?";
let q4 = "What gas do plants absorb from the air?";
let q5 = "How many days are in a leap year?";
let q6 = "What is 12 multiplied by 12?";
let q7 = "What is the largest ocean on Earth?";
let q8 = "How many bones are in the human body?";
let q9 = "What colour do you get mixing red and blue?";
let q10 = "What is the fastest land animal?";

let a1 = "mercury";
let a2 = "6";
let a3 = "tokyo";
let a4 = "carbon dioxide";
let a5 = "366";
let a6 = "144";
let a7 = "pacific";
let a8 = "206";
let a9 = "purple";
let a10 = "cheetah";

// --- Get question or answer by number ---
function getQuestion(num) {
  if (num === 1) {
    return q1;
  }
  if (num === 2) {
    return q2;
  }
  if (num === 3) {
    return q3;
  }
  if (num === 4) {
    return q4;
  }
  if (num === 5) {
    return q5;
  }
  if (num === 6) {
    return q6;
  }
  if (num === 7) {
    return q7;
  }
  if (num === 8) {
    return q8;
  }
  if (num === 9) {
    return q9;
  }
  return q10;
}

function getAnswer(num) {
  if (num === 1) {
    return a1;
  }
  if (num === 2) {
    return a2;
  }
  if (num === 3) {
    return a3;
  }
  if (num === 4) {
    return a4;
  }
  if (num === 5) {
    return a5;
  }
  if (num === 6) {
    return a6;
  }
  if (num === 7) {
    return a7;
  }
  if (num === 8) {
    return a8;
  }
  if (num === 9) {
    return a9;
  }
  return a10;
}

function showScreen(screenId) {
  let startScreen = document.getElementById("startScreen");
  startScreen.classList.add("hidden");
  let questionScreen = document.getElementById("questionScreen");
  questionScreen.classList.add("hidden");
  let resultsScreen = document.getElementById("resultsScreen");
  resultsScreen.classList.add("hidden");

  let currentScreen = document.getElementById(screenId);
  currentScreen.classList.remove("hidden");
}

// --- Quiz flow ---
function startQuiz() {
  currentIndex = 0;
  score = 0;
  showScreen("questionScreen");
  loadQuestion();
}

function loadQuestion() {
  let num = currentIndex + 1;

  document.getElementById("questionNumber").textContent =
    "Question " + num + " of " + totalQuestions;

  document.getElementById("questionText").textContent = getQuestion(num);
  document.getElementById("answerInput").value = "";

  hideFeedback();
  document.getElementById("nextBtn").classList.add("hidden");
}

function submitAnswer() {
  let userAnswer = document
    .getElementById("answerInput")
    .value.trim()
    .toLowerCase();
  let correctAnswer = getAnswer(currentIndex + 1);

  if (userAnswer === "") {
    return;
  }

  if (userAnswer === correctAnswer) {
    score = score + 1;
    showFeedback("Correct!", "correct");
  } else {
    showFeedback("The answer was: " + correctAnswer, "wrong");
  }

  document.getElementById("nextBtn").classList.remove("hidden");
}

function nextQuestion() {
  currentIndex = currentIndex + 1;

  if (currentIndex < totalQuestions) {
    loadQuestion();
  } else {
    showResults();
  }
}

// --- Feedback helpers ---
function showFeedback(message, type) {
  let feedback = document.getElementById("answerFeedback");
  feedback.textContent = message;
  feedback.className = "feedback " + type;
  feedback.classList.remove("hidden");
}

function hideFeedback() {
  let feedback = document.getElementById("answerFeedback");
  feedback.textContent = "";
  feedback.className = "feedback hidden";
}

// --- Results ---
function getResultTitle(s) {
  if (s >= 9) {
    return "Amazing! ";
  }
  if (s >= 6) {
    return "Well done! ";
  }
  return "Nice try! ";
}

function getResultMessage(s) {
  if (s >= 9) {
    return "Near perfect — you really know your stuff!";
  }
  if (s >= 6) {
    return "Solid effort — keep it up!";
  }
  return "Keep practising — you'll get there!";
}

function showResults() {
  showScreen("resultsScreen");
  document.getElementById("resultTitle").textContent = getResultTitle(score);
  document.getElementById("resultScore").textContent =
    "You scored " + score + " out of " + totalQuestions;
  document.getElementById("resultMessage").textContent =
    getResultMessage(score);
}

function resetQuiz() {
  showScreen("startScreen");
}
