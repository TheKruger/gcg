# GCG
The GCG is tool to convert gcg files to g-code files.

# GCG files
The gcg files extension is the `.gc` and you can convert these files to gcode files (`.nc`).
If you give the input file with with other extension the compiler will not warn you. The file extension is only stand for to organizing the files.

# Requirements
- python 3.x

# Setup
Run `pip install -r requirements.txt` to install the dependencies.

# Load your own commands
You can load your own commmands with the `-c` flag, for example `gcg.py -f mygcgfile.gc -c mycommands.json, othercommands.json`.
When you load the commands then it will be automatically merged to the default commands.

# Comments
If you use the `-C` or `--comments` then you can add commands after the g-code instructions.

# Contributing
The contributions are welcomed. This project is diffucult for me because I don't know how the g-code works.
So if you known how the g-code works and the g-code instructions then I will thank if you help me out.
Because I only know a little about the g-code and I collected all the informations from the internet and I hope these informations are good.
And of course python developer are welcomed too.