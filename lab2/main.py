import sqlite3 as sq
import base_table_gen

import tests

con = sq.connect(r"/mnt/d/DB_tests/test.db")
cur = con.cursor()

# base_table_gen.generate_data(1000,cur,'T1')
# base_table_gen.generate_data(10000,cur,'T2')
# base_table_gen.generate_data(100000,cur,'T3')
# base_table_gen.generate_data(1000000,cur,'T4')

# tests.INSERT_TESTS(cur)
# tests.DELETE_TESTS(cur)
# tests.UPDATE_TESTS(cur)
tests.SELECTKEY_TEST(cur)
tests.SELECTNOKEY_TEST(cur)

con.commit()


con.close()