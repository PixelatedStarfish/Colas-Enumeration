The Apeironillion Numbering System: An Extension of the Conway-Wechsler System with Truncation of Contiguous Substrings

-Legal-
Copyright 2024 PixelatedStarfish
Copyright 2023 Fish for Conway's illion Converter including zillions.py

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



-Introduction-
I played an idle game about Numbers Going Up, and I wondered just how far the numbers go up before there are no more names for them. I found a list of large numbers on Wikipedia, a few wikis dedicated to naming numbers, and finally Conway's illion Converter, created by Fish. 

An "illion" is defined as a number with a name that ends in "illion". These can also be called zillions, but the important thing is that each has a unique, pronouncable name. Sometimes illions are named numerically such that "million" is the "first illion", "billion" is the second, etc.

Illions can be defined according to a function I(n) = 10^(3n +3) such that I(n) is equal to 10, raised to the power of (3n + 3). Conway's illion Converter makes use of this function, and parses the result to generate names for the resulting illions. Names are based on the Conway-Wechsler system, which is explained in detail at the illion converter's site, see sources at the bottom. The most critical detail is that prefixes and suffixes start repeating fast.

I(1) is one million
I(100) is one centillion
I(1000) is one millinillion
I(1001) is one millimillion
I(2000) is one billinillion

I(1 000 000 000) is one millinillinillinillion, and from there the "nilli"s just keep piling up! My first thought was "Wouldn't it be funny if one zillion was actually a defined number? I'll play a trick on the illion converter! I'll modify zillions.py to output literal zillions, starting with I(1 000 000 000)."   

See, due to a recent operation I have had quite of bit of time to sit around and program. So I did that, and it worked just fine. "one millinillinillinillion" was now one zillion. All I had to do was alter the prefix table and make some string replacements. I added more names, and put them in a text file (bazillion, trazillion, fishillion). People on the wikis had their own personal names for these numbers, so I figured they could write their own text files with the names they like and load them in to my mod. Then I hit a wall.

This idea  works out for I(n) but only n is a power of ten. Otherwise numbers would actually not be shortened at all. At best, an "m" would get replaced with "z" or "baz", but names were still full of long strings of repeating latin. You can experiment with v0.1 to see this in action.

For version 1.0 of this project, I turned to polygons. I opted for the most distinct prefixes available to use and got to work, turning millimillion into dimillion. (The "di" means milli would be repeated twice).

I tooks a few liberties, dropping repeated vowels, and employing some metric prefixes. I also changed deca to deka, to avoid confusion with deci, but I am happy with the results and I think you will be too.

Before moving on, I'd like to note the limits of this implementation. A downside to greekification is that each input is parsed once by the illion converter, and again by the greekifier. This costs more time. I(10^10^4) can take up to a minute for me! (I did not even allow tetration!)

I would like to cut down on parsing as much as possible, by using tables of numbers. Right now, every time you give I(1) to process the converter reconstructs "million" each time. This was fast enough for Conway's illion converter, but once the numbers are getting Greek a second (and less efficient) parse happens. I would prefer that the names of so called "milestones" get stored in hash tables, so that parsing out these numbers can be skipped altogether. What parsing is left over can be done more quickly, by refering back to these tables.

-Notes on This Numbering System-

This is an extension of the Conway-Wechsler system.
It uses Greek prefixes (for polygons) to truncate contiguous, repeated substrings.

A contiguous repeated substring "likethis" looks like this:

    likethislikethislikethislikethislikethislikethis

Conway's illion Converter (by Fish) will produce these substrings when pushed to handle extremely large numbers. Such as "millinillinillinilli..."  

(In the interest of numeric mischief, pushing the converter as far as I could was one of the first things I did.)

With the addition of this polygon naming convention, names can be shortened significantly especially at "milestone numbers" such as those listed in the tables below.

"millimillion" becomes dimillion.
"millinillinillion" becomes millidinillion.

Note that one millidinillion added with one million is millidinillionmillion. The first "ion" indicates that "di" 
truncates "nillinilli" and not "nillimillinillimilli" 


-Tables of Numbers-

Notes on the Tables:
I(n) = 10^(3n + 3) 

^ indicates exponentiation
^^ indicates repeated exponentiation (tetration)
E is exponent notation
E# describes a tetration (via Hyper E notation)


     One Million to One Vigintillion

====  =================  ======  ========
I(n)  Suffix             E(#)    Powers
====  =================  ======  ========
  1   million             1e+06  10^6
  2   billion             1e+09  10^9
  3   trillion            1e+12  10^12
  4   quadrillion         1e+15  10^15
  5   quintillion         1e+18  10^18
  6   sextillion          1e+21  10^21
  7   septillion          1e+24  10^24
  8   octillion           1e+27  10^27
  9   nonillion           1e+30  10^30
 10   decillion           1e+33  10^33
 11   undecillion         1e+36  10^36
 12   duodecillion        1e+39  10^39
 13   tredecillion        1e+42  10^42
 14   quattuordecillion   1e+45  10^45
 15   quindecillion       1e+48  10^48
 16   sedecillion         1e+51  10^51
 17   septendecillion     1e+54  10^54
 18   octodecillion       1e+57  10^57
 19   novendecillion      1e+60  10^60
 20   vigintillion        1e+63  10^63
====  =================  ======  ========


      One Million to One Centillion

====  =================  ======  ========
I(n)  Suffix             E(#)    Powers
====  =================  ======  ========
  1   million            1e+06   10^6
 10   decillion          1e+33   10^33
 20   vigintillion       1e+63   10^63
 30   trigintillion      1e+93   10^93
 40   quadragintillion   1e+123  10^123
 50   quinquagintillion  1e+153  10^153
 60   sexagintillion     1e+183  10^183
 70   septuagintillion   1e+213  10^213
 80   octogintillion     1e+243  10^243
 90   nonagintillion     1e+273  10^273
100   centillion         1e+303  10^303
====  =================  ======  ========


     One Million to One Millinillion

====  =================  ======  ========
I(n)  Suffix             E(#)    Powers
====  =================  ======  ========
   1  million            1E6     10^6
 100  centillion         1E303   10^303
 200  ducentillion       1E603   10^603
 300  trecentillion      1E903   10^903
 400  quadringentillion  1E1203  10^1203
 500  quingentillion     1E1503  10^1503
 600  sescentillion      1E1803  10^1803
 700  septingentillion   1E2103  10^2103
 800  octingentillion    1E2403  10^2403
 900  nongentillion      1E2703  10^2703
1000  millinillion       1E3003  10^3003
====  =================  ======  ========


    One Millinillion to One Vigintillinillion

=====  ======================  =======  ========
I(n)   Suffix                  E(#)     Powers
=====  ======================  =======  ========
 1000  millinillion            1E3003   10^3003
 2000  billinillion            1E6003   10^6003
 3000  trillinillion           1E9003   10^9003
 4000  quadrillinillion        1E12003  10^12003
 5000  quintillinillion        1E15003  10^15003
 6000  sextillinillion         1E18003  10^18003
 7000  septillinillion         1E21003  10^21003
 8000  octillinillion          1E24003  10^24003
 9000  nonillinillion          1E27003  10^27003
10000  decillinillion          1E30003  10^30003
11000  undecillinillion        1E33003  10^33003
12000  duodecillinillion       1E36003  10^36003
13000  tredecillinillion       1E39003  10^39003
14000  quattuordecillinillion  1E42003  10^42003
15000  quindecillinillion      1E45003  10^45003
16000  sedecillinillion        1E48003  10^48003
17000  septendecillinillion    1E51003  10^51003
18000  octodecillinillion      1E54003  10^54003
19000  novendecillinillion     1E57003  10^57003
20000  vigintillinillion       1E60003  10^60003
=====  ======================  =======  ========


      One Millinillion to One Centillinillion

======  ======================  ========  =========
I(n)    Suffix                  E(#)      Powers
======  ======================  ========  =========
  1000  millinillion            1E3003    10^3003
 10000  decillinillion          1E30003   10^30003
 20000  vigintillinillion       1E60003   10^60003
 30000  trigintillinillion      1E90003   10^90003
 40000  quadragintillinillion   1E120003  10^120003
 50000  quinquagintillinillion  1E150003  10^150003
 60000  sexagintillinillion     1E180003  10^180003
 70000  septuagintillinillion   1E210003  10^210003
 80000  octogintillinillion     1E240003  10^240003
 90000  nonagintillinillion     1E270003  10^270003
100000  centillinillion         1E300003  10^300003
======  ======================  ========  =========


       One Millinillion to One Millidinillion

======  ======================  =========  ==========
I(n)    Suffix                  E(#)       Powers
======  ======================  =========  ==========
1000    millinillion            1E3003     10^3003
100000  centillinillion         1E300003   10^300003
200000  ducentillinillion       1E600003   10^600003
300000  trecentillinillion      1E900003   10^900003
400000  quadringentillinillion  1E1200003  10^1200003
500000  quingentillinillion     1E1500003  10^1500003
600000  sescentillinillion      1E1800003  10^1800003
700000  septingentillinillion   1E2100003  10^2100003
800000  octingentillinillion    1E2400003  10^2400003
900000  nongentillinillion      1E2700003  10^2700003
10^6    millidinillion          1E3000003  10^3000003
======  ======================  =========  ==========


             One Millinillion to One Millicosnillion

=====  =======================  ==============  ================
I(n)   Suffix                   E(#)            Powers
=====  =======================  ==============  ================
1000   millinillion             1E3003          10^3003
10^6   millidinillion           1E3000003       10^3000003
10^9   millitrianillion         1E3000000003    10^3000000003
10^12  millitetranillion        1E303#2         10^^2^303
10^15  millipentanillion        1E300003#2      10^^2^300003
10^18  millihexanillion         1E300000003#2   10^^2^300000003
10^21  milliheptanillion        1E33#3          10^^3^33
10^24  millioctanillion         1E30003#3       10^^3^30003
10^27  millienneanillion        1E30000003#3    10^^3^30000003
10^30  millideknillion          1E6#4           10^^4^6
10^33  milliundeknillion        1E3003#4        10^^4^3003
10^36  millidodeknillion        1E3000003#4     10^^4^3000003
10^39  millitriskaideknillion   1E3000000003#4  10^^4^3000000003
10^42  millitetrakaideknillion  1E303#5         10^^5^303
10^45  millipentakaideknillion  1E300003#5      10^^5^300003
10^48  millihexakaideknillion   1E300000003#5   10^^5^300000003
10^51  milliheptakaideknillion  1E33#6          10^^6^33
10^54  millioctakaideknillion   1E30003#6       10^^6^30003
10^57  millienneakaideknillion  1E30000003#6    10^^6^30000003
10^60  millicosnillion          1E6#7           10^^7^6
=====  =======================  ==============  ================


   One Millinillion to One Millihectnillion

======  =====================  ======  ========
I(n)    Suffix                 E(#)    Powers
======  =====================  ======  ========
1000    millinillion           1E3003  10^3003
10^30   millideknillion        1E6#4   10^^4^6
10^60   millicosnillion        1E6#7   10^^7^6
10^90   millitricontnillion    1E6#10  10^^10^6
10^120  millitetracontnillion  1E6#13  10^^13^6
10^150  millipentacontnillion  1E6#16  10^^16^6
10^180  millihexacontnillion   1E6#19  10^^19^6
10^210  milliheptacontnillion  1E6#22  10^^22^6
10^240  millioctacontnillion   1E6#25  10^^25^6
10^270  millienneacontnillion  1E6#28  10^^28^6
10^300  millihectnillion       1E6#31  10^^31^6
======  =====================  ======  ========


     One Millinillion to One Millikillonillion

=======  =====================  =======  =========
I(n)     Suffix                 E(#)     Powers
=======  =====================  =======  =========
1000     millinillion           1E3003   10^3003
10^300   millihectnillion       1E6#31   10^^31^6
10^600   millidihectnillion     1E6#61   10^^61^6
10^900   millitrihectnillion    1E6#91   10^^91^6
10^1200  millitetrahectnillion  1E6#121  10^^121^6
10^1500  millipentahectnillion  1E6#151  10^^151^6
10^1800  millihexahectnillion   1E6#181  10^^181^6
10^2100  milliheptahectnillion  1E6#211  10^^211^6
10^2400  millioctahectnillion   1E6#241  10^^241^6
10^2700  millienneahectnillion  1E6#271  10^^271^6
10^3000  millikillonillion      1E6#301  10^^301^6
=======  =====================  =======  =========


         One Millikillonillion to One Milliquettanillion

=======  ==================  ================  ==================
I(n)     Suffix              E(#)              Powers
=======  ==================  ================  ==================
10^3000  millikillonillion   1E6#301           10^^301^6
10^3M    millimeganillion    1E6#3001          10^^3001^6
10^3G    milligiganillion    1E6#30001         10^^30001^6
10^3T    milliteranillion    1E6#300001        10^^300001^6
10^3P    millipetanillion    1E6#3000001       10^^3000001^6
10^3E    milliexanillion     1E6#30000001      10^^30000001^6
10^3Z    millizettanillion   1E6#300000001     10^^300000001^6
10^3Y    milliyottanillion   1E6#3000000001    10^^3000000001^6
10^3R    millironnanillion   1E6#30000000001   10^^30000000001^6
10^3Q    milliquettanillion  1E6#(3(10^10)+1)  10^^(3(10^10)+1)^6


-Going Even Further Beyond-

In the source code of my parser (greekifier.py) I have taken the
liberty of calling the square of yotta "alpha"; the square of alpha is beta; followed by gamma, then delta, and the rest, including omega.

Since yotta = 10^24, alpha = 10^48. There are 24 greek letters.

This gives milliomeganillion = I(10^(24 * 2^24)) = I(10^402653184)
or 10^(3(10^402653184) + 3) or 1+e(3(10^402653184) + 3)

Why yotta? "yottayotta" is the largest square metric prefixes produce. "ronnaronna", or "quettaquetta" get swallowed by a long string of yottas at large values, hence "yottayotta" becomes "alpha"

Without this change, metric prefixes result in this progression as numbers go up: killo -> mega -> tera -> yotta -> yottayotta -> yottayottayottayotta -> exponentially growing yottas

"greekifier.py" can be independently tested to demonstrate the above.


On a final note, exhausting the Greek alphabet leaves omega to grow exponentially. In these cases, rather than finding (appropriating) another alphabet, for truncation, I would prefer that this naming convention be recursively applied to itself. Such that milliomegaomeganillion becomes "millidiomeganillion"

To prevent confusion ("Is 'omega' or 'omeganilli' repeated?") the "peiron" (from apeirogon) suffix can replace the final vowel of omega. This yields "millidiomegapeironillion"

However, this ultimately produces "milliomegaomegpeironillion" and even "milliomegaomegaomegpeironillion". The former is tolerable, but the latter is not because it would nessecarily follow "millidiomegaomegpeironillion" which cannot be repeated. (Perhaps "bi" could be used instead, but... really? That's mean.)

Perhaps "milliomegaomegaomegapeironillion" could instead be renamed
"alphillion". alphillion * 1000 is bialphillion, which is not to be confused with dialphillion; 

Picture this table filled out:
million
alphillion
betillion
...
omegillion
...
...
diomegillion
...
omegaomegillion
...
...
omegaomegpeironomegilliomegaomegpeironillion

I best stop here... I leave the pronunciation of this last number as an exercise for the reader... 

I could replace "omegaomegpeironomegilliomegaomegpeiron" with "kyoda", or "fish". Then, cycle through all the names again, concatenated to "kyoda" or "fish"

Then perhaps "conway", "wechsler", "ngu", "robert" for about 20 names adding our "bi"s and "di"s to even these...

If more are needed, just keep populating the list with whatever sounds nice, until a schema is developed even for this, to extend to  proportions of even greater amusement and bemusement.



-Sources-

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

Origin of "illion"
https://en.wiktionary.org/wiki/-illion#:~:text=Etymology,%2C%20and%20%2Dillion%20the%20stem.
