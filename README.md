# Bài tập nhóm môn Đảm bảo chất lượng và kiểm thử phần mềm

Kiểm thử các chức năng sau:

Login

Logout

Register a Patient

Find Patient Record

View the Patient

Search a Patient

Book an Appointment

Capture Vitals

Cho web https://demo.openmrs.org/openmrs/login.htm

## Thành viên nhóm

- Phạm Hoàng Phúc - 21IT640
- Phạm Quốc Phú -
- Lê Nhật Linh -
- Trình Đàm Huy -

## Công Nghệ Đã Sử Dụng

- Python 3.12
- [Selenium](https://www.selenium.dev/)
- [pytest](https://pytest.org/)

## Cài Đặt

1. **Clone Repository**

```bash
    git clone https://github.com/gin614pham/KiemThu.git
```

2. **Cài Đặt Các Gói Cần Thiết**

- Cài đặt Selenium và pytest

```bash
    pip install selenium pytest
```

3. **Cài Đặt WebDriver**
   Để chạy bài kiểm tra tự động, cần cài đặt WebDriver cho trình duyệt muốn kiểm tra.

   Tải file WebDriver cần thiết và thay đường dẫn file vào `service = Service(r"D:\Code\chromedriver-win64\chromedriver.exe")`
   trong file `test_login.py`

## Chạy Bài Kiểm Tra Tự Động

1. **Chạy kiểm thử tự động cho chức năng Login**

```bash
    pytest test_login.py -v
```
