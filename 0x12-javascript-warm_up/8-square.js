#!/usr/bin/node

if (process.argv.length == 2 || isNaN(parseInt(process.argv[2])))
{
	console.log("Missing size");
}
else
{
    let output = '';
    for (let i = 0; i < process.argv[2]; i++)
    {
	    for (let j = 0; j < process.argv[2]; j++)
	    {
		    output += "X";
	    }
	    if (i != (process.argv[2] - 1))
	    {
	        output += "\n";
	    }
    }
    console.log(output);
}
