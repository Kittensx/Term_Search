# Term_Search
Given any folder +  subfolders and your search term, you can quickly find results for thousands of files. Accepts command line input.

# 🔍 Term Search with CSV Output

This script (`term_search.py`) allows you to recursively search for a **case-sensitive** string (e.g., `exp2`) across all text-based files in a specified folder. It outputs a `.csv` file containing each match with file path, line number, and line content.

---

## 🚀 Features

- ✅ Case-sensitive string search
- 📂 Recursively scans subfolders
- 📜 Filters common text source files (`.py`, `.c`, `.h`, `.cpp`, `.txt`, etc.)
- 📉 Skips binary files
- 📊 Progress bar with ETA (`tqdm`)
- 📁 CSV output with:
  - File path
  - Line number
  - Matching line content

---

## 🛠 Requirements

Install `tqdm` if not already installed:

```bash
pip install tqdm
