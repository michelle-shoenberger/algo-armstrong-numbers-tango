
/*How can you make this more scalable and reusable later?
Release 2: find all Armstrong nums between 0 and 999
1. numbers will be this array so it's variable
2. Test all numbers - iterate over the list (could be range or individual numbers to check)
3. Initialize result array 
4. How to get the sum of powers for a number:
*/
exports.findArmstrongNumbers = function(numbers) {
  let result = [];
  let sum, one, second, third;
  if (!Array.isArray(numbers)) {
    return result
  }
  for (let i=0; i<numbers.length; i++) {
    // Determine sum of powers
    let strdigits = i.toString().split("")
    let total = 0
    for (let j=0; j<strdigits.length; j++) {
      total += parseInt(strdigits[j])**strdigits.length;
    }
    // Check if equivalent to number
    if (numbers[i] == total) {
      result.push(numbers[i]);
    }
  }
  return result
};
