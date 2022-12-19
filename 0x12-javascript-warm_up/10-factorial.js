#!/usr/bin/node

let val = 1;

console.log(factorial(parseInt(process.argv[2]), val));

function factorial(a, result)
{

	if (isNaN(a) || a == 0 || a == 1)
	{
		return result;
	}
		return factorial((a - 1), result *= a);
}
