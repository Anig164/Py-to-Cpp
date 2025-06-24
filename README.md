# Python to C++ Transpiler

A custom-built transpiler that converts a subset of Python code into equivalent C++ code. Designed using compiler design principles including lexical analysis, parsing, semantic analysis, and code generation.

## 🚀 Features

- Full lexical analysis using PLY (Python Lex-Yacc)
- Parser with grammar rules for assignments, loops, conditionals, and expressions
- Abstract Syntax Tree (AST) generation
- Semantic analysis with basic type inference
- C++ code generation with block-based formatting using braces
- Modular architecture: preprocessing → lexer → parser → semantic analyzer → code generator

## 🛠️ Technologies Used

- Python 3.x
- [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/)
- Custom classes for AST and code generation

## 📁 Project Structure
├── preprocessor.py       # Handles indentation → braces transformation
├── lexer.py              # Tokenizer built with PLY
├── parser.py             # Grammar rules and AST builder
├── semantic_analyzer.py  # Type checks and validations
├── code_generator.py     # C++ code generation from AST
├── main.py               # Entry point that runs all modules
├── sample_input.py       # Sample Python code to transpile
└── output.cpp            # Generated C++ code

 Limitations
	•	Currently supports only a subset of Python syntax
	•	No function or class translation yet (WIP)
