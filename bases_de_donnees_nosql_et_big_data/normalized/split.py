import fitz
import os

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))

SKIP_FOLDER = "DS_examens"
SKIP_SELF = "normalized"   # <--- IMPORTANT
OUT_DIR = os.getcwd()

def should_process(path: str) -> bool:
    # Skip if inside DS_examens
    rel = os.path.relpath(path, BASE_DIR)
    parts = rel.split(os.sep)

    if SKIP_FOLDER in parts:
        return False

    if SKIP_SELF in parts:
        return False

    return path.lower().endswith(".pdf")


def split_pdf(input_path: str):
    doc = fitz.open(input_path)
    name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(OUT_DIR, f"{name}_split.pdf")

    out = fitz.open()

    for i, page in enumerate(doc):
        rect = page.rect
        mid = rect.height / 2

        top_rect = fitz.Rect(rect.x0, rect.y0, rect.x1, mid)
        bottom_rect = fitz.Rect(rect.x0, mid, rect.x1, rect.y1)

        new_page_top = out.new_page(width=rect.width, height=rect.height/2)
        new_page_top.show_pdf_page(new_page_top.rect, doc, i, clip=top_rect)

        new_page_bottom = out.new_page(width=rect.width, height=rect.height/2)
        new_page_bottom.show_pdf_page(new_page_bottom.rect, doc, i, clip=bottom_rect)

    out.save(output_path)
    print(f"✔ Created: {output_path}")


print("Scanning folder:", BASE_DIR)

for root, dirs, files in os.walk(BASE_DIR):
    # Skip normalized folder entirely
    if root.endswith(SKIP_SELF):
        continue

    # Skip DS exams
    if SKIP_FOLDER in root:
        continue

    for f in files:
        full_path = os.path.join(root, f)
        if should_process(full_path):
            split_pdf(full_path)

print("\nDone!")
