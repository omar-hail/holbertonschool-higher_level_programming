# Python – Introductory Tasks (2-print.py → 9-easter_egg.py)

This mini-project contains the essential beginner Python scripts from `2-print.py` up to `9-easter_egg.py`.  
The tasks cover printing, f-strings, string multiplication, slicing, concatenation, and module importing.

All scripts are written for **Python 3** and respect `pycodestyle` requirements.

---

## 📂 Files & Descriptions

---

### **2-print.py**
Prints the exact text:

"Programming is like building a multilingual puzzle

Uses the `print` function and proper escaping.

---

### **3-print_number.py**
Prints an integer followed by the text `Battery street` using an **f-string**, without converting the number to a string.

**Example:**

98 Battery street

---

### **4-print_float.py**
Prints a float value with exactly **2 decimal places** using an f-string.

**Example:**

Float: 3.14

---

### **5-print_string.py**
Prints:

1. The string stored in `str`, repeated **3 times** (without loops).
2. The **first 9 characters** of the string.

**Example:**

Holberton SchoolHolberton SchoolHolberton School
Holberton

---

### **6-concat.py**
Concatenates the variables `str1` and `str2` to produce:

Welcome to Holberton School!

Without creating new variables beyond what's required.

---

### **7-edges.py**
Extracts specific parts of a string using slicing:

- `word_first_3`: first 3 letters  
- `word_last_2`: last 2 letters  
- `middle_word`: all characters except the first and last  

**Example:**

First 3 letters: Hol
Last 2 letters: on
Middle word: olberto

---

### **8-concat_edges.py**
Builds the sentence:

object-oriented programming with Python

using only slicing and concatenation from the original `str`.  
No loops, no conditionals, no new string literals.

---

### **9-easter_egg.py**
Prints **The Zen of Python**, by Tim Peters, using:

```python
import this
```
Script length must be ≤ 98 characters.

Output begins with:
The Zen of Python, by Tim Peters
and prints the full Zen of Python text.

🛠️ How to Run
Make scripts executable:
chmod u+x file.py
Run them:
./file.py
