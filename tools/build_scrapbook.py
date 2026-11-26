"""Tạo lại scrapbook.html từ khuôn mẫu + khối DATA trong index.html.

Chạy từ thư mục gốc repo:  python3 tools/build_scrapbook.py
Mọi nội dung (dự án, sự kiện, liên hệ...) chỉ sửa trong khối DATA của index.html,
rồi chạy script này để bản scrapbook cập nhật theo.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
main = (ROOT / "index.html").read_text(encoding="utf-8")
m = re.search(r"/\* =+\n   SỬA NỘI DUNG CỦA BẠN Ở ĐÂY.*?/\* =+ HẾT PHẦN CẦN SỬA =+ \*/", main, re.S)
if not m:
    raise SystemExit("Không tìm thấy khối DATA trong index.html")

tpl = (ROOT / "tools" / "scrapbook-template.html").read_text(encoding="utf-8")
if tpl.count("/*DATA*/") != 1:
    raise SystemExit("Khuôn mẫu phải có đúng một chỗ /*DATA*/")
page = tpl.replace("/*DATA*/", m.group(0))

head = ('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n')
k = page.index("</style>") + len("</style>")
out = head + page[:k] + "\n</head>\n<body>\n" + page[k:].lstrip("\n") + "\n</body>\n</html>\n"
(ROOT / "scrapbook.html").write_text(out, encoding="utf-8")
print("Đã tạo scrapbook.html")
