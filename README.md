<!---Elizabeth Yam ey92-->
# Latin/Russian Literal Translator
## CS 4744/Ling 4244 Computational Linguistics Final Project (~1mo)
### Elizabeth Yam (ey92)
As my final project for this class, I am creating a program to translate between Latin and Russian via their morphology and phonology (Python 2.7.6). I chose these two languages because I have studied Latin for 5 years and Russian for about 2 years, and they have relatively similar grammatical structures (parallels in conjugating and declining).<br>

This translator was created to do a direct, word-for-word literal translation between Latin and Russian. <br>

It doesn't into account context or identify special phrasal constructions. It is only concerned with the indicative mood and active voice for verbs. Nouns are not declined into the locative case. Adjectives used substantively will not be detected as being used in such a way. Additionally, there are no adverbs, auxiliary verbs, modals, comparatives, or superlatives.<br>

[Roots.py](https://github.com/ey92/Lat-Rus_Translate/blob/master/Roots.py) has all of the words included in the translator's dictionary. It can attempt to conjugate verbs and decline nouns/adjectives when given the parameters needed, but cannot deconstruct (and therefore translate) words not already in the dictionary.<br>

[See what's included for Latin](https://github.com/ey92/Lat-Rus_Translate/blob/master/Latin.md)

[See what's included for Russian](https://github.com/ey92/Lat-Rus_Translate/blob/master/Russian.md)

[see Latin.py](https://github.com/ey92/Lat-Rus_Translate/blob/master/Latin.py)

[see Russian.py](https://github.com/ey92/Lat-Rus_Translate/blob/master/Russian.py)

## Using the UI
- Open the command line (Windows) or terminal (Mac/Linux) and navigate to where the project files are.
- Run `python runtest.py`
- Enter the number corresponding to the option you want to pick
- Enter the required parameters, separated by commas
	- **caveat**: The program is not very robust and may crash if you provide the wrong input here
- After the inflected word is produced, you are given a prompt: "Would you like to do more? (y/n/a)"
	- y(es) returns to the previous menu
	- n(o) quits the UI
	- a(gain) re-runs the same choice from the previous menu

### Translation Example
![UI Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/UIExample.png)

### Latin to Russian Examples
Translate Latin Verb to Russian Verb:<br>
![Latin to Russian Verb Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/LRverb.png)

Translate Latin Noun to Russian Noun:<br>
![Latin to Russian Noun Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/LRnoun.png)

### Russian to Latin Examples
Translate Russian Verb to Latin Verb:<br>
![Russian to Latin Verb Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/RLverb.png)

Translate Russian Noun to Latin Noun:<br>
![Russian to Latin Noun Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/RLnoun.png)


### Latin Examples
Construct Verb:<br>
![Latin Construct Verb Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/LatinConstructVerb.png)

Construct Noun:<br>
![Latin Construct Noun Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/LatinConstructNoun.png)

Construct Adjective:<br>
![Latin Construct Adjective Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/LatinConstructAdjective.png)

Deconstruct Verb:<br>
![Latin Deconstruct Verb Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/LatinDeconstructVerb.png)

Deconstruct Noun:<br>
![Latin Deconstruct Noun Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/LatinDeconstructNoun.png)

Deconstruct Adjective:<br>
![Latin Deconstruct Adjective Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/LatinDeconstructAdjective.png)


### Russian Examples

Construct Verb:<br>
![Russian Construct Verb Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/RussianConstructVerb.png)

Construct Noun:<br>
![Russian Construct Noun Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/RussianConstructNoun.png)

Construct Adjective:<br>
![Russian Construct Adjective Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/RussianConstructAdjective.png)

Deconstruct Verb:<br>
![Russian Deconstruct Verb Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/RussianDeconstructVerb.png)

Deconstruct Noun:<br>
![Russian Deconstruct Noun Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/RussianDeconstructNoun.png)

Deconstruct Adjective:<br>
![Russian Deconstruct Adjective Example](https://github.com/ey92/Lat-Rus_Translate/blob/master/pics/RussianDeconstructAdjective.png)