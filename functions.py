import os
import sys
import json
from colors import *

def error(text):
    print("[" + lred + "Error" + white + "] " + text)

def info(text):
    print("[" + lblue + "Info" + white + "] " + text)

def create_gcode_file(name: str, code: str):
    """
    Genereate the g-code file.
    """
    with open(name, "w") as f:
        f.write(code)

def load(file: str, mode="r"):
    """
    Load a file and return the file content
    """
    return open(file, mode).read()

def merge(a, b):
    """
    Merge two dict into one.
    """
    r = a.copy()
    r.update(b)
    return r

def load_commands(file):
    """
    Load commands json file.
    """
    return json.load(open(file, "r"))

def validate_gcode(gcode):
    """
    Validate the g-code output.
    """
    gcode = gcode.split("\n")
    nline = 1
    for i in gcode:
        if i == " ":
            continue
        if not i.startswith(("G", "M", "X", "Y", "Z")):
            error(f"Invalid token at line {lgreen}{nline}{white} " + lcyan + i.replace(";", "").__repr__() + white + ".")
            sys.exit(1)
        nline += 1

def convert_to_gcode(code: str, tokens: dict, enable_comments=False, comments: str="comments.json"):
    """
    Convert gcg source to g-code source file.
    """

    gcode = ""

    if enable_comments:
        if not os.path.exists(comments):
            error("Comments file not exists.")
            sys.exit(1)
        comments = json.load(open(comments, "r"))

    # Replace the tokens from the commands file.
    tokens = list(tokens.items())
    for i in range(len(tokens)):
        old = tokens[i][0]
        new = tokens[i][1]
        code = code.replace(old, new)
    gcode = ""

    # Add comments
    if enable_comments:
        for line in code.split("\n"):
            inst = line.split(" ", 1)[0]
            args = line.split(" ", 1)[1]
            gcode += line + generate_comment(inst, comments, args)
    else:
        gcode = code

    gcode = gcode[:-1]
    validate_gcode(gcode)
    return gcode

def generate_comment(inst: str, comments: dict, args: list):
    """
    Generate comment after the instruction.
    """
    if inst not in comments:
        return "\n"
    return "; " + comments[inst] + " " + str(args).replace("[", "").replace("]", "") + "\n"

if __name__ == "__main__":

    # Load commands.
    tokens = load_commands("commands.json")

    # Load source code.
    code = load("test.gc")
    # Convert source code to g-code
    gcode = convert_to_gcode(code, tokens)

    print(gcode)