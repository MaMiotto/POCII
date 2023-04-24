# POCII
 
This is my final work for the computer science course. The idea of this project is to create a database with histograms from differents binary files of the same program (but compiled with different optimizations), so they can be used to train a malware detector. 

## Structure

This project consist on several folders with the same amount of files in each one. Those files consist on the same program in different stages on the process of generating the histograms. The programs are from [Jotai Benchmarks](https://github.com/lac-dcc/jotai-benchmarks/), so I didn't create a folder for the code version. You can have it by cloning their github project. 

The next step is to compile all those files into executables. They are in the "binaries" folder. A sufix is added to the name of the file to represent the way it was compiled. So the "-regular" sufix means that no flags or any other modifier was used during compiling. On the other hand, the "-ollvm" sufix says that the obfuscator-llvm was used during compiling.

Once you have all the binaries files, you can get the assembly instructions mapping for better CFG visualization. So using the cfggrind, we generate the .map files (on the "maps" folder), the .cfg files (on the "cfg" folder) and the .dot files (on the "dots" folder). 

## Running

If you don't want to simply download those files from this project, you can generate them yourself, as I did, using the Python scripts (on the "python scripts" folder). To do so, read the following steps:

To execute this program, you first need to set up the Jotai Benchmarks and the CFGgrind enviroments next to the python scripts folder.

Step 1: Download the "python scripts" folder <br />
Step 2: Clone [Jotai Benchmarks](https://github.com/lac-dcc/jotai-benchmarks/)<br />
Step 3: Build [CFGgrind](https://github.com/rimsa/CFGgrind) following its Readme instructions<br /><br />

So you have this final structure:<br /><br />

POCII <br />
├── README.md <br />
├── python scripts <br />
│   ├── fixingCodeBugs.py <br />
│   ├── histogramGenerator.py <br />
├── jotai-benchmarks <br />
│   ├── LICENSE.md <br />
│   ├── README.md <br />
│   ├── assets <br />
│   ├── benchmarks <br />
├── valgrind-3.20.0 <br />
│   ├── .in_place <br />
│   ├── autom4te.cache <br />
│   ├── auxprogs <br />
│   ├── cachegrind <br />
├── ...<br />

Step 4 (Optional): In order to compile all Jotai Benchmarks on windows, using the Windows Subsystem for Linux (WSL), I had a problem with its variable names (typedef redefinition error). So I made a script to change all those names. If you're facing a similar issue, just do this:

```
$> python3 fixingCodeBugs.py
```

Step 5: Run the histogram generator code, in order to generate all the binaries, cfg, map and dot files.

```
$> python3 fixingCodeBugs.py
```