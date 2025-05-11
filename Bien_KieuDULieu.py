"""
Biến và Kiểu dữ liệu:
1. Đặc điểm của biến trong Python:
    Không cần khai báo kiểu: Kiểu dữ liệu được xác định tự động dựa trên giá trị gán.
    Tạo biến a có giá trị là 5
"""
_s="Biến a trỏ đến giá trị bộ nhớ mang giá trị : "
a=5
print(_s,a,sep=" ")
"""
Trong đó:
    +Dynamic Typing: Kiểu dữ liệu của biến có thể thay đổi trong quá trình thực thi.
    +Biến là tham chiếu: Biến không chứa giá trị trực tiếp mà trỏ đến đối tượng trong bộ nhớ.
"""
"""
2. Các kiểu dữ liệu phổ biến
    a. Kiểu cơ bản số nguyên (int) và kiểu số thực (float)
"""
a = 10       # int
b = 3.14     # float
print(a,b,sep=" ")
#Kiểu chuỗi
_str="Kiểu dữ lệu dạng chuỗi"
#KiểudduBoooolean (Đúng/Sai)
_kiemtra = True
"""
* Quy tắc đặt tên biến
    + Bắt đầu bằng chữ cái hoặc _.
    + Không chứa ký tự đặc biệt (trừ _).
    + Phân biệt hoa thường: myVar ≠ myvar.
    + Tránh từ khóa Python: if, for, class,...
* Kiểm tra kiểu dữ liệu
    Dùng hàm type() hoặc isinstance():
"""
print(type(_kiemtra))
"""
1. Phép toán trên kiểu số (int, float)
    Phép toán	    Ký hiệu	    Ví dụ	    Kết quả	Ghi chú
    Cộng	        +	        5 + 3	            8	
    Trừ	            -	        10 - 2.5	        7.5	
    Nhân	        *	        4 * 3	            12	
    Chia	        /	        10 / 3	            3.333...	Luôn trả về float
    Chia nguyên	    //	        10 // 3	            3	Làm tròn xuống
    Lũy thừa	    **	        2 ** 3	            8	
    Chia dư     	%	        10 % 3	            1	Lấy phần dư
2. Phép toán trên chuỗi (str)
    Phép toán	        Ký hiệu	                        Ví dụ	                    Kết quả	Ghi chú
    Nối chuỗi	            +	                        "Hello" + " World"	        "Hello World"	
    Lặp chuỗi	            *	                        "Hi" * 3	                "HiHiHi"	
    Truy cập ký tự	        [index]	                    "Python"[1]	                'y'	   Index bắt đầu từ 0
    Cắt chuỗi	            [start:end]	                "Python"[2:4]	            "th"	Lấy từ start đến end-1
3. Phép toán trên kiểu boolean (bool)
    Phép toán	        Ký hiệu	            Ví dụ	            Kết quả	Ghi chú
    Phủ định	        not	                not True	        False	
    Và (AND)	        and	                True and False	    False	Cả hai phải đúng
    Hoặc (OR)	        or	                True or False	    True	Chỉ cần một đúng
4. Phép toán so sánh (Áp dụng cho mọi kiểu)
    Phép toán	        Ký hiệu	            Ví dụ	                Kết quả	Ghi chú
    Bằng	            ==	                5 == 5.0	            True	            Kiểu khác nhau vẫn có thể bằng
    Khác	            !=	                "a" != "A"	            True	
    Lớn hơn	            >	                10 > 5	                True	
    Nhỏ hơn	            <	                3.14 < 5	            True	
    Lớn hơn hoặc bằng	>=	                7 >= 7	                True	
    Nhỏ hơn hoặc bằng	<=	                "apple" <= "banana"	    True	So sánh theo thứ tự từ điển
5. Ép kiểu dữ liệu (Type Casting)
    Hàm	            Ví dụ	        Kết quả	Ghi chú
    int()	        int("10")	        10	Chuyển chuỗi số thành int
    float()	        float(5)	        5.0	Chuyển int thành float
    str()	        str(3.14)	        "3.14"	Chuyển mọi kiểu thành str
    bool()	        bool(0)	False	    0, "", None → False
"""