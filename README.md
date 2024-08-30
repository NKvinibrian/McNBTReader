# McNBTReader
A lightweight library for reading, editing, and saving Minecraft NBT files.

## Overview
McNBTReader is a Python library designed to efficiently handle Minecraft's NBT (Named Binary Tag) files, including `.dat`, `.schematic`, and `.nbt` formats.

## Important
This library is optimized for Python 3.12. Using previous versions of Python may result in performance issues.

## Features
- **Read NBT Files**: Supports `.dat`, `.schematic`, and `.nbt` files.
- **Edit NBT Files**: Currently under development.
- **Save NBT Files**: Currently under development.

## Usage

```python
from mcnbt.nbt import Nbt

tree = Nbt().read_file("your_file_path")
print(tree.name)
entity = tree['Schematic']['Entities'][0]['Pos']
print(f'x: {entity[0]} y: {entity[1]} z: {entity[2]}')
```
[LICENSE](LICENSE)