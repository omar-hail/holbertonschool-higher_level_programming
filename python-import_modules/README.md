# Python - Import & Modules

This folder contains solutions to tasks related to Python modules, importing, command-line arguments, and working with compiled files. Each script follows Holberton School requirements and uses safe importing (no `*` or `__import__` unless specified).

---

## 🐍 0. Import a Simple Add Function — `0-add.py`
Imports the `add(a, b)` function from `add_0.py`, assigns `a = 1` and `b = 2`, and prints the result using formatted output.

**Usage:**

./0-add.py
1 + 2 = 3

---

## 🧮 1. Calculator Functions — `1-calculation.py`
Imports functions (`add`, `sub`, `mul`, `div`) from `calculator_1.py`, assigns `a = 10` and `b = 5`, and prints the math results.

**Usage:**

./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2

---

## 📝 2. Print Arguments — `2-args.py`
Prints the number of arguments and lists each one with its index.

**Usage:**

./2-args.py
0 arguments.

./2-args.py Hello
1 argument:
1: Hello

./2-args.py Hello World School
3 arguments:
1: Hello
2: World
3: School

---

## ➕ 3. Infinite Addition — `3-infinite_add.py`
Adds all integer arguments passed to the script and prints the total. Supports big integers.

**Usage:**

./3-infinite_add.py 10 20 30
60

---

## 🔎 4. Discover Hidden Names — `4-hidden_discovery.py`
Located in `/tmp/` during execution.  
Imports the compiled module `hidden_4.pyc` and prints all names that **do not** start with `__`, sorted alphabetically.

**Usage (inside /tmp):**

curl -Lso "hidden_4.pyc" "https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc
"
./4-hidden_discovery.py

Example output:
my_secret_santa
print_hidden
print_school

---

## 📦 5. Load Variable — `5-variable_load.py`
Imports the variable `a` from `variable_load_5.py` and prints its value.

**Usage:**

./5-variable_load.py
98

---
