import os
import csv
from tqdm import tqdm


OUTPUT_FILE = f"{SEARCH_TERM}_matches.csv"
VALID_EXTENSIONS = {".py", ".c", ".h", ".cpp", ".txt", ".md", ".rst", ".hpp", ".cc"}

def is_text_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            sample = f.read(512)
        return b'\0' not in sample
    except Exception:
        return False

def find_references(root_folder):
    matched_lines = []
    all_files = []

    for root, _, files in os.walk(root_folder):  # ✅ Recursively walks all subfolders
        for file in files:
            if any(file.endswith(ext) for ext in VALID_EXTENSIONS):
                full_path = os.path.join(root, file)
                if is_text_file(full_path):
                    all_files.append(full_path)

    pbar = tqdm(total=len(all_files), desc="Searching files", unit="file")

    for filepath in all_files:
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                for line_number, line in enumerate(f, 1):
                    if SEARCH_TERM in line:
                        matched_lines.append((filepath, line_number, line.strip()))
        except Exception as e:
            print(f"⚠️ Skipping file due to error: {filepath}\n{e}")
        pbar.update(1)

    pbar.close()
    return matched_lines

def write_csv(results, OUTPUT_FILE):
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["filepath", "line_number", "line_text"])
        writer.writerows(results)

if __name__ == "__main__":
    print("🔍 Paste the target folder path to search (drag folder into terminal or paste manually):")
    SEARCH_TERM = input("Enter search term (case sensitive): ").strip()
    folder = input("Target folder: ").strip().strip('"').strip("'")

    if not os.path.isdir(folder):
        print(f"❌ Invalid folder: {folder}")
        exit(1)

   
    print(f"📁 Searching for case-sensitive '{SEARCH_TERM}' in: {folder}")
    results = find_references(folder)
    write_csv(results, OUTPUT_FILE)
    print(f"✅ Done. Results saved to: {OUTPUT_FILE} ({len(results)} matches)")
