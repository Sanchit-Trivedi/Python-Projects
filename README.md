# Python-Projects

Course Assignments Completed using Python at IIIT Delhi

## Folder Structure  

```
├── Assembler
│   ├── Assembler.pdf
│   ├── Assembler.py
│   ├── input.txt
│   └── input_Assembled
│       ├── MachineCode.txt
│       ├── OPCodeTable.txt
│       └── SymbolTable.txt
├── Betweeness Centrality
│   └── SBC_2018091.py
├── K-Map-Solver
│   ├── HW2_2018091.py
│   └── HW2_testing_2018091.py
├── Linear Transformations
│   └── Transformations_2D.py
├── README.md
└── Weather API
    ├── CSE101_HW1.pdf
    ├── a1.py
    └── a1test.py
```

## Assembler :gear:

A Two Pass Assembler that converts assembly language code into 12-bit machine code. The first 4 bits are reserved for Opcode and remaining 8 bits reserved for Memory. Empty lines are ignored while reading the file and Comments are parsed and collected separately. Memory is first allocated to instructions and then to variables.

```
Number Of Opcodes : 12 
Memory Limit : 256
```

### Syntax Rules

- Empty lines & whitespaces are allowed in code and Tokens should be separated by spaces.
- It is mandatory for a label to start with an alphabet and end with “:”.
- Variable should start with an alphabet.
- Use `//` to write a comment. Note that `//` can’t appear in comment body or in code.

### Errors   

- **Memory Limit Exceeded:** The number of instructions and variables exceed 255.
- **Unable To Resolve Stop:** The assembly code should have exactly one stop and should appear at the end of the code. Any other occurrence of STP is treated as an error.
- **Invalid Comment Declaration:** The comments are not declared as per syntax given.
- **Invalid Opcode/Label:** The assembler detected an invalid Opcode or Label.
- **Invalid Label/Variable Declaration:** The variable or label was not declared as per the syntax provided.
- **Can't Resolve Label L:** A branch instruction with L appeared in the code but no such Label was declared as a marker.

**Collaborator:** [Pruthwiraj Nanda](https://github.com/pruthwi07) 

## Betweenness Centrality :part_alternation_mark:
Betweenness Centrality is a measure of centrality in a graph based on shortest paths. For every pair of vertices in a connected graph, there exists a shortest path such that either the number of edges that the path passes through or the sum of the weights of the edges is minimized. The betweenness centrality for each vertex is the number of these shortest paths that pass through the vertex. The python code calculates the Standardised Betweenness Centrality and prints top K nodes ordered by Standardised Betweenness Centrality.

## Geometric Transformations :o:

Supports Rotate, Scale and Translate operations on Disc and Polygon.

## K-Map Solver :pencil2:

The Karnaugh Map or K-Map is a method of simplifying Boolean algebra expressions.The cells in the K-Map are ordered using the Gray Code. K-Map can be created using either SOP (sum of products) or POS (product of sums).

Implemented Quine-McCluskey and Petrick methods to solve a `4 x 4` K-Map.

**Sample Input**
```
No. of variables: 4
Function: (1,3,7,11,15) d (0,2,5) 
```
**Sample Output**
```
Simplified expression: yz+w’x’ OR yz+w’z
```

## Weather :sun_behind_small_cloud:
The module takes the location , n (For nth day from today) and time as input from the user and displays
appropiate weather information extracted from a JSON response given by a weather data website.
The concept of string slicing is used to extract required data.