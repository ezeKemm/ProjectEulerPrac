"""
-----------
PROBLEM
https://projecteuler.net/problem=24
-----------
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
        012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

-----------
SOLUTION
https://tinyurl.com/v7ee4vh
-----------
The best approach, given the permutation nature of the problem, is a recursive algorithm
to compute all possible combinations of our given alphanumerics while maintaining order.
This function assumes a ordered list as an input but this can easily be modified to sort first.
We recursively shorten the list, splicing out the value currently being accessed by the list,
until our base case. From our base case we build a subunit permutation composed of only several of our original values.
We build up this process until we have constructed the entire permutation.

For more efficiency, since we are asked only to find the millionth lexicographic permutation, we can add a condition
to prevent unnecessarily constructing the entire permutation.
"""


"""
DOCSTRING
Input: vals -- ordered list of alphanumerics to be permuted
Output: Lexicographic permutation of input list

Recursively determines all combinations of given numbers/letters in numerical/alphabetic order.
This provides a general lexicographic permutation calculator.
"""
def lexi_perm_calc(vals):
    lexicon = []
    "Base Case"
    if len(vals) == 1:
        return [vals[0]]

    for i in range(len(vals)):
        nvals = vals[:i] + vals[i+1::]
        rval = lexi_perm_calc(nvals)

        for j in range(len(rval)):
            lexicon.append(str(vals[i]) + str(rval[j]))

    return lexicon


"Assume list given in numerical/aphabetical order"
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = lexi_perm_calc(lst)

print(f"Millionth Lexicographic Permutation for {lst}: {result[1000000-1]}")
