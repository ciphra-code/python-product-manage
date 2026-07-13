products = ["Táo", "Cam", "Xoài"] 

while True: 
    print("========= Menu =========") 
    print("1. Xem sản phẩm") 
    print("2. Thêm sản phẩm") 
    print("3. Xóa sản phẩm") 
    print("4. Đếm sản phẩm") 
    print("5. Tìm sản phẩm") 
    print("6. Thoát") 
    
    choice = int(input("Nhập lựa chọn: ")) 
    if choice ==1: 
        for i in range(len(products)): 
            print(i + 1, products[i]) 
            input("Nhấn Enter để quay lại menu")
    elif choice ==2: 
        name = input("Nhập tên sản phẩm cần thêm:") 
        if name in products: 
            print("Sản phẩm đã tồn tại") 
        else: products.append(name) 
        print("Thêm sản phẩm thành công") 
    elif choice ==3: 
        name = input("Nhập tên sản phẩm cần xóa:") 
        if name in products: 
            products.remove(name) 
            print("Xóa sản phẩm thành công") 
        else: 
            print("Không tìm thấy sản phẩm") 
    elif choice == 4: 
        print("Cửa hàng có", len(products), "Sản phẩm") 
    elif choice == 5: 
        name = input("Nhập tên sản phẩm cần tìm:") 
        if name in products: 
            print("Tìm thấy sản phẩm") 
        else: 
            print("Không tìm thấy sản phẩm") 
    elif choice == 6: 
        print("Tạm biệt!") 
        break