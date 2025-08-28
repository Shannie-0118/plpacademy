// ===== Part 1: Variable Declarations and Conditionals =====
let userName = "Shanique";
let age = 20;

if (age >= 18) {
    console.log(userName + " is an adult 😎");
} else {
    console.log(userName + " is still a teen 😉");
}

// ===== Part 2: Custom Functions =====
function greetUser(name) {
    return `Hey ${name}! 👋 Welcome to the fun zone!`;
}

function calculateSquare(number) {
    return number * number;
}

// ===== Part 3: Loops =====
// For loop
for (let i = 1; i <= 5; i++) {
    console.log(`For loop: ${i} squared is ${calculateSquare(i)}`);
}

// While loop
let j = 1;
while (j <= 3) {
    console.log(`While loop fun: ${j} squared is ${calculateSquare(j)}`);
    j++;
}

// ===== Part 4: DOM Interactions =====
const outputDiv = document.getElementById("userInfo");
const greetBtn = document.getElementById("greetBtn");
const colorBtn = document.getElementById("colorBtn
