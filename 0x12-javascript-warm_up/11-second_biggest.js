#!/usr/bin/node

if (process.argv.length == 2 || process.argv.length == 3 || isNaN(parseInt(process.argv[2])))
{
    console.log(0);
}
else
{
    let array = [];
    for (let i = 2; i < process.argv.length; i++)
    {
        array.push(parseInt(process.argv[i]));
    }

    let sorted_array = [];
    while (array.length != 0)
    {
        sorted_array.push(Math.max.apply(Math, array));
	array.splice(array.indexOf(Math.max.apply(Math, array)), 1)
    }
    console.log(sorted_array[1]);
    
}
