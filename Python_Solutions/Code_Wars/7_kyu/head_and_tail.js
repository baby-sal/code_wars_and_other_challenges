// You need to swap the head and the tail of the specified array:

// the head (the first half) of array moves to the end, the tail (the second half) 
// moves to the start. The middle element (if it exists) leaves on the same position.

// Return new array.

// For example:

//    [ 1, 2, 3, 4, 5 ]   =>  [ 4, 5, 3, 1, 2 ]
//     \----/   \----/         
//      head     tail 

//    [ -1, 2 ]  => [ 2, -1 ] 
//    [ 1, 2, -3, 4, 5, 6, -7, 8 ]   =>  [ 5, 6, -7, 8, 1, 2, -3, 4 ]  

function swapHeadAndTail(arr) {
    if (arr.length % 2 == 0) {
        const middle = Math.floor(arr.length / 2)
        return arr.slice(middle, arr.length).concat(arr.slice(0, middle))
    }
    else {
        const middle = Math.floor(arr.length / 2)
        return arr.slice(middle + 1, arr.length).concat(arr[middle], arr.slice(0, middle))
    }
};

console.log(swapHeadAndTail([1, 2, -3, 4, 5, 6, -7, 8]))
console.log(swapHeadAndTail([-1, 2]))
console.log(swapHeadAndTail([-1, 2, 3]))
console.log(swapHeadAndTail([-1, 2, 3, 4, 5]))



// input = [45, 69, -71, -30, 49, 62, -11, 15, 17, 86, -37, -26, -75]
// : expected[-71, -30, 49, 62, -11, 15, 17, 86, -37, -26, -75, -11, 45, 69, -71, -30, 49, 62] 
// to deeply equal[15, 17, 86, -37, -26, -75, -11, 45, 69, -71, -30, 49, 62]