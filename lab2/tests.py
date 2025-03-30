import sqlite3 as sq
import time
import base_table_gen
import random


def clone_table(org_name,cur):
    new_name = "clone_"+ org_name
    cur.execute("CREATE TABLE "+new_name+" ('id' INTEGER UNIQUE,'value'	TEXT, PRIMARY KEY ('id' AUTOINCREMENT))")
    cur.execute("INSERT INTO "+new_name+ " SELECT * FROM "+ org_name)
    return new_name
    
def INSERT_TESTS(cur):

    f = open("research/insert.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)

        old_tab = "T" + str(i+1)
        new_tab = clone_table(old_tab,cur)

        f.write(str(start)+'\n')
        for _ in range(100):

            begin = time.time()
            base_table_gen.instert_rand_data(cur,new_tab,"hi")
            end = time.time() - begin

            f.write(str(end)+'\n')
            cur.execute("DELETE FROM "+new_tab+" WHERE id = ?",((start + 1),))
        cur.execute("DROP TABLE "+new_tab)
    f.close()


def val_DELETE_TESTS(cur):

    f = open("research/val_delete.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)
        
        old_tab = "T" + str(i+1)
        new_tab = clone_table(old_tab,cur)

        f.write(str(start)+'\n')

        for _ in range(100):

            cur.execute("SELECT value FROM "+new_tab+" ORDER BY RANDOM() LIMIT 1")
            val = cur.fetchall()[0]

            begin = time.time()

            cur.execute("DELETE FROM "+new_tab+" WHERE value = ?",val)
       
            end = time.time() - begin
            f.write(str(end)+'\n')
            base_table_gen.instert_rand_data(cur,new_tab,"val")

        cur.execute("DROP TABLE "+new_tab)
    f.close()

def key_DELETE_TESTS(cur):

    f = open("research/key_delete.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)
        
        old_tab = "T" + str(i+1)
        new_tab = clone_table(old_tab,cur)

        f.write(str(start)+'\n')

        for _ in range(100):

            cur.execute("SELECT id FROM "+new_tab+" ORDER BY RANDOM() LIMIT 1")
            val = cur.fetchall()[0]
            
            begin = time.time()

            cur.execute("DELETE FROM "+new_tab+" WHERE id = ?",val)
       
            end = time.time() - begin
            f.write(str(end)+'\n')
            base_table_gen.instert_rand_data(cur,new_tab,"val")

        cur.execute("DROP TABLE "+new_tab)
    f.close()


def key_UPDATE_TESTS(cur):

    f = open("research/key_update.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)

        old_tab = "T" + str(i+1)
        new_tab = clone_table(old_tab,cur)

        f.write(str(start)+'\n')
        for _ in range(100):

            r = random.randrange(1,start)

            begin = time.time()

            cur.execute("UPDATE "+new_tab+" SET value = 'hi' WHERE id = "+str(r))

            end = time.time() - begin
            
            f.write(str(end)+'\n')
        cur.execute("DROP TABLE "+new_tab)
    f.close()

def val_UPDATE_TESTS(cur):

    f = open("research/val_update.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)

        old_tab = "T" + str(i+1)
        new_tab = clone_table(old_tab,cur)
        
        f.write(str(start)+'\n')
        for _ in range(100):

            r = random.randrange(1,start)

            begin = time.time()

            cur.execute("UPDATE "+new_tab+" SET value = 'hi' WHERE value = ?",("data:"+str(r),))

            end = time.time() - begin
            
            f.write(str(end)+'\n')
        cur.execute("DROP TABLE "+new_tab)
    f.close()


def key_SELECT_TESTS(cur):

    f = open("research/key_select.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)
        
        old_tab = "T" + str(i+1)
        new_tab = clone_table(old_tab,cur)

        f.write(str(start)+'\n')
        for _ in range(100):

            r = random.randrange(1,start)

            begin = time.time()

            cur.execute("SELECT * FROM "+new_tab+" WHERE id = ?",(r,))

            end = time.time() - begin
        
            
            f.write(str(end)+'\n')
        cur.execute("DROP TABLE "+new_tab)
    f.close()


def val_SELECT_TESTS(cur):

    f = open("research/val_select.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)

        old_tab = "T" + str(i+1)
        new_tab = clone_table(old_tab,cur)

        f.write(str(start)+'\n')
        for _ in range(100):

            r = random.randrange(1,start)

            begin = time.time()

            cur.execute("SELECT * FROM "+new_tab+" WHERE value = ?",("data:"+str(r),))

            end = time.time() - begin
            f.write(str(end)+'\n')
        cur.execute("DROP TABLE "+new_tab)


    f.close()


def mask_SELECT_TESTS(cur):

    f = open("research/mask_select.txt","w")

    start = 10

    for i in range(0,3):
        start = start * (10)

        old_tab = "T" + str(i+1)
        new_tab = clone_table(old_tab,cur)

        f.write(str(start*10)+'\n')
        for _ in range(100):

            r = random.randrange(1,start)

            begin = time.time()

            cur.execute("SELECT * FROM "+new_tab+" WHERE value LIKE ?",("%ta"+str(r)+"%",))

            end = time.time() - begin
            f.write(str(end)+'\n')
        cur.execute("DROP TABLE "+new_tab)


    f.close()


def litle_OPTIMIZE_TESTS(cur,con):

    f = open("research/litle_optimaze.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)

        print(i)

        f.write(str(start)+'\n')
        for _ in range(100):

            old_tab = "T" + str(i+1)
            new_tab = clone_table(old_tab,cur)

            to_del = random.sample(range(1,start),200)
            # for _ in range(start - 200):
            #     cur.execute("SELECT id FROM "+new_tab+" ORDER BY RANDOM() LIMIT 1")
            #     val = cur.fetchall()[0]
            #     cur.execute("DELETE FROM "+new_tab+" WHERE id = ?",val)

            for id in to_del:
                cur.execute("DELETE FROM "+new_tab+" WHERE id = ?",(id,))

            con.commit()
            begin = time.time()
            # cur.execute("OPTIMIZE TABLE "+ new_tab)
            cur.execute("VACUUM")
            end = time.time() - begin
            f.write(str(end)+'\n')

            con.commit()
            cur.execute("DROP TABLE "+new_tab)


    f.close()



def big_OPTIMIZE_TESTS(cur,con):

    f = open("research/big_optimaze.txt","w")

    start = 100

    for i in range(0,3):
        start = start * (10)

        print(i)

        f.write(str(start)+'\n')
        for _ in range(100):

            old_tab = "T" + str(i+1)
            new_tab = clone_table(old_tab,cur)

            to_del = random.sample(range(1,start),start - 200)
            # for _ in range(start - 200):
            #     cur.execute("SELECT id FROM "+new_tab+" ORDER BY RANDOM() LIMIT 1")
            #     val = cur.fetchall()[0]
            #     cur.execute("DELETE FROM "+new_tab+" WHERE id = ?",val)

            for id in to_del:
                cur.execute("DELETE FROM "+new_tab+" WHERE id = ?",(id,))

            con.commit()
            begin = time.time()
            # cur.execute("OPTIMIZE TABLE "+ new_tab)
            cur.execute("VACUUM")
            end = time.time() - begin
            f.write(str(end)+'\n')

            con.commit()
            cur.execute("DROP TABLE "+new_tab)


    f.close()