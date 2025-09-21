// Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

// Return your answer as a number.


function sumMix(x) {
    const nums = x.map(Number);
    let sum = 0;
    nums.forEach(element => {
        sum += element
    });
    return sum
};


console.log(sumMix([1, '2', 2, '4']))