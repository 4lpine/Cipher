# Alcipher Encryption Tool

This is a custom encryption tool that allows you to encode and decode text files using a custom key. The tool provides options to specify the input file, the key file, the key strength, and the output directory.

## Prerequisites

Just python 3 | All modules used are apart of the standard library


Usage : 
  - Encoding : 
    - To encode a file "input.txt" with a specified key strength (let's say 12) and save the output to a folder which contains the output and the key, use the following command:
      - ```python alcipher.py encode --input input.txt --strength 12 --output output_dir```
        
    
    - To use a specific key in for encoding the input.txt file and save the encoded output to a directory named output_dir, use the following command:
        - ```python alcipher.py encode --input input.txt --key key.txt --output output_dir```

        
  - Decoding
    - To decode a file encoded_output.txt using the key from key.txt and save the decoded output to a directory named output_dir, use the following command:
      - ```python alcipher.py decode --input encoded_output.txt --key key.txt --output output_dir```

Notes : 
  - The --output argument is optional and alcipher will print all the information to the commandline if it isn't given or if the output argument is "screen".
  - Alcipher saves encoded output into a folder which contains the output and the key, and saves decoded output into a file
  - The strength argument multiplies the length of the input by a factor of itself. For example if an input is given with strength 10 the output will be 10 times longer than the input. Using this information be weary about using too much strength, it may hinder the efficiency

How it works : 
  - **Alcipher pairs the standard ascii codes with random ones and even allows for multiple ascii codes to be paired with one ascii code hence the "strength" argument to randomize a given input in such a way that it's almost impossible to crack without the key.**
