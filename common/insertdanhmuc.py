# Hàm thêm danh mục
from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def insert_danhmuc(tendm, mota):
    try:
        connection = connect_mysql()
        if connection is None:
            return

        cursor = connection.cursor()
        sql = "INSERT INTO danhmuc (tendm, mota) VALUES (%s, %s)"
        data = (tendm, mota)
        cursor.execute(sql, data)
        connection.commit()

        print(f"✅ Đã thêm danh mục: {tendm}")
    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
