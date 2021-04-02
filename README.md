# Implementation-of-Stuck-at-Cells
The main.py file contains the encoder/decoder code for the stuck-at cells problem.

The folder currently includes an example for a channel which can receive messages of length 4.

There is a parity checking matrix (pcm) attached and an input file for the indices of the stuck cells.

To use the code scheme:
Attach the desired parity checking matrix in an excel file format, with the name of: "pcm". There is an example pcm attached to this folder.
Attach the indices of the stuck cells in the file named "input" (also an excel file).
Run the python file, and input messages in the following format:
To input a message to the memory, follow the instructions written on the screen, and enter "e" to encode a message to the memory.
Enter a message of length of 4, for a pcm with n=7, using the format: "xxxx", for example.
To receive a message that was saved to the memory, enter the decoder by passing "d" to the input line and then enter the number of the message you would  like to retrieve.

