import pymysql
def deleteAccount():
 db_setting={
 "host": "192.168.90.45",
    "port": 30037,
    "user": "teconsole",
    "password": "teconsole!",
    "db": "TE_SSO",
    "charset": "utf8"
}
 conn = pymysql.connect(**db_setting)
 with conn.cursor() as cursor:

    aco ="delete From telligent_member.member_account ORDER BY creation_time desc LIMIT 1;"
    cursor.execute(aco)
    conn.commit()
    data = cursor.fetchall()
    print(data)
    conn.close()
