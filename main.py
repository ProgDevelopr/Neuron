"""Intrepeter for the Neuron esoteric programming language."""

from sys import exit as e
from argparse import ArgumentParser
from os.path import exists

def error_message(msg):
    print(f"\n[ERROR] {msg}")
    e(1)

def find_brackets(code):
    stack, table = [], {}
    for i,c in enumerate(code):
        if c == "[":
            stack.append(i)
        elif c == "]":
            if not stack:
                error_message(f"Character \"]\" found without match at index {i}.")
            j = stack.pop(-1)
            table[i] = j
            table[j] = i
    if stack:
        error_message(f"Character \"[\" found without match at index/indices {', '.join(map(str, stack))}.")
    return table

def find_quotes(code):
    idx, table = -1, {}
    for i,c in enumerate(code):
        if c == "\"":
            if idx == -1:
                idx = i
            else:
                j, idx = idx, -1
                table[j] = i
    if idx != -1:
        error_message(f"Unmatched quote at index {idx}.")
    return table

arithmetic = {
    "+": 1,
    "-": -1,
    "*": 5,
    "#": -5
}

def run(code: str, size_t=500):
    tape = [0] * size_t
    idx = size_t // 2
    pc = 0
    bracket_table = find_brackets(code)
    quote_table = find_quotes(code)

    try:
        while pc < len(code):
            c = code[pc]

            if c == ">":
                idx += 1
                if idx >= size_t:
                    error_message(f"Current index is above tape size ({size_t}).")

            elif c == "<":
                idx -= 1
                if idx < 0:
                    error_message(f"Current index is below 0.")

            elif c in arithmetic:
                tape[idx] += arithmetic[c]

            elif c == ",":
                inp = 0
                try:
                    inp = input(":")
                    tape[idx] = int(inp)
                except EOFError:
                    error_message("EOF when reading a line. You should use interactive inputs only.")
                except ValueError:
                    error_message(f"An invalid integer \"{inp}\" was entered.")

            elif c == "@":
                inp = ""
                try:
                    inp = input(">")
                    if len(inp) > 1:
                        error_message("The input given to \"@\" should be one character long.")
                    if inp:
                        tape[idx] = ord(inp[0])
                    else:
                        error_message("Please enter one character for \"@\".")
                except EOFError:
                    error_message("EOF when reading a line. You should use interactive inputs only.")

            elif c == "?":
                try:
                    input()
                except EOFError:
                    pass

            elif c == ".":
                print(tape[idx], end="")

            elif c == ":":
                print(chr(tape[idx]), end="")

            elif c == "\\":
                print()

            elif c == "_":
                print(end=" ")

            elif c == "&":
                print(idx, end="")

            elif c == "!":
                tape[idx] = 0

            elif c == "=":
                if idx + 1 >= size_t:
                    error_message(f"Cannot copy to {idx+1} because it's outside the tape (size: {size_t}).")
                tape[idx+1] = tape[idx]

            elif c == "|":
                tape[idx] = abs(tape[idx])

            elif c == "\"":
                pc = quote_table[pc]

            elif c == "[":
                if tape[idx] == 0:
                    pc = bracket_table[pc]

            elif c== "]":
                if tape[idx] != 0:
                    pc = bracket_table[pc]

            elif c == ";":
                pc = 0
                continue

            if c.isalnum():
                print(c,end="")

            pc += 1
    except KeyboardInterrupt:
        e(1)

parser = ArgumentParser("Neuron: a BF dialect for the modern world.")
parser.add_argument("file", type=str)
parser.add_argument("--tape", type=int, required=False)
args = parser.parse_args()

if not exists(args.file):
    error_message(f"File \"{args.file}\" not found.")

if args.file.split(".")[-1].lower() != "n":
    error_message(f"File extension must be \".n\".")

with open(args.file, "r", encoding="utf-8") as f:
    content = "".join(x.strip().replace(" ","") for x in f.readlines())
if args.tape:
    run(content, args.tape)
else:
    run(content)
