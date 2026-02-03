Names:
- Antony
- Youssof
- Jad
- Mubashir Shehun
- Rebecca 


-- Project Goals --

The main goal of this project is to create a program that can encode a user input into a cipher with at least three different methods of encoding. It's as simple as writing up and inputting whatever you wish to encode and then choosing what method of encryption you want to use. 

The methods (for now) are going to be encryption through: converting the input to morse code (dots and dashes), encoding the input using a caesar cipher (shifting the letters up or down using a specific number as our key), and finally encoding the input using a Vignère cipher (similar to a caesar cipher, but uses a code word. Each letter in the key word is a number on the alphabet. You shift the letters in the word you are encoding by the value of each letter in the key word).

This project could be helpful as a gateway for a computer science student or beginner programmer who wants to learn and experiment with basic encryption methods.

The target user for this sort of project would have one primary user, that being the individual encoding and decoding the plaintext.

In terms of a general plan for the actual project right now, the goal is to have all major ciphers done by the end of February at the latest (first week being focused on the Caesar cipher, next being Morse code, and the final one being the Vignère cipher), and then by early March start development on the web application portion of the project encompassing the actual user interface that allows the user to press buttons to encode something while also storing the key used for the encryption along with the resulting code into a separate area for the user to refer back to.

For right now, that is the basic goal of the project. It's set up to potentially involve more methods of encryption, but the primary goal is to just have the three listed ciphers as well as a section that allows the user to recall old ciphers and their keys


-- Current Setup --

To run the project currently, you will need the latest version of Python installed. As it stands right now, there is no web application yet. There is a choppy iteration of the Caesar cipher code set up that can be run in a terminal, but it is much easier to run in an IDE.
Once the program runs, it will ask whether or not you wish to encode or decode something. If you do not already have encoded text, then the user is advised to type "encode". It will then ask you for a shift value, to which the user should respond with a single integer value. Once that is done, the program should then go through the cipher and return an encoded piece of text, ending the interaction with a question of whether or not the user wishes to encode/decode something else. If the answer is anything but "yes", the process will end.

-- Team Norms --

For right now, as each member has relatively different schedules that can prove to be inflexible, the goal is to meet at least once a week outside of class through a call to knock off any major bullet points or concerns. Our channels of communication would likely constitute a general group chat that is periodically checked throughout the hours one can work. With decisions, it makes more sense to go with a majority rule just to keep things moving along smoothly. 

As there is an odd number of group members, it is unlikely for there to be any major need for a tiebreaker unless one or more people are neutral with a specific decision. At that point, the dissenting parties can rationalize a decision. If both parties are steadfast, then we can rely on a coinflip as a last resort.
