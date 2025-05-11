"""
Hàm đọc giá trị vào từ bàn phím
1. Cấu trúc hàm input
    input([prompt])
    Trong đó:
    + prompt (tùy chọn): Chuỗi hiển thị để hướng dẫn người dùng nhập liệu.
    + Giá trị trả về: Luôn là một chuỗi (str) chứa nội dung người dùng nhập vào.
* Ví dụ: Viết lệnh nhập vào họ tên in ra Xin chào bạn: _ten
"""
_ten= input("Nhập vào tên bạn")
print("Xin chào bạn: ",_ten)
"""
Do giá trị trã về  là một chuỗi nên bạn phải ép về kiểu dữ liệu bạn cần tính toán (int, float,.._
Xử lí trường hợp nhập sai gi trị là số nguyên
"""
try:
    _tuoi = int(input("Nhập vào tuổi của bạn "))
    print(f"Tuổi ta của bạn là: {_tuoi + 1} ")
except ValueError:
    print("Bạn phải nhập số!")
finally:
    #xóa biến _tuoi
    del _tuoi
"""
Xử lí chuỗi có nhiều khoản trắng
sử dụng hàm strip()
"""
_str= "  Lập trình Python xử   lí chuỗi    có khoảng trắng thừa   "
print(f"Độ dài chuỗi chưa bỏ khoảng trắng thừa: {len(_str)}")
_str= _str.strip()
print(f"Chuỗi đã xử lí khoảng trắng thừa {len(_str)}")
