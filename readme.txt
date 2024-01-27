Cola's Enumeration for Naming Large Numbers: An Extension of the Conway-Wechsler System with Truncation of Contiguous Repeating Substrings

--Introduction--

You might be wondering who Cola is. Cola is a dog, who is always ready for food, licking, and being carried. 

I played an idle game about Numbers Going Up, and I wondered just how far the numbers go up before there are no more names for them. I found a list of large numbers on Wikipedia, a few wikis dedicated to naming numbers, and finally Conway's illion Converter, created by Fish. What followed is now a month long joke I have played on myself. 

An "illion" is defined as a number with a name that ends in "illion". These can also be called zillions, but the important thing is that each has a unique, pronounceable name. Sometimes illions are named numerically such that "million" is the "first illion" and "billion" is the second (in the short scale).

"Illions" can be defined according to a function I(n) = 10^(3n +3) such that I(n) is equal to 10, raised to the power of (3n + 3). Conway's illion Converter makes use of this function, and parses the result to generate names for the resulting "illions".The most critical detail is that prefixes and suffixes start repeating fast.

I(1) is one million
I(1000) is one millinillion
I(1 000 000) is one millinillinillion
I(1 000 000 000) is one millinillinillinillion

...and from there the "nilli"s just keep piling up! So, for this project, I turned to polygonal nomenclature. I opted for the most distinct prefixes and got to work shortening these names for as many numbers as I could manage.

I am happy with the results and I think you will be too, even if you use the long scale.


--Notes on This Numbering System--

This is an extension of the Conway-Wechsler system.
It uses Greek prefixes (for polygons) to truncate contiguous, repeated substrings.

A contiguous repeated substring "likethis" looks like this:

    likethislikethislikethislikethislikethislikethis

Conway's illion Converter (by Fish) will produce these substrings when pushed to handle extremely large numbers. Such as "millinillinillinilli..."  (In the interest of numeric mischief, pushing the converter as far as I could was one of the first things I did.)

With the addition of this polygon naming convention, names can be shortened significantly, especially at "milestone numbers" such as those listed in the tables below.

"millimillion" becomes dimillion.
"millinillinillion" becomes millidinillion.

Take a look at the (short scale) tables for more information.


--Tables of Numbers--

Notes on the Tables:
I(n) = 10^(3n + 3)

^ indicates exponentiation
^^ indicates repeated exponentiation (tetration)
e+ notates a power of 10
e# describes a tetration of 10 (as hyper e notation)


      One Million to One Vigintillion

======  =================  ======  ========
  I(n)  Suffix               e(#)  Powers
======  =================  ======  ========
     1  million             1e+06  10^6
     2  billion             1e+09  10^9
     3  trillion            1e+12  10^12
     4  quadrillion         1e+15  10^15
     5  quintillion         1e+18  10^18
     6  sextillion          1e+21  10^21
     7  septillion          1e+24  10^24
     8  octillion           1e+27  10^27
     9  nonillion           1e+30  10^30
    10  decillion           1e+33  10^33
    11  undecillion         1e+36  10^36
    12  duodecillion        1e+39  10^39
    13  tredecillion        1e+42  10^42
    14  quattuordecillion   1e+45  10^45
    15  quindecillion       1e+48  10^48
    16  sedecillion         1e+51  10^51
    17  septendecillion     1e+54  10^54
    18  octodecillion       1e+57  10^57
    19  novendecillion      1e+60  10^60
    20  vigintillion        1e+63  10^63
======  =================  ======  ========


       One Million to One Centillion

======  =================  ======  ========
  I(n)  Suffix               e(#)  Powers
======  =================  ======  ========
     1  million            1e+06   10^6
    10  decillion          1e+33   10^33
    20  vigintillion       1e+63   10^63
    30  trigintillion      1e+93   10^93
    40  quadragintillion   1e+123  10^123
    50  quinquagintillion  1e+153  10^153
    60  sexagintillion     1e+183  10^183
    70  septuagintillion   1e+213  10^213
    80  octogintillion     1e+243  10^243
    90  nonagintillion     1e+273  10^273
   100  centillion         1e+303  10^303
======  =================  ======  ========


       One Million to One Millinillion

======  =================  =======  ========
  I(n)  Suffix             e(#)     Powers
======  =================  =======  ========
     1  million            1e+6     10^6
   100  centillion         1e+303   10^303
   200  ducentillion       1e+603   10^603
   300  trecentillion      1e+903   10^903
   400  quadringentillion  1e+1203  10^1203
   500  quingentillion     1e+1503  10^1503
   600  sescentillion      1e+1803  10^1803
   700  septingentillion   1e+2103  10^2103
   800  octingentillion    1e+2403  10^2403
   900  nongentillion      1e+2703  10^2703
  1000  millinillion       1e+3003  10^3003
======  =================  =======  ========


    One Millinillion to One Vigintinillion

======  ===================  ========  ========
  I(n)  Suffix               e(#)      Powers
======  ===================  ========  ========
  1000  millinillion         1e+3003   10^3003
  2000  billinillion         1e+6003   10^6003
  3000  trillinillion        1e+9003   10^9003
  4000  quadrillinillion     1e+12003  10^12003
  5000  quintillinillion     1e+15003  10^15003
  6000  sextillinillion      1e+18003  10^18003
  7000  septillinillion      1e+21003  10^21003
  8000  octillinillion       1e+24003  10^24003
  9000  nonillinillion       1e+27003  10^27003
 10000  decinillion          1e+30003  10^30003
 11000  undecinillion        1e+33003  10^33003
 12000  duodecinillion       1e+36003  10^36003
 13000  tredecinillion       1e+39003  10^39003
 14000  quattuordecinillion  1e+42003  10^42003
 15000  quindecinillion      1e+45003  10^45003
 16000  sedecinillion        1e+48003  10^48003
 17000  septendecinillion    1e+51003  10^51003
 18000  octodecinillion      1e+54003  10^54003
 19000  novendecinillion     1e+57003  10^57003
 20000  vigintinillion       1e+60003  10^60003
======  ===================  ========  ========
*Note that the leftmost "illi" is dropped after the nonillinillion

      One Millinillion to One Centinillion

======  ===================  =========  =========
  I(n)  Suffix               e(#)       Powers
======  ===================  =========  =========
  1000  millinillion         1e+3003    10^3003
 10000  decinillion          1e+30003   10^30003
 20000  vigintinillion       1e+60003   10^60003
 30000  trigintanillion      1e+90003   10^90003
 40000  quadragintanillion   1e+120003  10^120003
 50000  quinquagintanillion  1e+150003  10^150003
 60000  sexagintanillion     1e+180003  10^180003
 70000  septuagintanillion   1e+210003  10^210003
 80000  octogintanillion     1e+240003  10^240003
 90000  nonagintanillion     1e+270003  10^270003
100000  centinillion         1e+300003  10^300003
======  ===================  =========  =========


      One Millinillion to One Millidinillion

======  ===================  ==========  ==========
I(n)    Suffix               e(#)        Powers
======  ===================  ==========  ==========
1000    millinillion         1e+3003     10^3003
100000  centinillion         1e+300003   10^300003
200000  ducentinillion       1e+600003   10^600003
300000  trecentinillion      1e+900003   10^900003
400000  quadringentinillion  1e+1200003  10^1200003
500000  quingentinillion     1e+1500003  10^1500003
600000  sescentinillion      1e+1800003  10^1800003
700000  septingentinillion   1e+2100003  10^2100003
800000  octingentinillion    1e+2400003  10^2400003
900000  nongentinillion      1e+2700003  10^2700003
10^6    millidinillion       1e+3000003  10^3000003
======  ===================  ==========  ==========


            One Millinillion to One Millicosanillion

======  =====================  ===============  ================
I(n)    Suffix                 e(#)             Powers
======  =====================  ===============  ================
1000    millinillion           1e+3003          10^3003
10^6    millidinillion         1e+3000003       10^3000003
10^9    millitrianillion       1e+3000000003    10^3000000003
10^12   millitetranillion      1e+303#2         10^^2^303
10^15   millipentanillion      1e+300003#2      10^^2^300003
10^18   millihexanillion       1e+300000003#2   10^^2^300000003
10^21   milliheptanillion      1e+33#3          10^^3^33
10^24   millioctanillion       1e+30003#3       10^^3^30003
10^27   millinonanillion       1e+30000003#3    10^^3^30000003
10^30   millidekanillion       1e+6#4           10^^4^6
10^33   milliundekanillion     1e+3003#4        10^^4^3003
10^36   millidodekanillion     1e+3000003#4     10^^4^3000003
10^39   millitrisdekanillion   1e+3000000003#4  10^^4^3000000003
10^42   millitetradekanillion  1e+303#5         10^^5^303
10^45   millipentadekanillion  1e+300003#5      10^^5^300003
10^48   millihexadekanillion   1e+300000003#5   10^^5^300000003
10^51   milliheptadekanillion  1e+33#6          10^^6^33
10^54   millioctadekanillion   1e+30003#6       10^^6^30003
10^57   millinonadekanillion   1e+30000003#6    10^^6^30000003
10^60   millicosanillion       1e+6#7           10^^7^6
======  =====================  ===============  ================


      One Millinillion to One Millihectanillion

======  =========================  =======  ========
I(n)    Suffix                     e(#)     Powers
======  =========================  =======  ========
1000    millinillion               1e+3003  10^3003
10^30   millidekanillion           1e+6#4   10^^4^6
10^60   millicosanillion           1e+6#7   10^^7^6
10^90   millitricontakainillion    1e+6#10  10^^10^6
10^120  millitetracontakainillion  1e+6#13  10^^13^6
10^150  millipentacontakainillion  1e+6#16  10^^16^6
10^180  millihexacontakainillion   1e+6#19  10^^19^6
10^210  milliheptacontakainillion  1e+6#22  10^^22^6
10^240  millioctacontakainillion   1e+6#25  10^^25^6
10^270  millinonacontakainillion   1e+6#28  10^^28^6
10^300  millihectanillion          1e+6#31  10^^31^6
======  =========================  =======  ========


    One Millihectanillion to One Millikillonillion

=======  =========================  ========  =========
I(n)     Suffix                     e(#)      Powers
=======  =========================  ========  =========
10^300   millihectanillion          1e+6#31   10^^31^6
10^600   millidihectanillion        1e+6#61   10^^61^6
10^900   millitrihectakainillion    1e+6#91   10^^91^6
10^1200  millitetrahectakainillion  1e+6#121  10^^121^6
10^1500  millipentahectakainillion  1e+6#151  10^^151^6
10^1800  millihexahectakainillion   1e+6#181  10^^181^6
10^2100  milliheptahectakainillion  1e+6#211  10^^211^6
10^2400  millioctahectakainillion   1e+6#241  10^^241^6
10^2700  millinonahectakainillion   1e+6#271  10^^271^6
10^3000  millikillonillion          1e+6#301  10^^301^6
=======  =========================  ========  =========


--Going Even Further Beyond: Metric and Wow Numbers--

Numbers on the order of millimeganillion and beyond take too long to generate in a timely manner (for me). However, the optimized greekifier module can still produce the necessary prefixes in a reasonable amount of time. 

For each metric prefix, from killo to quetta, there is a corresponding milli[prefix]nillion. This, still, is not nearly as large as the numbers can get, but first, a sidenote.


-Sidenote: Apologies to the Greek Fans-

I would like to note that I chose prefixes that were distinct and familiar over ones that were strictly greek. I picked, "di" over "bi", and "killo" over "chilla". I swapped "deca" for "deka" to distinguish it from "deci". I dropped the "i" in "icosa" to avoid "milliicosa". Finally, I dropped "myria" for "dekakillo" because it is easier to read and more efficient programatically (saving an edge case).


-What is Supermetric?-

That is a word I made up... that's it. Why did I do that? Well, it benefits this project to extend this system to absurd proportions, and I did not feel like waiting thirty years for new metric prefixes to develop.

alpha   10^48   alphecto   10^(-48)
kyoda   10^45   kyodecto   10^(-45)
wechsla 10^42   wechslo    10^(-42)
conwa   10^39   conwo      10^(-39) 
ortensa 10^36   ortenso    10^(-36)
jana    10^33   janecto    10^(-33)
quetta  10^30   quecto     10^(-30)

I did not invent an arbitrary number of prefixes, but I needed prefixes up to 10^48 because that is the sqaure of "yotta". Otherwise, names just get flooded with repeated "yotta"s. So, I decided to just make up prefixes until I filled the gap to 10^48. What happens at 10^48? Well...


-Greek Alphabetic Prefixes and Wow Numbers-

10^48 is called "alpha". "beta" is the square of alpha. "gamma" is the square of "beta". Upon exhausting the entire Greek alphabet (after omega), we reach "wowalpha" and "wowomega" soon after. Then, "wowomega" is followed by "diwowalpha" such that the "wow"s ultimately start compounding. One can imagine a number named "milli[some long string contiguous 'wowomega's]nillion, describing some arbitrarily large number. 

  *Why "wow"? It was easier to distinguish than "wau" in a long string!

  *Please note the prefixes denoting values less than 10 are not used to generate names.
  That said, you are free to extrapolate: "becto", "gammecto" "decto", "epsilecto"...
  dropping the last vowel from the corresponding prefix and concatenating "ecto" accordingly.
  Perhaps my prefixes will be adopted by the General Conference on Weights and Measures, as a scheme for arbitrary extension. "Big Jane", and "Hortens" are from my maternal grandfather's early years. They are joined here by Conway, Wechsler, and Kyoda (Fish). 


--Final Thoughts: (What's next?)--

If you want to name numbers without limit, you do eventually have to start repeating strings. I like to think I have kicked that can far down the proverbial road. That said, I have seen the wikis and I know there are named numbers still farther on. The thing is, I have pushed this implementation about as hard as I could to generate names fast. It becomes more difficult to test and debug as numbers grow.  

Dropping insignificant figures would be excellent, but this requires parting with millions at some point, and then millinillions... who wants that? 

Another option is to decide that "millikillonillion" is the cut off point. At (and past) that point, something increments, tables get updated, and I(n) gets a new definition. I(1) is now equal to millikillonillon, but millikillionillion is renamed to "zillion", or whatever. Now, I(2) is bizillion. I(1000) is zillinillion. At "zillikillonillion" (and beyond) this happens again and everything gets updated for the next name. Fill a text file with a few (hundred) names. When those run out, tack on "wow"s at the left, then "diwow"s, on through to endless "wow"s...   

Anyway, have fun with this thing!


--Changelog v1.1--

Optimized parsing, now digits are parsed instead of strings.
This reduces the required parsing significantly.
Additional "on's" are also no longer required. 

Added speed tests, "Boring" and "Wacky".
One is for typical inputs, powers of ten and the like.
The wacky one had a bug that produced all sorts of crazy numbers people do not think about, the perfect edge case generator.

Various optimizations and bug fixes.
The time to process 10^10^4 has dropped from over 30 seconds to less than a quarter of a second (on my machine).


--Legal--

Cola's Enumeration is by PixelatedStarfish. Copyright 2024
Conway's illion Converter is by Fish. Copyright 2023

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


--Sources--

Conway's illion Converter
https://kyodaisuu.github.io/illion/conway.html

Conway's illion Converter Source
https://github.com/kyodaisuu/kyodaisuu.github.io/blob/main/illion/zillion.py

Tetration
https://en.wikipedia.org/wiki/Tetration

Hyper E Notation
https://googology.fandom.com/wiki/Hyper-E_notation

Polygon List (Greek Prefix List)
https://en.wikipedia.org/wiki/List_of_polygons#List%20of%20n-gons%20by%20Greek%20numerical%20prefixes

Metric Prefixes
https://www.nist.gov/pml/owm/metric-si-prefixes
