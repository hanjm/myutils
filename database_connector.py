# coding=utf-8
from __future__ import unicode_literals, print_function

import MySQLdb


# database connection
def get_mysql_connection():
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", db="solobookmovies",
                           use_unicode=True)
    cursor = conn.cursor()
    # 统一utf-8
    conn.set_character_set('utf8')
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    return conn, cursor
