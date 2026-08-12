let totalQuestions = 10;
let currentIndex = 0;
let score = 0;

let currentQuestion = "";
let currentAnswer = "";

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

function loadCurrentQuestion(num) {
  if (num === 1) {
    currentQuestion = q1;
    currentAnswer = a1;
  }
  if (num === 2) {
    currentQuestion = q2;
    currentAnswer = a2;
  }
  if (num === 3) {
    currentQuestion = q3;
    currentAnswer = a3;
  }
  if (num === 4) {
    currentQuestion = q4;
    currentAnswer = a4;
  }
  if (num === 5) {
    currentQuestion = q5;
    currentAnswer = a5;
  }
  if (num === 6) {
    currentQuestion = q6;
    currentAnswer = a6;
  }
  if (num === 7) {
    currentQuestion = q7;
    currentAnswer = a7;
  }
  if (num === 8) {
    currentQuestion = q8;
    currentAnswer = a8;
  }
  if (num === 9) {
    currentQuestion = q9;
    currentAnswer = a9;
  }
  if (num === 10) {
    currentQuestion = q10;
    currentAnswer = a10;
  }
}

function showScreen(id) {
  document.getElementById("startScreen").classList.add("hidden");
  document.getElementById("questionScreen").classList.add("hidden");
  document.getElementById("resultsScreen").classList.add("hidden");
  document.getElementById(id).classList.remove("hidden");
}

function startQuiz() {
  currentIndex = 0;
  score = 0;
  showScreen("questionScreen");
  loadQuestion();
}

function loadQuestion() {
  let num = currentIndex + 1;
  loadCurrentQuestion(num);

  document.getElementById("questionNumber").textContent =
    "Question " + num + " of " + totalQuestions;
  document.getElementById("questionText").textContent = currentQuestion;

  document.getElementById("answerInput").value = "";

  hideFeedback();
  document.getElementById("nextBtn").classList.add("hidden");
}

function submitAnswer() {
  let userAnswer = document.getElementById("answerInput").value.toLowerCase();

  if (userAnswer === "") {
    // do nothing, wait for them to type something
  } else {
    if (userAnswer === currentAnswer) {
      score = score + 1;
      showFeedback("Correct!", "correct");
    } else {
      showFeedback("The answer was: " + currentAnswer, "wrong");
    }
    document.getElementById("nextBtn").classList.remove("hidden");
  }
}

function nextQuestion() {
  currentIndex = currentIndex + 1;
  if (currentIndex < totalQuestions) {
    loadQuestion();
  } else {
    showResults();
  }
}

function showFeedback(message, type) {
  let feedback = document.getElementById("answerFeedback");
  feedback.textContent = message;
  feedback.classList.remove("hidden", "correct", "wrong");
  feedback.classList.add(type);
}

function hideFeedback() {
  let feedback = document.getElementById("answerFeedback");
  feedback.textContent = "";
  feedback.classList.add("hidden");
  feedback.classList.remove("correct", "wrong");
}

function resetQuiz() {
  showScreen("startScreen");
}

// BONUS

let resultTitle = "";
let resultMessage = "";

function calculateResultText(s) {
  if (s >= 9) {
    resultTitle = "Amazing!";
    resultMessage = "Near perfect — you really know your stuff!";
  } else if (s >= 6) {
    resultTitle = "Well done!";
    resultMessage = "Solid effort — keep it up!";
  } else {
    resultTitle = "Nice try!";
    resultMessage = "Keep practising — you'll get there!";
  }
}

function showResults() {
  showScreen("resultsScreen");
  calculateResultText(score);

  document.getElementById("resultTitle").textContent = resultTitle;
  document.getElementById("resultScore").textContent =
    "You scored " + score + " out of " + totalQuestions;
  document.getElementById("resultMessage").textContent = resultMessage;
}
