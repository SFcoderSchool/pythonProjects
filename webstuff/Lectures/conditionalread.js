// Read each problem and determine the output of each

// PART 1 -----------------------------------------------------------------------------------
// Read 1
let a = 6;
if (a === 6) {
  console.info("a");
  if (a === 4) {
    console.info("b");
  }
}

// Read 2
let b = 6;
if (b === 5) {
  console.info("a");
  if (b === 6) {
    console.info("b");
  }
}

// Read 3
let c = 6;
if (c === 6) {
  console.info("a");
  c = 7;
  if (c === 7) {
    console.info("b");
  }
}
// END PART 1 -----------------------------------------------------------------------------------

// PART 2 -----------------------------------------------------------------------------------
// Read 4
let d = 6;
if (d + 2 === 8) {
  console.info("a");
  if (d + 3 === 9) {
    console.info("b");
  }
  if (d + 10 === 15) {
    console.info("c");
  }
}

// Read 5
let e = "hello";
if (e === "Hello") {
  console.info("a");
}
if (e === "hellO") {
  console.info("b");
  if (e === "hello") {
    console.info("c");
  }
}
if (e === "hello") {
  console.info("d");
}
// END PART 2 -----------------------------------------------------------------------------------
