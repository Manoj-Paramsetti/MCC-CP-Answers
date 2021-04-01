# MCC-CP-Answers
In this repo, I shared answers for Microsoft Campus Club's Competitive programming questions

**Secured position: #1**

## Paradoxical Entity

You are provided with a playlist containing N songs, each has a unique positive integer length. Assume you like all the songs from this playlist, but there is a song, which you like more than others.

It is named "Computing Paradox".

You decided to sort this playlist in increasing order of songs length. For example, if the lengths of the songs in the playlist were {1, 3, 5, 2, 4} after sorting it becomes {1, 2, 3, 4, 5}.

Before the sorting, "Computing Paradox" was on the kth position (1-indexing is assumed for the playlist) in the playlist.

Your task is to find the position of "Computing Paradox" in the sorted playlist.

**Input Format**

The first line contains two numbers N denoting the number of songs in the playlist. The second line contains N space separated integers A1, A2, A3,..., AN denoting the lengths of songs. The third line contains an integer k, denoting the position of "Computing Paradox" in the initial playlist.

**Constraints**

No Constraints

**Output Format**

Output a single line containing the position of "Computing Paradox" in the sorted playlist.

**Sample Input 0**
```
4
1 3 4 2
2
```
**Sample Output 0**
```
3
```
**Explanation 0**

N equals to 4, k equals to 2, A equals to {1, 3, 4, 2}. The answer is 3 because {1, 3, 4, 2} -> {1, 2, 3, 4}.

## Document-Index 
In Document Process we make use of something called an index, or an inverted index. In layman terms, it is just a set of pairs (WORD, OCCURRENCES). WORD signifies the frequency of word occurring in the document. OCCURRENCES on the other hand is a sequence of integers giving the positions at which the word occurs, in an increasing word.

Let us take a famous example from John F. Kennedy's statement:

"ask not what your country can do for you ask what you can do for your country"

The Index would look something like: ask 0 9 can 5 12 country 4 16 do 6 13 for 7 14 not 1 what 2 10 you 8 11 your 3 15

If you closely notice, the zeroth word in the document as well as the ninth word is "ask", and hence the entry for "ask" in the index is "ask 0 9".

You are tasked to make this happen through Code where we can read through the particular statement and print the index, in lexicographic order. Remember that the single character word * is the last word.

**Input Format**

String: A sequence of whitespace separated words

**Constraints**

None

**Output Format**

Order of Words in lexicographic order.

**Sample Input 0**
```
If you want to lose weight, you need to stop eating junk, and you need to start exercising. Today. Not tomorrow. A journey of a thousand miles begins with a single step.*
```
**Sample Output 0**
```
a 21 24 29 
and 12 
begins 27 
eating 10 
exercising 17 
if 0 
journey 22 
junk 11 
lose 4 
miles 26 
need 7 14 
not 19 
of 23 
single 30 
start 16 
step 31 
stop 9 
thousand 25 
to 3 8 15 
today 18 
tomorrow 20 
want 2 
weight 5 
with 28 
you 1 6 13
```
## Counter Spiral
Given a square matrix, you have to write a program to print it in a counter-clockwise spiral form.

**Input Format**

The first line of the input contains an integer number n which represents the number of rows and columns in the matrix. From the second line contains n rows with each row having n elements separated by a space.

**Constraints**

1 < N < 1000

**Output Format**

Print the elements in a single line with each element separated by a space

**Sample Input 0**
```
4
25 1 29 7
24 20 4 32
16 38 29 1
48 25 21 19
```
**Sample Output 0**
```
25 24 16 48 25 21 19 1 32 7 29 1 20 38 29 4
```
