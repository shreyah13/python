import pymysql

def connectToDb():
    connectionObj = pymysql.Connect(
        host='localhost', port=3306, user='root', password='Root123', db='nithin_db', charset='utf8'
    )
    print('DB connected')
    return connectionObj    

def disconnectDb(connectionObj):
    connectionObj.close()
    print('DB disconnected')

def updateRow():
    query = 'update students set name = %s where id = %s'
    name = input('Enter name to be updated: ')
    id = input('Enter Id of the student to update record: ')
    try:
        conn = connectToDb()
        my_cursor = conn.cursor()
        count = my_cursor.execute(query, (name, id) )
        if count == 0:
            print(f'Student with id={id} not found') 
        else:
            print('Row updated')
        conn.commit()
        my_cursor.close()
    except Exception as e:
        print('Table deletion failed')
        print(e)
    else:
        disconnectDb(conn)

updateRow()