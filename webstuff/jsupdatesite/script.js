let name = "";
let shown = false;

// Group of code that handles combining the first and last name inputs, shows the name on the page.
function create_name() {
  let first = document.getElementById("firstname").value;
  let last = document.getElementById("lastname").value;
  name = first + " " + last;
  document.getElementById("name").innerHTML = name;
  shown = true;
}

// Group of code that shows or hides the name
function toggle_name() {
  if (shown === false) {
    document.getElementById("name").innerHTML = name;
    shown = true;
  } else {
    document.getElementById("name").innerHTML = "";
    shown = false;
  }
}

// Group of code that changes the color of the name, can change other values
function change_name_color() {
  document.getElementById("name").style.color =
    "rgb(" +
    parseInt(Math.random() * 255) +
    "," +
    parseInt(Math.random() * 255) +
    "," +
    parseInt(Math.random() * 255) +
    ")";
}

// Group of code that changes the background color
function change_bg_color() {
  // Notice that this doesn't use getElementById but body since we're directly changing the background of the body
  document.body.style.background =
    "rgb(" +
    parseInt(Math.random() * 255) +
    "," +
    parseInt(Math.random() * 255) +
    "," +
    parseInt(Math.random() * 255) +
    ")";
}
