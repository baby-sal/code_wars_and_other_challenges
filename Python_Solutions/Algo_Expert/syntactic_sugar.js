const arr = [1, 2, 3, 4];

const doubled = arr.map(num => num * 2);

// console.log(doubled);

const [first, second, ...rest] = arr;

// console.log(first, second);
// console.log(rest);

function add(x, y) {
    console.log(x + y);
};

// add(...arr)

arr2 = [4, 5, 6];

const combined = [0, ...arr, 7, ...arr2];

// console.log(combined);

function logParams(x, ...extra) {
    console.log(x);
    console.log(extra);
};

// logParams(1, 2, 3, 4)

// const name = 'Sally';
const name = null;
const defaultName = name ?? 'Default Name'
// console.log(`Hello ${name}`);
console.log('Hello ' + defaultName);

