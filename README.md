# Lab 6.1 Thầy Nguyễn Thế Bảo - Hướng dẫn sử dụng và chạy project
## Sinh Viện thực hiện Lê Văn Hoàng - 2224802010279
## 1. Clone project từ GitHub

```powershell
git clone https://github.com/EurusDFIR/Lab6.1.git
cd Lab6.1.git
```

## 2. Tạo môi trường ảo Python

```powershell
python -m venv venv
venv\Scripts\Activate.ps1  # Nếu dùng PowerShell
# hoặc
venv\Scripts\activate.bat  # Nếu dùng CMD
```

## 3. Cài đặt các thư viện cần thiết

```powershell
pip install -r requirements.txt
```

## 4. Tạo database PostgreSQL

- Đăng nhập vào pgAdmin hoặc dùng lệnh psql.
- Tạo database tên đúng là: `2224802010279`
- Tài khoản, mật khẩu, host, port phải giống trong file `2224802010279.py`:
  - user: `postgres`
  - password: `eurus`
  - host: `localhost`
  - port: `5432`

Ví dụ lệnh SQL:

```sql
CREATE DATABASE "2224802010279";
```

## 5. Chạy chương trình

```powershell
python 2224802010279.py
```

## 6. Lưu ý

- Không cần cài đặt lại thư mục `venv` từ git (đã được loại trừ bằng `.gitignore`).
- Nếu muốn đổi thông tin kết nối database, sửa các biến ở đầu file `2224802010279.py`.
- Nếu gặp lỗi thiếu thư viện, hãy kiểm tra lại bước 3.

---

**Tóm tắt:**
Chỉ cần clone repo, tạo môi trường ảo, cài thư viện bằng `requirements.txt`, tạo database và chạy file python là xong!
