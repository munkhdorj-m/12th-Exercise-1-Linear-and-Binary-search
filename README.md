# Linear Search and Binary Search


PDF: https://drive.google.com/file/d/14bB72Mvr2QaOCf2f6r3CLbhEHWTM7GuC/view?usp=sharing

**Rules for this assignment**

- Write every search yourself. Do **not** use `in`, `.index()`, `.count()`, `list.sort()`, or the `bisect` module.
- Exercises 1 and 2 use **linear search**.
- Exercises 3, 4 and 5 use **binary search**. The input list is already sorted.
- Exercises 4 and 5 are also tested for **speed** — a linear scan will fail those tests even if the answer is correct.
- When an exercise returns two values, return them **in a list**, like `[3, 1]`.

---

## Exercise 1

**Problem:**
Search the list and return a list of **every** index where `target` appears, in order.
Return an empty list if the target is not in the list.

**Example:**

    Example Input:
        data   = [4, 2, 4, 9, 4]
        target = 4

    Program Output:
        [0, 2, 4]

    Example Input:
        data   = [10, 20, 30]
        target = 99

    Program Output:
        []

---

## Exercise 2

**Problem:**

`records` is a list of student records. Each record is a list `[id, name, score]`.
The list is **not sorted**, so you must use linear search.
Return the **name** of the student with that id, or `None` if no student has it.

**Example:**

    Example Input:
        records = [
            [101, "Bat", 78],
            [205, "Saraa", 91],
            [144, "Tuguldur", 65],
            [317, "Anu", 88],
        ]
        student_id = 144

    Program Output:
        "Tuguldur"

    Example Input:
        student_id = 999

    Program Output:
        None

---

## Exercise 3

**Problem:**

`data` is a **sorted** list. Do a binary search and return a list `[index, steps]`:

- `index` — the index where `target` was found, or `-1` if it is not there.
- `steps` — how many times you looked at a middle element.

**Example:**

    Example Input:
        data   = [1, 3, 5, 7, 9, 11, 13, 15]
        target = 7

    Program Output:
        [3, 1]      # found immediately at the middle

    Example Input:
        data   = [1, 3, 5, 7, 9, 11, 13, 15]
        target = 15

    Program Output:
        [7, 4]

    Example Input:
        data   = [1, 3, 5, 7, 9, 11, 13, 15]
        target = 8

    Program Output:
        [-1, 3]     # not found, but it still took 3 steps to prove it

---

## Exercise 4

**Problem:**

`data` is a **sorted** list. Return the index where `value` should be inserted so the
list stays sorted. If `value` is already in the list, return the position of the
**first** (leftmost) copy.

The answer is always between `0` and `len(data)`.

**Example:**

    Example Input:
        data  = [10, 20, 30, 40]
        value = 25

    Program Output:
        2           # [10, 20, 25, 30, 40]

    Example Input:
        data  = [10, 20, 30, 40]
        value = 50

    Program Output:
        4           # goes on the end

    Example Input:
        data  = [1, 2, 2, 2, 3]
        value = 2

    Program Output:
        1           # leftmost 2

---

## Exercise 5

**Problem:**

`data` is a **sorted** list that may contain repeated values.
Return a list `[first, last]` — the index of the first and the last occurrence of
`target`. Return `[-1, -1]` if the target is not in the list.

Hint: run binary search twice — once looking for the leftmost match, once for the rightmost.

**Example:**

    Example Input:
        data   = [1, 2, 2, 2, 3, 4]
        target = 2

    Program Output:
        [1, 3]

    Example Input:
        data   = [5, 5, 5, 5]
        target = 5

    Program Output:
        [0, 3]

    Example Input:
        data   = [1, 2, 3]
        target = 4

    Program Output:
        [-1, -1]

---

## Exercise 6 (Optional)

**Problem:**

Number Guessing Game — but the **computer** guesses.

- You think of a secret number from 1 to 1000. Do not tell the program.
- The program guesses a number. You answer `h` (too high), `l` (too low) or `c` (correct).
- The program must use binary search, so it always wins in at most 10 guesses.
- If your answers are contradictory (no number is left to guess), the program must say you cheated.
- Save each game to `guess_log.txt`: the secret number found, and how many guesses it took.

**Example**

    I will guess your number between 1 and 1000!
    Answer with h (too high), l (too low) or c (correct).

    Guess 1: Is it 500? l
    Guess 2: Is it 750? h
    Guess 3: Is it 625? l
    ...
    Guess 9: Is it 673? c

    Got it in 9 guesses!
    Result saved to guess_log.txt

    Example 2:
    Guess 1: Is it 500? h
    Guess 2: Is it 250? l
    Guess 3: Is it 375? h
    ...
    You are cheating! No number fits your answers.

---
