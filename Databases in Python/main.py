#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn
 
 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()

    cur.execute("SELECT albums.title, artists.name FROM albums INNER JOIN artists ON albums.artistId = artists.artistId")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

def main():
    database = r"sample.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Query all tasks")
        select_all_tasks(conn)
 
    
main()