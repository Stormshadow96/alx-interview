---

# Curriculum

## Short Specializations

- 0x01. Lockboxes

## Must Know

For this project, you will need a solid understanding of several key concepts:

- **Lists and List Manipulation**
- **Graph Theory Basics**
- **Algorithmic Complexity**
- **Recursion**
- **Queue and Stack**
- **Set Operations**

By reviewing these concepts, you will be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.

---

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

---

## Tasks

### 0. Lockboxes (mandatory)

Write a method that determines if all the boxes can be opened.

Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- Return True if all boxes can be opened, else return False

---

## Usage

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```

---

## Repo

- GitHub repository: alx-interview
- Directory: 0x01-lockboxes
- File: 0-lockboxes.py

---

Copyright © 2024 ALX, All rights reserved.

---

