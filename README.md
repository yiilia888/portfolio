# Portfolio Minh Nhàn

Trang portfolio cá nhân, gồm giới thiệu, dự án tại UEL và hoạt động sự kiện. Có 2 phiên bản:
- `/` là bản chính, phong cách trời mây (mặc định).
- `/scrapbook.html` là bản phụ, phong cách scrapbook denim.

Chuyển qua lại bằng nút ở góc dưới bên phải.

## Sửa nội dung
1. Mở `index.html`, tìm đoạn `SỬA NỘI DUNG CỦA BẠN Ở ĐÂY` và sửa trong khối `DATA`.
2. Chạy `python3 tools/build_scrapbook.py` để bản scrapbook cập nhật theo.
3. Push lên GitHub, Vercel tự deploy.

## Deploy trên Vercel
Import repo, chọn Framework Preset là **Other**, để trống Build Command và Output Directory, rồi bấm Deploy.

Chi tiết các quyết định thiết kế và việc còn dang dở: xem `CLAUDE.md`.
