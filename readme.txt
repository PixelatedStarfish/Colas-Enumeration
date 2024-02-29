Cola's Enumeration for Naming Large Numbers: An Extension of the Conway-Wechsler System with Truncation of Contiguous Repeating Substrings

--Contents--

Introduction
    What is Cola's Enumeration?
    Conway's illion Converter and the Conway-Weschler System
How Does Cola's Enumeration Work?
    Truncation by use of Greek Numerals
    Examples of Greek and Metric Prefixes
    Going Even Further Beyond: Polymetric Combinations
Program Implementation 
    Comparing Enumerations: "So, is it any good?"
    Limitations of this Program
    Features
Conclusion


Tables of Numbers
    Short Scale Tables
    Long Scale Tables
Change Log
    v1.3
    v1.2
    v1.1
    v1.0
Legal
Sources


--Introduction--

-What is Cola's Enumeration?-

You might be wondering who Cola is. Cola is a Yorkshire Terrier, who is always ready for food, licking, and being carried. You might also be wondering what the Conway-Weschler System is, and why I felt the need to extend it with this enumeration. May this document answer your questions. May you find this document, and its accompanying program, to be as illuminating and enjoyable as I do.

"Cola's Enumeration for Naming Large Numbers: An Extension of the Conway-Wechsler System with Truncation of Contiguous Repeating Substrings" is a counting machine for naming arbitrarily large natural numbers. It is based on the Conway-Weschler System. which can also name arbitrarily large natural numbers with Latin numerals. However, in the Conway-Weschler System the length of names grows rapidly, and names are quickly populated with redundant syllables. For instance, "Millinillinillinillion" has three contiguous "nilli"s, and four "illi"s. Cola's Enumeration truncates this redundancy without loss of information.

-Conway's illion Converter and the Conway-Weschler System-

The Conway-Weschler System is an enumeration created by John Conway, Richard Guy, and Allan Weschler. It was initially published in "The Book of Numbers", written by Conway and Guy in 1995. It was then extended by Conway and Weschler in 1996. Conway's illion Converter, created by Fish in 2021, is a program to automate this system.

So, what is an "illion"? An "illion" is a named with the suffix "illion", in the Conway-Weschler system. These include one million, one billion, one trillion, etc. Fish refers to these numbers as "illion"s, such that "million" is the first "illion", billion is the second, trillion is the third. The Conway-Weschler system extends this "illion" naming convention arbitrarily, by employing Latin numerals in the following manner. 

Given one million (named for a thousand thousands) is considered the "first illion", one billion is the "second illion", and one trillion is the "third illion" then "illions" from the second to the 999th can be named as a portmanteau of a Latin numeral and "(m)illion". The "bi" of billion and "tri" of trillion are consistent with this convention. (See the Sources for a list of Latin numerals.) At the "thousandth illion", this convention would appear to be exhausted. The prefix "milli" would refer to one thousand, but it is already in use by "million", so "millinillion" was coined to allow for further enumerating.

The next "illion", for 1001, would be millimillion. Continuing to the "two thousandth illion", we reach "billinillion". By combining a Latin numeral with the suffix "illinillion", it is possible to enumerate up to the "999,000th illion" by the same method for enumerating to the "999th illion".

The Conway-Weschler system use two "illi"s for the "nillions", which I find a bit verbose. Consider the "999,999th illion", which is called "novenonagintanongentilli-novenonagintanongentillion". "Novenonagintanongentilli" is already a long name, and it gets repeated in this case. What is next? The "millionth illion", which is called "millinillinillion".  Like Cerberus' three heads, this number has three "illi"s. As numbers grow higher, the "illi"s and the Latin just keep piling up, out to infinity!


--How Does Cola's Enumeration Work?--

-Truncation by use of Greek Numerals-

Cola's Enumeration uses Greek numerals (also used for naming polygons) to truncate contiguous, repeated substrings in "illion" numbers, which are named exclusively with Latin numerals in the Conway-Weschler system.

A string composed of the contiguous repeated substring "nilli" looks like this:
    "nillinillinillinillinilli"

The five "nilli"s of this substring can be truncated to "pentanillion" in Cola's Enumeration, with "penta" refering to the Greek numeral for five. Millinillinillinillinillinillion in the Conway-Weschler system is enumerated as mipentanillion in Cola's Enumeration.

-Examples of Greek and Metric Prefixes-

    hena      - 1
    di        - 2
    tri       - 3
    tetra     - 4
    penta     - 5
    hexa      - 6
    hepta     - 7
    octa      - 8
    nona      - 9
    deka      - 10
    undeka    - 11
    dodeka    - 12
    trisdeka  - 13
    tetradeka - 14
    cosa     -  20
    triconta  - 30
    hecta     - 100
    killo     - 1000
    mega      - 10^6
    giga      - 10^9
    tera      - 10^12
    peta      - 10^15
    exa       - 10^18
    zetta     - 10^21
    yotta     - 10^24
    ronna     - 10^27
    quetta    - 10^30


I would like to note that I chose prefixes that were distinct and familiar over ones that were strictly accurate to ancient greek numerals. I chose the most common, simple, and distinct numerals to maximize ease of reading. I also made trivial adaptations to reduce edge cases and improve program efficiency. 

I swapped "deca" for "deka" to distinguish it from "deci". I dropped the "i" in "icosa" to avoid the doubled "i" of "miicosa". I made use of metric prefixes wherever possible ("killo" over "chilla"). To save edge cases, I dropped "myria" for "dekakillo" and switched "hecto" to "hecta".

Take a look at the tables for more information.


-Going Even Further Beyond: Polymetric Combinations and Enumerating Contiguous Quettas-

Suppose you have embarked on a quest to count all of the natural numbers. "One, two, three", you begin. You have already acquired your immortality; you have adventured throughout the jungles, the cities, the deserts, and the seas, and lived thousands of lives. You have studied under the gurus and mastered the 72 transformations. You have seen the empires rise and fall like waves on the water. You have named every bird on every branch of every tree, and all the creatures of the lands and waters. Now you take a breath and count the stars, until each of the skies of the earth are entirely numbered. You leap skyward, and take a vantage point in the heavens. You see new stars, and continue counting. Well beyond the millions, and the vigintillions, and the minillions, you are counting. You admire stars, pulsars, and quasars, and you are still counting. Mikillonillion has long since passed, as have the megas, and the gigas, the teras. You enumerate the stars across clusters of galaxies, by the zettas, and yottas. In search of the edge of reality, you keep counting, but you quickly arrive at miquettanillion. You are out of Latin numerals, and Greek numerals. What now?

By combining prefixes, larger numbers can be counted. Quetta is the metric prefix equivalent to 10^30, it is the largest metric prefix to date. Given killo is 10^3, 10^33 can be described as killoquetta. However, "quettaquetta" would not be far behind, and "quettaquettaquetta" not much farther. What should be done with these repeating "quetta"s?

To truncate these contiguous quettas, count the number of "quetta"s as a Latin numeral, and swap out the "quetta"s for your Latin and a single "quetta".  By this method, "diquetta" is 10^30 * 2, and "biquetta" is 10^30 squared. For another example, "miquettaquettaquettaquettaquettanillion" is better written as mikaiquinquettanillion, and better pronounced as mi-kai-quin-quetta-nillion. Note that "kai" here is Greek for "and". Why is "kai" here? Well, suppose we have a number with a thousand "quetta"s. As "bi" is taken from billion, "mini" is taken from "minillion". The thousand "quetta" number  would be written as "mikaiminiquettanillion"; "kai" separates the two "mi"s neatly.

After much experimenting. I have decided this was too difficult to implement and test with any reliability. The numbers discussed here are too large to be generated in a timely manner and, the most I can do is generate some of the smaller "poly-quetta" Greek prefixes.



 
--Program Implementation--

-Comparing Enumerations-

Cola's Enumeration and Conway's illion Converter were compared for computing time, and output length, over a range of inputs from 1 to 3,000,000. The following was generated: 

Stats for Cola's Enumeration

Average Enumeration Time:   9.07e-06 seconds
Average Enumeration Length: 45.443 characters

Maximum Enumeration Time:   0.03 seconds
Maximum Enumeration Length: 70 characters

Stats for Conway's illion Converter

Average Enumeration Time:   4.49e-06 seconds
Average Enumeration Length: 50.512 characters

Maximum Enumeration Time:   0.034 seconds
Maximum Enumeration Length: 77 characters

Predictably, Cola's Enumeration is generally slower, but produces shorter output. This is expected behavior, because Cola's Enumeration performs addtional computations, specifically to shorten output length. While Conway's illion Converter is faster on average, it has a larger maximum time. The larger maximum time is surprising.

-Limitations of this Program-

- Numbers without repeating contiguous substrings in their respective enumerations will still
  be described with at least one syllable for each non-zero digit. 

- The set of inputs (such that a given input be enumerated in a timely manner) ranges from 
  1 to 10^10^4 (from one to ten to the power of ten thousand). This makes generating enumerations beyond mikillonillion less than practical. 

- There may still be bugs or duplicated names. The space of all inputs too large to test
  exhaustively. 

- Hyper E notation is not extended beyond one octothorpe.

-Features-

- A menu with options for experimenting with Cola's Enumeration and Conway's illion Converter.

- A parser for interpreting inputs expressed with arithmetic operations.

- Output with engineering notation and "Hyper E" notation.

- Tables of numbers.

- Enumeration of random input.

- Implementations of short scale and long scale enumerations.

--Conclusion--

-The Foggy Journey to Fish: Wikis, Blogs, and Citogenesis-

While coming to develop this enumeration has been a joy. I do feel the need to critique the various "illion" series on blogs, websites, and wikis that helped inspire this project. Before I learned of the Conway-Weschler system and Conway's illion converter, I was bouncing around on the Googology wiki, the Massive Numbers wiki, and the Gugology wiki, which I had found by chance. From tab to tab, I found various  notations for describing large numbers, lists of named "illions", novel schemes and magnitudes, and lists of tiers to classify numbers. These contributions, though intriguing, were also in conflict. For example, the Googology wiki page for the "thousandth illion" names this number "millinillion" (as in the Conway-Weschler system) but it also includes names like "millillion", "milliatillion", "milletillion", and "platillion". While I can understand the fun of coining names for these large numbers. I question the pedagogical value of various authors arbitrarily naming various large numbers on a blog or wiki, and compiling the (conflicting) results. 

I understand the apparent irony of this questioning, having just written another numbering system for my own fun, and potentially adding to the confusion. That said, googology has developed a "citogenesis" problem (a term describing the memetic growth of citations, to the point of obfuscating the origin of information, by proliferation and indirection). Take "micrillion", as coined by Johnathan Bowers. This number can be found on his blog with other numbers he has coined. There are wikis citing the blog, and there are forum posts citing the wikis, and there also youtube videos linking to other numbers and blog posts and wikis. As of writing, there are thousands of search engine results for "micrillion", parroting this term into veracity without the context of its creation. 

I understand that the Conway-Weschler system, with its endlessly growing number of "illi"s, is not always a practical convention for naming extremely large numbers, but the system is mathematically, and logically, consistent. 

-To Appreciate Numbers Going Up-

So, you might be wondering why I did this: "Who is ever going to need anything like this?", "Why not just use engineering notation, scientific notation, or arrow notation?" Well, you can use this because it is fun. This is the numeric equivalent of a Rube-Goldberg machine, and that is all it needs to be.

Imagine yourself with a great deal of time on your hands. The year is 2023. You had a nondescript operation, and you have left your tutoring job to go on a medical leave. You pick up a new video game to pass the time. It is the kind of game with a bunch of numbers going up; the kind of game where you can click on some stuff, and go to sleep, and come back to find the numbers have gone up, and now you can spend number (yes, number) to get the mcguffin that makes the numbers go up more quickly. You contemplate strategies for making the numbers go up faster. You visit fan pages and wikis for tips and tricks, for slaying the angry number titans, so you can make the numbers go up faster. The game displays numbers with a suffix by default, (such as "6.283 Million") and as the numbers rise from millions to vigintillions, you become curious as to how the dev has named so many numbers. 

You find a list of large numbers on Wikipedia, a few wikis dedicated to naming numbers, and finally Conway's illion Converter. You push it as high as it will let you, and notice the repeating "illi"s on your screen. In the interest of numeric mischief, you decide to play a numeric joke. You think to yourself "maybe I can write a fork, that names some of these illions 'gazillion' or 'jillion', like in that one episode of Futurama, where Phillip J. Fry bids 'one jillion dollars' at auction, and is met with the reply 'Sir, that's not a real number'." It would be funny if jillion was actually a real, defined number. Things like that are funny when you are on painkillers. So, you make some alterations. Funny stuff. However, the Number-Goblin-that-lives-in-your-head-now is not satisfied with this. 

You remember that English has words for shapes in it. Polygons are named with ancient Greek instead of ancient Latin. You can do something with that. So you do something with that, counting the Latin "illi"s with Greek numerals, and it becomes an enumeration that you can name after your older-brother's-college-roomate's-dog-but-sometimes-also-your-family-dog-because-your-family-is-happy-to-sit. How could anyone resist the opportunity to name something after their beloved family dog? So you decide to write the enumeration and name it after the dog. 



Anyway, have fun with this thing!

-Tables of Numbers-

--Short Scale Tables--

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


        One Million to One Minillion

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
  1000  minillion          1e+3003  10^3003
======  =================  =======  ========


      One Minillion to One Vigintinillion

======  ===================  ========  ========
  I(n)  Suffix               e(#)      Powers
======  ===================  ========  ========
  1000  minillion            1e+3003   10^3003
  2000  binillion            1e+6003   10^6003
  3000  trinillion           1e+9003   10^9003
  4000  quadrinillion        1e+12003  10^12003
  5000  quintinillion        1e+15003  10^15003
  6000  sextinillion         1e+18003  10^18003
  7000  septinillion         1e+21003  10^21003
  8000  octinillion          1e+24003  10^24003
  9000  noninillion          1e+27003  10^27003
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


        One Minillion to One Centinillion

======  ===================  =========  =========
  I(n)  Suffix               e(#)       Powers
======  ===================  =========  =========
  1000  minillion            1e+3003    10^3003
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


         One Minillion to One Midinillion

======  ===================  ==========  ==========
I(n)    Suffix               e(#)        Powers
======  ===================  ==========  ==========
1000    minillion            1e+3003     10^3003
100000  centinillion         1e+300003   10^300003
200000  ducentinillion       1e+600003   10^600003
300000  trecentinillion      1e+900003   10^900003
400000  quadringentinillion  1e+1200003  10^1200003
500000  quingentinillion     1e+1500003  10^1500003
600000  sescentinillion      1e+1800003  10^1800003
700000  septingentinillion   1e+2100003  10^2100003
800000  octingentinillion    1e+2400003  10^2400003
900000  nongentinillion      1e+2700003  10^2700003
10^6    midinillion          1e+3000003  10^3000003
======  ===================  ==========  ==========


             One Minillion to One Micosanillion

======  ==================  ===============  ================
I(n)    Suffix              e(#)             Powers
======  ==================  ===============  ================
1000    minillion           1e+3003          10^3003
10^6    midinillion         1e+3000003       10^3000003
10^9    mitrinillion        1e+3000000003    10^3000000003
10^12   mitetranillion      1e+303#2         10^^2^303
10^15   mipentanillion      1e+300003#2      10^^2^300003
10^18   mihexanillion       1e+300000003#2   10^^2^300000003
10^21   miheptanillion      1e+33#3          10^^3^33
10^24   mioctanillion       1e+30003#3       10^^3^30003
10^27   minonanillion       1e+30000003#3    10^^3^30000003
10^30   midekanillion       1e+6#4           10^^4^6
10^33   miundekanillion     1e+3003#4        10^^4^3003
10^36   midodekanillion     1e+3000003#4     10^^4^3000003
10^39   mitrisdekanillion   1e+3000000003#4  10^^4^3000000003
10^42   mitetradekanillion  1e+303#5         10^^5^303
10^45   mipentadekanillion  1e+300003#5      10^^5^300003
10^48   mihexadekanillion   1e+300000003#5   10^^5^300000003
10^51   miheptadekanillion  1e+33#6          10^^6^33
10^54   mioctadekanillion   1e+30003#6       10^^6^30003
10^57   minonadekanillion   1e+30000003#6    10^^6^30000003
10^60   micosanillion       1e+6#7           10^^7^6
======  ==================  ===============  ================


       One Minillion to One Mihectanillion

======  ======================  =======  ========
I(n)    Suffix                  e(#)     Powers
======  ======================  =======  ========
1000    minillion               1e+3003  10^3003
10^30   midekanillion           1e+6#4   10^^4^6
10^60   micosanillion           1e+6#7   10^^7^6
10^90   mitricontakainillion    1e+6#10  10^^10^6
10^120  mitetracontakainillion  1e+6#13  10^^13^6
10^150  mipentacontakainillion  1e+6#16  10^^16^6
10^180  mihexacontakainillion   1e+6#19  10^^19^6
10^210  miheptacontakainillion  1e+6#22  10^^22^6
10^240  mioctacontakainillion   1e+6#25  10^^25^6
10^270  minonacontakainillion   1e+6#28  10^^28^6
10^300  mihectanillion          1e+6#31  10^^31^6
======  ======================  =======  ========


      One Mihectanillion to One Mikillonillion

=======  ======================  ========  =========
I(n)     Suffix                  e(#)      Powers
=======  ======================  ========  =========
10^300   mihectanillion          1e+6#31   10^^31^6
10^600   midihectanillion        1e+6#61   10^^61^6
10^900   mitrihectakainillion    1e+6#91   10^^91^6
10^1200  mitetrahectakainillion  1e+6#121  10^^121^6
10^1500  mipentahectakainillion  1e+6#151  10^^151^6
10^1800  mihexahectakainillion   1e+6#181  10^^181^6
10^2100  miheptahectakainillion  1e+6#211  10^^211^6
10^2400  mioctahectakainillion   1e+6#241  10^^241^6
10^2700  minonahectakainillion   1e+6#271  10^^271^6
10^3000  mikillonillion          1e+6#301  10^^301^6
=======  ======================  ========  =========


-Long Scale Tables-

Notes on the Tables:
I(n) = 10^(6n) [Long scale]

^ indicates exponentiation
^^ indicates repeated exponentiation (tetration)
e+ notates a power of 10
e# describes a tetration of 10 (as hyper e notation)


      One Million to One Vigintillion

======  =================  ======  ========
  I(n)  Suffix               e(#)  Powers
======  =================  ======  ========
     1  million            1e+06   10^6
     2  billion            1e+12   10^12
     3  trillion           1e+18   10^18
     4  quadrillion        1e+24   10^24
     5  quintillion        1e+30   10^30
     6  sextillion         1e+36   10^36
     7  septillion         1e+42   10^42
     8  octillion          1e+48   10^48
     9  nonillion          1e+54   10^54
    10  decillion          1e+60   10^60
    11  undecillion        1e+66   10^66
    12  duodecillion       1e+72   10^72
    13  tredecillion       1e+78   10^78
    14  quattuordecillion  1e+84   10^84
    15  quindecillion      1e+90   10^90
    16  sedecillion        1e+96   10^96
    17  septendecillion    1e+102  10^102
    18  octodecillion      1e+108  10^108
    19  novendecillion     1e+114  10^114
    20  vigintillion       1e+120  10^120
======  =================  ======  ========


       One Million to One Centillion

======  =================  ======  ========
  I(n)  Suffix             e(#)    Powers
======  =================  ======  ========
     1  million            1e+6    10^6
    10  decillion          1e+60   10^60
    20  vigintillion       1e+120  10^120
    30  trigintillion      1e+180  10^180
    40  quadragintillion   1e+240  10^240
    50  quinquagintillion  1e+300  10^300
    60  sexagintillion     1e+360  10^360
    70  septuagintillion   1e+420  10^420
    80  octogintillion     1e+480  10^480
    90  nonagintillion     1e+540  10^540
   100  centillion         1e+600  10^600
======  =================  ======  ========


        One Million to One Minillion

======  =================  =======  ========
  I(n)  Suffix             e(#)     Powers
======  =================  =======  ========
     1  million            1e+6     10^6
   100  centillion         1e+600   10^600
   200  ducentillion       1e+1200  10^1200
   300  trecentillion      1e+1800  10^1800
   400  quadringentillion  1e+2400  10^2400
   500  quingentillion     1e+3000  10^3000
   600  sescentillion      1e+3600  10^3600
   700  septingentillion   1e+4200  10^4200
   800  octingentillion    1e+4800  10^4800
   900  nongentillion      1e+5400  10^5400
  1000  minillion          1e+6000  10^6000
======  =================  =======  ========


       One Minillion to One Vigintinillion

======  ===================  =========  =========
  I(n)  Suffix               e(#)       Powers
======  ===================  =========  =========
  1000  minillion            1e+6000    10^6000
  2000  binillion            1e+12000   10^12000
  3000  trinillion           1e+18000   10^18000
  4000  quadrinillion        1e+24000   10^24000
  5000  quintinillion        1e+30000   10^30000
  6000  sextinillion         1e+36000   10^36000
  7000  septinillion         1e+42000   10^42000
  8000  octinillion          1e+48000   10^48000
  9000  noninillion          1e+54000   10^54000
 10000  decinillion          1e+60000   10^60000
 11000  undecinillion        1e+66000   10^66000
 12000  duodecinillion       1e+72000   10^72000
 13000  tredecinillion       1e+78000   10^78000
 14000  quattuordecinillion  1e+84000   10^84000
 15000  quindecinillion      1e+90000   10^90000
 16000  sedecinillion        1e+96000   10^96000
 17000  septendecinillion    1e+102000  10^102000
 18000  octodecinillion      1e+108000  10^108000
 19000  novendecinillion     1e+114000  10^114000
 20000  vigintinillion       1e+120000  10^120000
======  ===================  =========  =========


        One Minillion to One Centinillion

======  ===================  =========  =========
  I(n)  Suffix               e(#)       Powers
======  ===================  =========  =========
  1000  minillion            1e+3003    10^3003
 10000  decinillion          1e+60000   10^60000
 20000  vigintinillion       1e+120000  10^120000
 30000  trigintanillion      1e+180000  10^180000
 40000  quadragintanillion   1e+240000  10^240000
 50000  quinquagintanillion  1e+300000  10^300000
 60000  sexagintanillion     1e+360000  10^360000
 70000  septuagintanillion   1e+420000  10^420000
 80000  octogintanillion     1e+480000  10^480000
 90000  nonagintanillion     1e+540000  10^540000
100000  centinillion         1e+600000  10^600000
======  ===================  =========  =========


         One Minillion to One Midinillion

======  ===================  ==========  ==========
I(n)    Suffix               e(#)        Powers
======  ===================  ==========  ==========
1000    minillion            1e+3003     10^3003
100000  centinillion         1e+600000   10^600000
200000  ducentinillion       1e+1200000  10^1200000
300000  trecentinillion      1e+1800000  10^1800000
400000  quadringentinillion  1e+2400000  10^2400000
500000  quingentinillion     1e+3000000  10^3000000
600000  sescentinillion      1e+3600000  10^3600000
700000  septingentinillion   1e+4200000  10^4200000
800000  octingentinillion    1e+4800000  10^4800000
900000  nongentinillion      1e+5400000  10^5400000
10^6    midinillion          1e+6000000  10^6000000
======  ===================  ==========  ==========


             One Minillion to One Micosanillion

======  ==================  ===============  ================
I(n)    Suffix              e(#)             Powers
======  ==================  ===============  ================
1000    minillion           1e+6000          10^6000
10^6    midinillion         1e+6000000       10^6000000
10^9    mitrinillion        1e+6000000000    10^6000000000
10^12   mitetranillion      1e+600#2         10^^2^600
10^15   mipentanillion      1e+600000#2      10^^2^600000
10^18   mihexanillion       1e+600000000#2   10^^2^600000000
10^21   miheptanillion      1e+60#3          10^^3^60
10^24   mioctanillion       1e+60000#3       10^^3^60000
10^27   minonanillion       1e+60000000#3    10^^3^60000000
10^30   midekanillion       1e+6#4           10^^4^6
10^33   miundekanillion     1e+6000#4        10^^4^6000
10^36   midodekanillion     1e+6000000#4     10^^4^6000000
10^39   mitrisdekanillion   1e+6000000000#4  10^^4^6000000000
10^42   mitetradekanillion  1e+600#5         10^^5^600
10^45   mipentadekanillion  1e+600000#5      10^^5^600000
10^48   mihexadekanillion   1e+600000000#5   10^^5^600000000
10^51   miheptadekanillion  1e+60#6          10^^6^60
10^54   mioctadekanillion   1e+60000#6       10^^6^60000
10^57   minonadekanillion   1e+60000000#6    10^^6^60000000
10^60   micosanillion       1e+6#7           10^^7^6
======  ==================  ===============  ================


       One Minillion to One Mihectanillion

======  ======================  =======  ========
I(n)    Suffix                  e(#)     Powers
======  ======================  =======  ========
1000    minillion               1e+6000  10^6000
10^30   midekanillion           1e+6#4   10^^4^6
10^60   micosanillion           1e+6#7   10^^7^6
10^90   mitricontakainillion    1e+6#10  10^^10^6
10^120  mitetracontakainillion  1e+6#13  10^^13^6
10^150  mipentacontakainillion  1e+6#16  10^^16^6
10^180  mihexacontakainillion   1e+6#19  10^^19^6
10^210  miheptacontakainillion  1e+6#22  10^^22^6
10^240  mioctacontakainillion   1e+6#25  10^^25^6
10^270  minonacontakainillion   1e+6#28  10^^28^6
10^300  mihectanillion          1e+6#31  10^^31^6
======  ======================  =======  ========


      One Mihectanillion to One Mikillonillion

=======  ======================  ========  =========
I(n)     Suffix                  e(#)      Powers
=======  ======================  ========  =========
10^300   mihectanillion          1e+6#31   10^^31^6
10^600   midihectanillion        1e+6#61   10^^61^6
10^900   mitrihectakainillion    1e+6#91   10^^91^6
10^1200  mitetrahectakainillion  1e+6#121  10^^121^6
10^1500  mipentahectakainillion  1e+6#151  10^^151^6
10^1800  mihexahectakainillion   1e+6#181  10^^181^6
10^2100  miheptahectakainillion  1e+6#211  10^^211^6
10^2400  mioctahectakainillion   1e+6#241  10^^241^6
10^2700  minonahectakainillion   1e+6#271  10^^271^6
10^3000  mikillonillion          1e+6#301  10^^301^6
=======  ======================  ========  =========

--Changelog--

-v1.3-

inputs 103 and 300 had the same output, this was due to a block that had remained indented to deeply after removing the clasues for the "modified" system. 

Removed a stubborn bug. The output "centillion" was repeated for 101 - 109.
This persisted for each hundred.

Added a test to identify these duplications. Iterate, and if I(n) = I(n + 1) break. This is a linear time test, which allows for a search over many inputs.

-v1.2-

Changed "tria" to "tri" for simplicity
Implemented long scale
Modified names such that each has only one "illi"
Greatly simplified the "supermetric" portion of this project. (I had to break some easter eggs.)

Inputs less than one are supported

Updated tables and menu options accordingly

Removed "Boring" and "Wacky" tests

-v1.1-

Optimized parsing, now digits are parsed instead of strings.
This reduces the required parsing significantly.
Additional "on's" are also no longer required. 

Added speed tests, "Boring" and "Wacky".
One is for typical inputs, powers of ten and the like.
The wacky one had a bug that produced all sorts of crazy numbers people do not think about, the perfect edge case generator.

Various optimizations and bug fixes.
The time to process 10^10^4 has dropped from over 30 seconds to less than a quarter of a second on my machine.

-v1.0-

Initial release


--Legal--

Cola's Enumeration is by AndrewJ (PixelatedStarfish). Copyright 2024
Conway's illion Converter is by Fish. Copyright 2023

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


--Sources--

Large Numbers
https://mrob.com/pub/math/largenum.html

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

Many Sided Shapes
https://benpittstoller.com/Misc/ManySidedShapes.html

Metric Prefixes
https://www.nist.gov/pml/owm/metric-si-prefixes

Latin Numerals
https://en.wikipedia.org/wiki/Latin_numerals#:~:text=M%C4%ABlle%20'1000'%20is%20indeclinable%20in,m%C4%ABlle%2C%20deinde%20centum%20(Catullus)

Bowers, Illion Numbers
https://www.polytope.net/hedrondude/illion.htm

XKCD, Citogenesis
https://www.explainxkcd.com/wiki/index.php/978:_Citogenesis

"Micrillion" Search of 12,000 results
https://www.google.com/search?q=micriliion&rlz=1C1VDKB_enUS965US965&oq=micriliion&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIPCAEQABgNGIMBGLEDGIAEMg8IAhAAGA0YgwEYsQMYgAQyDwgDEAAYDRiDARixAxiABDIPCAQQABgNGIMBGLEDGIAEMg8IBRAAGA0YgwEYsQMYgAQyCQgGEAAYDRiABDIJCAcQABgNGIAEMgkICBAAGA0YgAQyCQgJEAAYDRiABNIBCDQyNTVqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8#ip=1

NGU IDLE
https://store.steampowered.com/app/1147690/NGU_IDLE/
