# csp_ai

This project involves solving a game using Constraint Satisfaction Problems (CSP) techniques, leveraging code from the [AIMA Python repository](https://github.com/aimacode/aima-python/tree/master). It was developed as part of the Artificial Intelligence course at the Technical University of Crete (TUC), under the guidance of Professor M. Lagoudakis.

## Game Description

The game is called Unruly, and it can be found [here](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/unruly.h). The objective is to solve the game using CSP-based methods by providing an input file with a specific format and obtaining the solved game as output.

## Input Format

The input is provided via a file and must follow this specific format:

```
8x8:bceadEDgCcAgCcabBi
```

- The `8x8` specifies the dimensions of the board (8 rows by 8 columns).
- The following string represents the initial state of the board in a compact notation.

## Output Format

The output of the program will be a solved game in the following format:


```
8x8:AaAaaAAaAaaAAaaAaAaAaaAAAaAaAAaaaAaAaAAaaaAAaaAAAAaaAaaAaAAaAAaaa
```

- The `8x8` again specifies the dimensions of the board.
- The string represents the final, solved state of the board.

  ## Acknowledgments

- **Professor M. Lagoudakis** for teaching the course and providing guidance.
- **AIMA Python Repository** for the foundational CSP code.
- **Simon Tatham** for the [Unruly game](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/unruly.h).
