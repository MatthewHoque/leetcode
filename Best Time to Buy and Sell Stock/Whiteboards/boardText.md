## Initial Thoughts
Going to go into Excel to start some brainstorming on this one

Given the example we notice that each "buying" price as we go along has a decreasing number of options and obviosly we want to consider the "buying" price so instantly thinking about a two sided pointer approach


After messing around on excel I am fairly confident I have the right idea for an O(n) implementation. 

Much better graphic explanation on the excel "Sheet 1"
However the overview is that we have 2 pointers on the left and to pointers on the right and we would want to move towards the center.

One pointer on each side will hold on to the max values while two other pointers on each side will explore the possibilities between all these pointers.

From there 3 calculations are made, the left potential between the left 2 pointers, the right potential between the right two pointers, and the end potential referred to as "far" in the excel sheet where the smallest of the left 2 pointers is put up with the largest of the two right


Have to leave now but will implement this when I get back to this


Returned and realized a small edge case that needs to be covered regarding my selectors (green squares) being shifted around

took another break then went on a bug hunting spree, honestly did not like that i submitted 3 times before the answer was accepted but thats ok
There are some optimizations that could potentially be done with how some stuff isn't moved around on some of the cycles thus creating redundant computations, this could be fixed pretty easy with some testing though I will not be spending the time for it

Most importantly, an O(n) solution was implemented
I seemed to have overcomplicated the problem however by doing a 2 end approach where I could have done it one ended.