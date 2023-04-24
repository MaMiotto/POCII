# POCII
 
This is my final work for the computer science course. The idea of this project is to create a database with histograms from differents binary files of the same program (but compiled with different optimizations), so they can be used to train a malware detector. 

## Structure

This project consist on several folders with the same amount of files in each one. Those files consist on the same program in different stages on the process of generating the histograms. The programs are from [Jotai Benchmarks](https://github.com/lac-dcc/jotai-benchmarks/), so I didn't create a folder for the code version. You can have it by cloning their github project. 

The next step is to compile all those files into executables. They are in the "binaries" folder. A sufix is added to the name of the file to represent the way it was compiled. So the "-regular" sufix means that no flags or any other modifier was used during compiling. On the other hand, the "-ollvm" sufix says that the obfuscator-llvm was used during compiling.

## Running

To execute this program, you first need to set up the Jotai Benchmarks and the CFGgrind enviroments in this same folder.

Step 1: Clone this project<br />
Step 2: Clone [Jotai Benchmarks](https://github.com/lac-dcc/jotai-benchmarks/)<br />
Step 3: Build [CFGgrind](https://github.com/rimsa/CFGgrind) following its Readme instructions<br /><br />

So you have this final structure:<br /><br />

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
