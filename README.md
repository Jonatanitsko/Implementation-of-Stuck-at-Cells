# Implementation-of-Stuck-at-Cells
The main.py file contains the encoder/decoder code for the stuck-at cells problem.

The folder currently includes an example for a channel which can receive messages of length 4.

There is a parity checking matrix attached (Parity checking matrix.csv) and an input file (Encoding input file.csv) containing the wanted message for encoding along with the indices of the stuck cells and their values.
To use the code scheme:
  1.Attach the desired parity checking matrix in an excel file format, with the name of: "Parity checking matrix". There is an example pcm attached to this folder.
  2.Attach the wanted message for encoding along with the indices of the stuck cells and their values. In the file named "Encoding input file"(also an excel file). 
  3.Run the python file, and input messages in the following format:
    a. To start, enter "e" to encode a message to the memory. 
    b. To receive a message that was saved to the memory, enter the decoder by passing "d" to the input line.

