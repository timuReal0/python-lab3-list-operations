# Python Lab 3 – List Operations with a Console Menu

A menu-based console application that works with a list of integers.
Written for the third lab of an introductory programming course, focused on
functions, Python lists and building a simple console interface.

## Features

| Option | What it does |
|--------|--------------|
| `1` | Reads a list of integers, separated by spaces. |
| `2` | Finds and prints the longest sublist in which all elements have the same sum of digits. |
| `3` | Removes from the list every element whose sum of digits is even. |
| `P` | Prints the current list. |
| `E` | Exits the program. |

A sublist means a sequence of consecutive elements from the list.

## Code structure

Each feature is implemented in its own function:

- `Read` – reads the numbers from the keyboard and stores them in the list
- `DigitSum` – returns the sum of the digits of a number
- `subList` – finds the longest sublist with equal digit sums (option 2)
- `removeList` – removes the elements with an even digit sum (option 3)
- `PrintList` – prints the current list (option P)
- `Menu` – shows the menu and calls the function for the chosen option

## Example

For the list `12 21 30 4 11 7`, the digit sums are 3, 3, 3, 4, 2 and 7.

- Option `2` prints `[12, 21, 30]`, since all three have digit sum 3.
- Option `3` removes `4` and `11` (even digit sums), so option `P` then prints `[12, 21, 30, 7]`.

## How to run

Requires Python 3.

```
python app.py
```

Or open the file in IDLE and press **F5** (Run Module).
