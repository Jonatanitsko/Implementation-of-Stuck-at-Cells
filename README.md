# Implementation-of-Stuck-at-Cells
The main.py file contains the encoder/decoder code for the stuck-at cells problem.

The folder currently includes an example for a channel which can receive messages of length 4.

There is a parity checking matrix (pcm) attached and an input file for the indices of the stuck cells.

To use the code scheme:
Attach the desired parity checking matrix in an excel file format, with the name of: "Parity checking matrix". There is an example pcm attached to this folder.
Attach the indices of the stuck cells and the message in the file named "Encoding input file"(also an excel file).
Run the python file, and input messages in the following format:
To start enter "e" to encode a message to the memory.
To receive a message that was saved to the memory, enter the decoder by passing "d" to the input line and then enter the number of the message you would  like to retrieve.
