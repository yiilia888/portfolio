# Portfolio Minh Nhàn

Portfolio xin thực tập **C&B (Lương thưởng & Phúc lợi)** của sinh viên QTKD UEL. Trang tĩnh, không cần build. Push lên `main` thì Vercel tự deploy.

## Cấu trúc
| File | Vai trò |
|---|---|
| `index.html` | **Bản chính, mặc định** (phong cách trời mây). Chứa khối `DATA`, là **nguồn nội dung duy nhất**. |
| `scrapbook.html` | Bản phụ, phong cách scrapbook denim. **Không sửa tay**: file do `tools/build_scrapbook.py` tạo ra. |
| `tools/scrapbook-template.html` | Giao diện bản scrapbook, chứa chỗ đánh dấu `/*DATA*/`. |
| `tools/build_scrapbook.py` | Chèn `DATA` từ index.html vào khuôn mẫu, tạo `scrapbook.html`. |
| `tools/cover-vinamilk.html`, `tools/render_cover.js` | Nguồn và script render ảnh bìa dự án Vinamilk. |
| `images/` | Ảnh đại diện, ảnh sự kiện, chứng nhận. `images/projects/` chứa ảnh bìa 7 dự án. |

## Quy trình sửa
1. Sửa nội dung trong khối `DATA` của `index.html` (đoạn giữa `SỬA NỘI DUNG CỦA BẠN Ở ĐÂY` và `HẾT PHẦN CẦN SỬA`).
2. Chạy `python3 tools/build_scrapbook.py` để bản scrapbook cập nhật theo.
3. Commit, push `main`. Vercel tự cập nhật.

Sửa giao diện bản chính: CSS trong `index.html`. Sửa giao diện bản scrapbook: `tools/scrapbook-template.html`, rồi chạy lại bước 2.

## Đã chốt
- **Tên hiển thị:** chỉ ghi "Minh Nhàn", không ghi họ đầy đủ.
- **Bảng màu:** navy `#21355A`, xanh dương `#255997`, xanh trời `#79BFE1`, xanh nhạt `#AEDEED`. **Màu đậm chỉ dùng cho chi tiết nhỏ** (nút, nhãn, chip, ô ngày). Mảng lớn dùng màu nhạt.
- **Bản chính (mặc định):** lấy cảm hứng từ mẫu trời mây. Nền gradient xanh trời, mây, sao lấp lánh. Font Playfair Display (tên, tiêu đề), Dancing Script (chữ viết tay), Be Vietnam Pro (chữ thường). Đầu trang có ảnh tròn và 3 nhãn bay quanh, hàng 4 thẻ số liệu, phần "Về mình" có ảnh polaroid và 2 thẻ mục tiêu. Có chế độ sáng và tối.
- **Bản scrapbook:** lấy cảm hứng từ phong cách denim may vá. Chữ phồng vân denim, khuy áo, băng washi, khung ảnh kiểu khăn bandana, dải caro. Font Baloo 2 và Patrick Hand. Chỉ có chế độ sáng (nền giấy). Không dùng hình hay chữ của poster gốc.
- **Nút chuyển bản:** dạng viên thuốc xanh, cố định ở góc dưới bên phải, 2 bản cùng kiểu.
  - Bản chính sang scrapbook: icon **vương miện jean bo tròn** (đã chốt, đã bỏ phương án trái thơm). Hạt hồng và vàng ở đầu chóp, đường chỉ kem, trái tim hồng ở đế.
  - Scrapbook về bản chính: icon **cặp văn phòng**.
- **Bìa Vinamilk** do mình tự thiết kế (`tools/cover-vinamilk.html`). 6 bìa còn lại là trang đầu file hoặc ảnh chụp slide bạn gửi.
- **Link file:**
  - CV và 9 file dự án trên Google Drive đều để "Bất kỳ ai có liên kết – Người xem".
  - CV có ID `16zwjFPjY6ZQ_beMbskQ0G_kHwqD80gsb`. Khi sửa CV, dùng "Quản lý phiên bản → Tải phiên bản mới lên" để giữ nguyên link.

## Dữ kiện đã kiểm chứng
- **HCMC Marathon 2026:** mùa 13, chạy ngày 11/01/2026, gần 11.000 VĐV từ 75 quốc gia, xuất phát Công viên 30/4 trên đường Lê Duẩn, đơn vị vận hành Pulse Active. Đây không phải giải Techcombank (giải đó tổ chức tháng 12).
- **VnExpress Marathon HCMC Midnight 2026:** chứng nhận cấp ngày 22/03/2026, ban "Vật phẩm sau race".
- **Concert Anh Trai Vượt Ngàn Chông Gai 2026:** ngày 17–18/10/2026 tại KĐT Phú Long – Bình Trưng và The Global City.

## Còn chờ xác nhận
- **Ngày tháng:** bìa báo cáo Vinamilk ghi ngày 26/11/2025, file VietJet có từ năm 2025, nhưng CV và trang đang ghi 04–06/2026. CV còn ghi nhầm dự án FPT là "12/2026 – 03/2026".
- **Nội dung Claude tự đoán, cần xác nhận:**
  - Mục tiêu dài hạn "Chuyên viên C&B".
  - Vai trò ở concert (Operation, chuẩn bị ghế, suy ra từ ảnh).
  - Việc "trao vật phẩm sau race" ở VnExpress Marathon.
  - Câu tiêu đề "Đằng sau mỗi con số là một con người".
- **Còn thiếu:**
  - Mô tả đề tài Business Communication.
  - Vai trò cụ thể ở bài Veblen và Sharera.
  - Ảnh chân dung độ phân giải cao (ảnh hiện tại lấy từ CV, hơi mờ).
  - Ảnh tại HCMC Marathon.
- **Chưa làm:** nút chuyển ngôn ngữ VI/EN.
- **Lưu ý riêng tư:** trang công khai đang hiện số điện thoại.

## Ghi chú cho Claude
- Bản xem trước trên Claude:
  - Bản chính: https://claude.ai/artifact/EkRGtExhp9P7jCgZTVBjV1
  - Scrapbook: https://claude.ai/artifact/6mHb7LuQGQcv5uddo2cLpv
- Trang xem trước không có `<!doctype>`, `<html>` hay `<head>`. Muốn đăng bản xem trước thì bỏ phần khung đó khỏi file repo.
- Sau mỗi lần sửa, chụp màn hình bằng Playwright để kiểm tra: không lỗi console, ở bề rộng 390px không bị cuộn ngang.
