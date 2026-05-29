// Short function lecture

// A function is giving a set of reusable instructions a name. You can use functions anytime and anywhere.

function print10Hello() {
  for (let i = 0; i < 10; i = i + 1) {
    console.log("Hello");
  }
}

// activating the box of code 3x instead of copy pasting the for loop lowers the mess
print10Hello();
print10Hello();
print10Hello();

// you can also write the function and use it later for organization purposes
function count10() {
  for (let i = 0; i < 10; i = i + 1) {
    console.log(i);
  }
}

print10Hello();
count10();
print10Hello();
count10();
print10Hello();

// returning data; function call will become the data that gets returned
function sum(x, y) {
  return x + y;
}

// return also stops the function in its tracks
function printHiMax5Times(n) {
  for (let i = 0; i < n; i = i + 1) {
    if (i == 5) {
      return;
    }
    console.log("Hi");
  }
}
