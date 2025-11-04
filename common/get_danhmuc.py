import mysql.connector
from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


# Hàm kết nối MySQL

# Hàm lấy danh sách tất cả danh mục
def get_all_danhmuc():
    try:
        connection = connect_mysql()
        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM danhmuc"
        cursor.execute(sql)
        result = cursor.fetchall()

        print("✅ Danh sách danh mục:")
        for row in result:
            print(f"ID: {row['madm']}, Tên: {row['tendm']}, Mô tả: {row['mota']}")

        return result

    except Error as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
