var arm = require("./armstrongNumbers");
var shallowEqual = require('shallow-equal');

function createArrayOfNum(maxValue) {
  return Array.apply(null, {length: maxValue}).map(Number.call, Number)
}

console.log(shallowEqual.shallowEqualArrays(arm.findArmstrongNumbers([0]),[0]));
console.log(shallowEqual.shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(8)), [0, 1, 2, 3, 4, 5, 6, 7]));
console.log(shallowEqual.shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(99)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]));
console.log(shallowEqual.shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(999)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]));
