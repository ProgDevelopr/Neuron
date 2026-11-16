<center>
<img src="logo.png" alt="Logo" width="110" height="110">

# NEURON ESOTERIC PROGRAMMING LANGUAGE
</center>

`>`  Move the pointer to the cell on the right.

`<`  Move the pointer to the cell on the left.

`+`  Add 1 to the cell that the pointer is on.

`*`  Add 5 to the cell that the pointer is on.

`-`  Subtract 1 from the cell that the pointer is on.

`#`  Subtract 5 from the cell that the pointer is on.

`!`  Set the current cell to 0.

`=`  Copy the current cell's value to the one on its right.

`|`  Set the current cell to its absolute value.

`,`  Ask an integer input from the user and keep the value in the current cell.

`@`  Ask a character input from the user and store it in the current cell as its ASCII number.

`?`  Pause until the user has entered ENTER. It also does nothing when it hits EOF.

`.`  Print the cell's value as is.

`:`  Print the number as a character corresponding to ASCII. (Ex: 65 -> A)

`\`  Newline.

`&`  Print current index.

`_`  Print a space.

`"content"`  It's a comment. The text between these quotes is a comment.

`[`  If the current cell isn't 0, continue until "]", if it is 0, go past "]".

`]`  If the current cell isn't 0, go back to "[", if it is 0, do nothing.

`;`  Repeat the program forever, tape is preserved.

## Note
- Any alphanumeric character mentioned in a neuron file will be printed.

- Any unrecognised punctuation or symbol is ignored as BrainF**k wanted.

- There are 500 cells (all 0) in a default tape if the user doesn't enter --tape CLI argument.

- Neuron files must have the extension, `".n"`.