import pymysql

def connectToDb():
    connectionObj = pymysql.Connect(host = 'localhost',port = 3306, user = 'root', password = 'root123', db = 'shreya', charset = 'utf8')
    print(type(connectionObj))
    print('Database connected successfully.')
    return connectionObj

def disconnectDb(connectionObj):
    connectionObj.close()
    print('Database disconnected successfully.')

def my_app():
    try:
        connection = connectToDb()
    except:
        print('Database disconnected successfully.')
    else:
        disconnectDb(connection)