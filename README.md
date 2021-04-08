# Implementation-of-Stuck-at-Cells
The folder currently includes an example of a channel which can receive messages of length 4.

The main.py file contains the encoder/decoder code for the stuck-at cells problem.

There is a parity checking matrix attached along with the indices of the stuck cells and their values (Parity checking matrix.csv). An input file (Encoding input file.csv) containing the wanted message for encoding is also attached.
To use the coding scheme:
1.  Attach the desired parity checking matrix along with the indices of the stuck cells and their values as columns at the end of the matrix. In an excel file format, with the name of: "Parity checking matrix". There is an example pcm attached to this folder.
2.  Attach the wanted message for encoding in the file named "Encoding input file"(also an excel file).
3.  Run the python file, and input messages in the following format:
a.  To start, enter "e" to encode a message to the memory.
b.  To receive a message that was saved to the memory, enter the decoder by passing "d" to the input line.
c.   To end enter "exit"

