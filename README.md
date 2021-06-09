# Hexdump in Python

This is the Python version of the standard Hex-dump (monitor style) program.

# Background

The code was developed, quickly, to solve an urgent issue at a client site. The 
program needed to examine a single file at a time and dump out both HEX and ASCII
representations of the contents.

The main limitations of the code are:

    1. It only works on a single file per execution
    2. It does not handle STDIN
    3. The file address is fixed to 6 HEX digits

It the context of the original problem, none of the above were considered issues
due to the immediate requriement for the program. 

This program has been superceeded by the Go version

# Usage

The prorgam has the following options:

```
./hexDump.py  -h
Usage: -f <file>

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  File to be dumped
  -n, --narrow          Narrow format (8-byte wide)
  -m, --medium          Normal format (16-byte wide)
  -w, --wide            Wide format (32-byte wide)
  -u, --ultra           Ultra-wide format (64-byte wide)
  ```

  The main options are around the width of the display (8, 16, 32 and 64 bytes wide).
