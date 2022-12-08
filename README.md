Exercise for Lecture 5 – modules

a)
Create a package called Bioinformatics (or similar) containing a module called
Pattern (or similar). It should contain a function that accepts the following
arguments:
1) a DNA sequence (from the file in part c)
2) a pattern to match against
3) an optional Boolean flag (yes/no) stating whether the sequence is circular or
not
and returns a sorted list of the positions of the matches.

You can use the module regex to find overlapping matches. If the sequence is
circular, this will require a small adaptation of your code.
A call to the function in your module could for example look like:
pos = Bioinf.getPatternMatchPositions(sequence,pattern,is_circular)

b)Create a second Module called Restriction (or similar). This should contain a
subroutine that accepts the following arguments:
1) a list that contains the positions where a restriction enzyme cuts a given
sequence
2) the length of the sequence
Both are created in the first module
3) an optional Boolean value that decides whether the fragment lengths should
be computed for a linear or circular sequence
The function should return a list of the expected lengths of the fragments that would
result from cutting with that enzyme.

c)Write a program that uses these two modules to read a DNA sequence from a
file, search for restriction enzyme cutting sites, calculate the fragment sizes, and
report the result in a nicely formatted way to a new file. This part should also collect
the filename, the pattern and the circular flag via commandline argument, input or
config file (not in the code!)
