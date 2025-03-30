import sqlite3 as sq
import base_table_gen

import tests

con = sq.connect(r"/mnt/d/DB_tests/test.db")
cur = con.cursor()

# base_table_gen.generate_data(1000,cur,'T1')
# base_table_gen.generate_data(10000,cur,'T2')
# base_table_gen.generate_data(100000,cur,'T3')
# base_table_gen.generate_data(1000000,cur,'T4')


# tests.val_DELETE_TESTS(cur)
# tests.key_DELETE_TESTS(cur)

# tests.key_UPDATE_TESTS(cur)
# tests.val_UPDATE_TESTS(cur)

# tests.val_SELECT_TESTS(cur)
# tests.key_SELECT_TESTS(cur)

# tests.INSERT_TESTS(cur)

# tests.mask_SELECT_TESTS(cur)

# tests.DELETE_TESTS(cur)
# tests.UPDATE_TESTS(cur)
# tests.SELECTKEY_TEST(cur)
# tests.SELECTNOKEY_TEST(cur)

tests.litle_OPTIMIZE_TESTS(cur,con)


con.commit()


con.close()