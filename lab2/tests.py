import sqlite3 as sq
import time
import base_table_gen
import random


def INSERT_TESTS(cur):

    f = open("research/insert.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)
        new_tab = "clone_T" + str(i+1)
        old_tab = "T" + str(i+1)
        cur.execute("CREATE TABLE "+new_tab+" AS SELECT * FROM "+old_tab)
        f.write(str(start)+'\n')
        for _ in range(100):
            begin = time.time()

            base_table_gen.instert_rand_data(cur,"clone_T"+str(i+1))

            end = time.time() - begin
            f.write(str(end)+'\n')
            cur.execute("DELETE FROM clone_T"+str(i+1)+" WHERE id = "+str(start + 1))
        cur.execute("DROP TABLE "+new_tab)
    f.close()


def DELETE_TESTS(cur):

    f = open("research/delete.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)
        new_tab = "clone_T" + str(i+1)
        old_tab = "T" + str(i+1)
        cur.execute("CREATE TABLE "+new_tab+" AS SELECT * FROM "+old_tab)
        f.write(str(start)+'\n')

        used_ids = []

        for _ in range(100):


            cur.execute("SELECT value FROM "+new_tab+" ORDER BY RANDOM() LIMIT 1")
            val = cur.fetchall()[0]

            begin = time.time()

            cur.execute("DELETE FROM clone_T"+str(i+1)+" WHERE value = ?",val)
       
            end = time.time() - begin
            f.write(str(end)+'\n')
            base_table_gen.instert_rand_data(cur,"clone_T"+str(i+1))
        cur.execute("DROP TABLE "+new_tab)
    f.close()


def UPDATE_TESTS(cur):

    f = open("research/update.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)
        new_tab = "clone_T" + str(i+1)
        old_tab = "T" + str(i+1)
        cur.execute("CREATE TABLE "+new_tab+" AS SELECT * FROM "+old_tab)
        f.write(str(start)+'\n')
        for _ in range(100):

            r = random.randrange(1,start)

            begin = time.time()

            cur.execute("UPDATE "+new_tab+" SET value = 'hi' WHERE id = "+str(r))

            end = time.time() - begin
            
            f.write(str(end)+'\n')
        cur.execute("DROP TABLE "+new_tab)
    f.close()

def SELECTKEY_TEST(cur):

    f = open("research/selectkey.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)
        new_tab = "clone_T" + str(i+1)
        old_tab = "T" + str(i+1)
        cur.execute("CREATE TABLE "+new_tab+" AS SELECT * FROM "+old_tab)
        f.write(str(start)+'\n')
        for _ in range(100):

            r = random.randrange(1,start)

            begin = time.time()

            cur.execute("SELECT * FROM "+new_tab+" WHERE id = ?",(r,))

            end = time.time() - begin
        
            
            f.write(str(end)+'\n')
        cur.execute("DROP TABLE "+new_tab)
    f.close()


def SELECTNOKEY_TEST(cur):

    f = open("research/selectnokey.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)
        new_tab = "clone_T" + str(i+1)
        old_tab = "T" + str(i+1)
        cur.execute("CREATE TABLE "+new_tab+" AS SELECT * FROM "+old_tab)
        f.write(str(start)+'\n')
        for _ in range(100):

            r = random.randrange(1,start)

            # cur.execute("SELECT value FROM "+old_tab+" WHERE id = ?",(r,))

            # val = cur.fetchall()[0]

            begin = time.time()

            cur.execute("SELECT * FROM "+new_tab+" WHERE value = ?",("data:"+str(r),))
            # print("data:"+str(r))
            # cur.execute("SELECT * FROM "+new_tab+" WHERE value = ?",val)

            end = time.time() - begin
            f.write(str(end)+'\n')
        cur.execute("DROP TABLE "+new_tab)


    f.close()