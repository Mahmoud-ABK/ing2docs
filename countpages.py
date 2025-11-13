from pathlib import Path
from PyPDF2 import PdfReader
from pptx import Presentation
import docx

root = Path(".")  # current directory (where Python file is placed)

def count_pages_pdf(path):
    try:
        reader = PdfReader(str(path))
        return len(reader.pages)
    except:
        return 0

def count_slides_pptx(path):
    try:
        prs = Presentation(str(path))
        return len(prs.slides)
    except:
        return 0

def count_pages_docx(path):
    try:
        doc = docx.Document(path)
        return len(doc.paragraphs)  # approximate pages by paragraphs
    except:
        return 0

def print_tree_with_totals(path: Path, prefix=""):
    total_pages = 0
    total_slides = 0
    total_paragraphs = 0

    entries = sorted([e for e in path.iterdir() if not e.name.startswith('.')], key=lambda x: (x.is_file(), x.name.lower()))

    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        rel_path = entry.relative_to(root)
        if entry.is_dir():
            print(f"{prefix}{connector}{rel_path}/")
            sub_totals = print_tree_with_totals(entry, prefix + ("    " if i == len(entries) - 1 else "│   "))
            total_pages += sub_totals['pages']
            total_slides += sub_totals['slides']
            total_paragraphs += sub_totals['paragraphs']
            print(f"{prefix}{'    ' if i == len(entries) - 1 else '│   '}└── Total for {rel_path}: "
                  f"{sub_totals['pages']} pages (*{sub_totals['pages']*2}, *{sub_totals['pages']*4}), "
                  f"{sub_totals['slides']} slides (*{sub_totals['slides']*2}, *{sub_totals['slides']*4}), "
                  f"{sub_totals['paragraphs']} paragraphs (*{sub_totals['paragraphs']*2}, *{sub_totals['paragraphs']*4})")
        else:
            if entry.suffix.lower() == ".pdf":
                count = count_pages_pdf(entry)
                total_pages += count
                label = f"[{count} pages (*{count*2}, *{count*4})]"
            elif entry.suffix.lower() == ".pptx":
                count = count_slides_pptx(entry)
                total_slides += count
                label = f"[{count} slides (*{count*2}, *{count*4})]"
            elif entry.suffix.lower() in [".docx", ".doc"]:
                count = count_pages_docx(entry)
                total_paragraphs += count
                label = f"[{count} paragraphs (*{count*2}, *{count*4})]"
            else:
                label = ""
            print(f"{prefix}{connector}{rel_path} {label}")

    return {'pages': total_pages, 'slides': total_slides, 'paragraphs': total_paragraphs}

# Run the tree printing and get grand totals
grand_totals = print_tree_with_totals(root)
print("\nGrand Total:")
print(f"PDF pages: {grand_totals['pages']} (*{grand_totals['pages']*2}, *{grand_totals['pages']*4}), "
      f"PPTX slides: {grand_totals['slides']} (*{grand_totals['slides']*2}, *{grand_totals['slides']*4}), "
      f"Word paragraphs: {grand_totals['paragraphs']} (*{grand_totals['paragraphs']*2}, *{grand_totals['paragraphs']*4})")
