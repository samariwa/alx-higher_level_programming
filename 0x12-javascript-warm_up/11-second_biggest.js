#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3 || isNaN(parseInt(process.argv[2]))) {
  console.log(0);
} else {
  const array = [];
  for (let i = 2; i < process.argv.length; i++) {
    array.push(parseInt(process.argv[i]));
  }

  const SortedArray = [];
  while (array.length !== 0) {
    SortedArray.push(Math.max.apply(Math, array));
    array.splice(array.indexOf(Math.max.apply(Math, array)), 1);
  }
  console.log(SortedArray[1]);
}
