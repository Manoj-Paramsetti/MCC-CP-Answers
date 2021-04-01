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