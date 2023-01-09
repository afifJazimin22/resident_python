import mysql.connector
import uuid


def check_item_availability(plate):

    conn = mysql.connector.connect(host='localhost',
        user='root',
        password='Hustle4hasil_',
        database='resident')
    print("this is {}".format(plate))
    cursor = conn.cursor()
    query = f"SELECT * FROM cars WHERE plateNumber = '{plate}'"
    # query = {plate}
    print(query)
    cursor.execute(query)

    result = cursor.fetchone()

    # print(test)

    if result:
        cursor.execute(f"INSERT INTO car_logs (id, Description, plateNumber) VALUES ( uuid(), 'This {plate} has entered Sakura Resident','{plate}')")
        conn.commit()
        return True

    else:
        return False

