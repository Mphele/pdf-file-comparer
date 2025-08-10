# PDF File Comparator

A simple Python script that compares two PDF files to check if they are **identical**, using **SHA-1 hashing**.
It validates file types, checks for existence, and processes files in chunks for efficiency.

## Features

* **File validation**: Ensures the provided files are PDFs and exist before processing.
* **Chunked reading**: Reads files in 4KB chunks to handle large files efficiently.
* **Hash comparison**: Uses SHA-1 hashing to determine if files are identical.
* **Pathlib integration**: Cleaner, cross-platform file path handling.

## How It Works

1. The user is prompted to enter two PDF file paths.
2. The script validates that:

   * Both are `.pdf` files.
   * Both files exist in the given paths.
3. Each file is read in chunks and hashed using SHA-1.
4. The resulting hashes are compared:

   * **Match** → "Files are identical"
   * **Mismatch** → "Files are different"

## Requirements

* Python 3.7+
* No external libraries required (only built-in modules hashlib and pathlib).

## Usage

python pdf_comparator.py


Example:

```
Enter first file name/path: sample1.pdf
Enter second file name/path: sample2.pdf
Files are different
```

## Example Output

* If files match:

```
Files are identical
```

* If files differ:

```
Files are different
```

## Why This Project?

This script is a practical introduction to:

* File handling in Python.
* Hash-based file comparison.
* Using Pathlib for clean file path operations.

It’s great for beginners who want to explore Python's built-in libraries while building something useful.

