# import modul
import sqlite3

def tambah_data(id, nama, email):
    try:
        sqliteConnection = sqlite3.connect('database_siswa.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil menambah terknoneksi ke database")
        a = sqliteConnection
        b = tambah_data()
        sqlite_create_table_query = '''CREATE TABLE data_siswa (
                                        id INTEGER PRIMARY KEY,
                                        nama TEXT NOT NULL,
                                        email text NOT NULL UNIQUE);'''
        cursor.execute(sqlite_create_table_query)
        print("Berhasil menambah data ke tabel")
        sqliteConnection.commit()
        sqlite_insert_with_param = """INSERT INTO data_siswa (
                                        id , nama , email )
                                        VALUES(?, ?, ?);"""

        data_tuple = (id, nama, email)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Berhasil Terkoneksi ke Database")
        cursor.close()

    except sqlite3.Error as error:
        print("Error Gagal terkoneksi ke Database", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("Koneksi Database Selesai")

tambah_data(2, 'rijal', 'rijal@gmail.com')
tambah_data(3, 'mimin', 'mimin@gmail.com')




