# Fast & Simple CLI Calculator

A lightweight, optimized command-line calculator written in Python. It evaluates basic arithmetic operations quickly and securely using dictionary dispatch.

---

## How It Works

1. **User Input:** You type an expression separated by spaces (for example: `12 * 4`).
2. **Splitting (Tokenizing):** The program splits the line into three pieces: the first number, the operator symbol, and the second number.
3. **Lookup Table (Dictionary Dispatch):** Instead of checking multiple `if/elif` conditions (`if op == '+': ... elif op == '-': ...`), the code uses a Python dictionary that maps each symbol (`+`, `-`, `*`, `/`) directly to its corresponding function from Python's built-in `operator` module.
4. **Execution & Safeguards:**
   - It checks whether the operator is valid.
   - It blocks division by zero before performing the math.
   - It runs the operation and returns the result.

---

## Complexity Analysis

### Time Complexity
- **Lookup & Calculation:** **$O(1)$ (Constant Time)**  
  Dictionary lookups in Python use hash tables, which find the correct operation instantly regardless of input size. Python's built-in `operator` functions are implemented directly in C, running at hardware speed.
- **Input Parsing:** **$O(L)$**, where $L$ is the number of characters in your input line (splitting a short 3-token string takes negligible time, effectively constant for regular numbers).

### Space Complexity
- **Memory Usage:** **$O(1)$ (Constant Space)**  
  The dictionary stores only four references to standard library functions. Memory consumption does not scale or grow across calculations.

---

## Getting Started

### Prerequisites
- Python 3.8+ (no third-party packages required)

### Running the Calculator
```bash
python calculator.py