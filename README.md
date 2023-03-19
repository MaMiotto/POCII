# POCII
 
This is my final work for the computer science course. The idea of this project is to create a database with histograms from differents binary files of the same program (but compiled with different optimizations), so they can be used to train a malware detector.

## Running

To execute this program, you first need to set up the Jotai Benchmarks and the CFGgrind enviroments in this same folder.

Step 1: Clone this project
Step 2: Clone [Jotai Benchmarks](https://github.com/lac-dcc/jotai-benchmarks/)
Step 3: Build [CFGgrind](https://github.com/rimsa/CFGgrind) following its Readme instructions

So you have this final structure:

POCII <br />
├── README.md <br />
├── jotai-benchmarks <br />
│   ├── LICENSE.md <br />
│   ├── README.md <br />
│   ├── assets <br />
│   ├── benchmarks <br />
    ... <br />
├── valgrind-3.20.0 <br />
│   ├── .in_place <br />
│   ├── autom4te.cache <br />
│   ├── auxprogs <br />
│   ├── cachegrind <br />
    ... <br />
├── .gitattributes <br />
├── .gitignore <br />
