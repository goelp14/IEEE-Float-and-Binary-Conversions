# IEEE-Float-and-Binary-Conversions

_This program is designed to not only convert from the IEEE Float 754 standard to a Binary String and vice versa, but also display all the work along with it. The intent is to speed up the process when trying to complete these conversions and the work must be shown. I hope this can make lives easier in some way or another_

##Usage
You can access the features of this program by adding arguments when you run it from terminal or by simply running the program and following the built in steps.

###Float to Binary
####Terminal
To use the Terminal follow this format:
```bash
python <path/to/script> -ftb <insert float here>
```
####From Program
The Program will prompt you to type either a "0" or a "1" depending on if you want to convert from float to binary or binary to float. Simply type in the number corresponding to the option you want and follow the displayed instructions.

###Binary to Float
####Terminal
To use the Terminal follow this format:
```bash
python <path/to/script> -btf <insert binary string here>
```
Note that you must place the binary string in "" if there are spaces in your binary string as the code would read them as seperate arguments. This way it is read as one string which is then converted into a binary string with no spaces.

####From Program
Same as with Float to Binary.

##Extra Info

I have many safeties put in place so if the program closes with an exit message, do not be alarmed. You likely put something in that the code can't work with. Simply fix that and run the code again.

To see the help manual simply run the program but with the option **-h**.

If you find any bugs please notify me.


