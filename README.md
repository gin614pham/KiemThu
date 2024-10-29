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

1. **Chạy kiểm thử tự động cho chức năng Login**

```bash
    pytest tests/test_login.py -v
```

2. **Chạy kiểm thử tự động cho chức năng New Customer**

```bash
    pytest tests/test_new_customer.py -v
```

> ❗ **Lưu ý:** Thay đổi Email cho dữ liệu test của 2 hàm`test_create_new_customer` và`test_create_new_customer_with_existing_email`trong`/tests/test_new_customer.py`
