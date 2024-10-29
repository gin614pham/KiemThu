# Bài tập nhóm môn Đảm bảo chất lượng và kiểm thử phần mềm

Nhóm chúng tôi sử dụng pytest và mô hình POM để tạo Test Automation

Kiểm thử các chức năng sau:

- Login
- New Customer
- New Account
- Deposit
- Widthdraw
- Fund Transfer
- Customized Statement Form
- Log out

Trên web [Guru99Bank](http://www.demo.guru99.com/V4/)

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

## Chạy Bài Kiểm Tra Tự Động

### Chạy toàn bộ bài kiểm tra tự động

```bash
    pytest tests/ -v
```

> **Trong trường hợp muốn xuất báo cáo ra file HTML**

```bash
    pytest -v --html=report.html tests/
```

Đảm bảo đã cài đặt `pytest-html` trước khi chạy lệnh xuất báo cáo

```bash
    pip install pytest-html
```

### Chạy riêng lẻ cho từng chức năng

1. **Chạy kiểm thử tự động cho chức năng Login**

```bash
    pytest tests/test_login.py -v
```

2. **Chạy kiểm thử tự động cho chức năng New Customer**

```bash
    pytest tests/test_new_customer.py -v
```

> ❗ **Lưu ý:** Thay đổi Email cho dữ liệu test của 2 hàm`test_create_new_customer` và`test_create_new_customer_with_existing_email`trong`/tests/test_new_customer.py`

3. **Chạy kiểm thử tự động cho chức năng New Account**

```bash
    pytest tests/test_new_customer.py -v
```

4. **Chạy kiểm thử tự động cho chức năng Deposit**

```bash
    pytest tests/test_deposit.py -v
```

5. **Chạy kiểm thử tự động cho chức năng X**
6. **Chạy kiểm thử tự động cho chức năng X**
7. **Chạy kiểm thử tự động cho chức năng X**

8. **Chạy kiểm thử tự động cho chức năng Logout**

```bash
    pytest tests/test_logout.py -v
```
