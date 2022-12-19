#!/usr/bin/node

const val = 1;

console.log(factorial(parseInt(process.argv[2]), val));

function factorial (a, result) {
  if (isNaN(a) || a === 0 || a === 1) {
    return result;
  }
  const NewResult = result * a;
  return factorial((a - 1), NewResult);
}
