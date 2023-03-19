# POCII
 
This is my final work for the computer science course. The idea of this project is to create a database with histograms from differents binary files of the same program (but compiled with different optimizations), so they can be used to train a malware detector.

## Running

To execute this program, you first need to set up the Jotai Benchmarks and the CFGgrind enviroments in this same folder.

Step 1: Clone this project
Step 2: Clone [Jotai Benchmarks](https://github.com/lac-dcc/jotai-benchmarks/)
Step 3: Build [CFGgrind](https://github.com/rimsa/CFGgrind) following its Readme instructions

So you have this final structure:

POCII
├── README.md
├── jotai-benchmarks
│   ├── LICENSE.md
│   ├── README.md
│   ├── assets
│   ├── benchmarks
    ...
├── valgrind-3.20.0
│   ├── .in_place
│   ├── autom4te.cache
│   ├── auxprogs
│   ├── cachegrind
    ...
