// functions
// function addNumbers(num1, num2){
//     console.log(num1 + num2);
// }

// function addNumbers(num1, num2){
//     return num1 + num2;
// }
// let total = addNumbers(1, 3);
// console.log(total);

//for loop:

// let lst = ['Butter', 'Eggs', 'Sugar'];

// for (i = 0; i < lst.length; i++) {
//     let lst_item = `${i+1}. ${lst[i]}`;
//     console.log(lst_item);
// }

// while loop:

let budget = 0;
let goal = 400;
let weeklySavings = 100;

while (budget < goal) {
    budget = budget + weeklySavings
    message = `Current budget: $${budget}`
    console.log(message)
}