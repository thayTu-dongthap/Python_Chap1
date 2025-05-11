#Sử dụng hàm print trong Python
"""
1. ý nghĩa: Sử dụng hàm print để hiển thị thông tin ra ngoài
2. Cú pháp cơ bản:
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Trong đó:
    objects: Các đối tượng cần in (có thể là chuỗi, số, biến...).
    sep: Ký tự phân cách giữa các đối tượng (mặc định là khoảng trắng ' ').
    end: Ký tự kết thúc (mặc định là xuống dòng '\n'
    file: Nơi xuất dữ liệu (mặc định là màn hình, có thể thay bằng tệp tin).
    flush: Quyết định xem dữ liệu có được đẩy ngay ra đầu ra hay không (mặc định False).
"""
#Hiển thị chuỗi
print("Xin chào Python")
#Hiển thị số ra ngoài thông qua hàm print
print(5+6)
#- In nhiều đối tượng
_Name="Cao Tụ"
_Tuoi=36
print("Tôi tên là: ", _Name," Tuổi: ",_Tuoi)
#Thay đổi phân cách (sep):
print( "10", "05","2023", sep="/")
#Thay đổi ký tự kết thúc (end):
print("Xin chào", end=" ")
print("Python!")
# Output: Xin chào Python!
# In kết hợp với f-string (Python 3.6+):
price = 19.9
print(f"Giá: {price} USD")
# Output: Giá: 99.99 USD
_Thang=3
print(f"Lập trình Python trong {_Thang} tháng cho người mới bắt đầu")