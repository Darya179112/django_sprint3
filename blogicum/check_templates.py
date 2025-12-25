from pathlib import Path
import os

# Вычислите BASE_DIR как в settings.py
BASE_DIR = Path(__file__).resolve().parent.parent

print(f"Current working directory: {os.getcwd()}")
print(f"BASE_DIR: {BASE_DIR}")
print(f"Templates directory: {BASE_DIR / 'templates'}")
print(f"Exists? {(BASE_DIR / 'templates').exists()}")

# Проверьте конкретные файлы
index_path = BASE_DIR / 'templates' / 'blog' / 'index.html'
about_path = BASE_DIR / 'templates' / 'pages' / 'about.html'

print(f"\nblog/index.html path: {index_path}")
print(f"Exists? {index_path.exists()}")

print(f"\npages/about.html path: {about_path}")
print(f"Exists? {about_path.exists()}")

# Проверьте содержимое
if index_path.exists():
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()[:100]
        print(f"\nFirst 100 chars of index.html: {content}")