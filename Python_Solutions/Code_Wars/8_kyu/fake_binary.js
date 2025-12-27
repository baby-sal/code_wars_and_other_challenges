// Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
// Return the resulting string.
// Note: input will never be an empty string


function fakeBin(x) {
    const replaced = x.replace(/[123456789]/g, (char) => {
        const replacement = { 1: "0", 2: "0", 3: "0", 4: "0", 5: "1", 6: "1", 7: "1", 8: "1", 9: "1" };
        return replacement[char] || char;
    });
    return replaced;
};

console.log(fakeBin('45385593107843568'));