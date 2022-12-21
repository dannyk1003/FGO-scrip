import sqlite3
import json

class historyDB:
    def __init__(self, path):
        self.path = path
        self.createTable()
        self.battleSkill_init()
        self.insert('first', self.supporter, self.battleSkill)

    def _connect(self):
        self.conn = sqlite3.connect(rf'{self.path}\history\history.db')
        self.c = self.conn.cursor()


    def _close(self):
        self.conn.commit()
        self.conn.close()


    def battleSkill_init(self):
        with open(rf'{self.path}\Configs\support_init.json','r') as fr:
            self.supporter = json.load(fr)
                

        with open(rf'{self.path}\Configs\battleSkill_init.json','r') as fr:
            self.battleSkill = json.load(fr)


    def dropTable(self):
        self._connect()      

        self.c.execute(
            '''
            drop table if exists history
            '''
        )

        self._close()


    def createTable(self):
        self._connect()       

        self.c.execute(
            '''
            create table if not exists history(
                name text primary key not null,
                Support text not null,
                battleSkill text not null
            )

            '''
        )

        self._close()


    def select(self):
        self._connect()
        DB_data = dict()

        cursor = self.c.execute(
            '''
            select * from history
            '''
        )

        for row in cursor:
            print ("name = ", row[0])
            print ("Support = ", row[1])
            print ("battleSkill = ", row[2], "\n")
            # DB_data.append({'name': row[0], 'Support': row[1], 'battleSkill': row[2]})
            DB_data.update({row[0]:{'Support': row[1], 'battleSkill': row[2]}})



        self._close()
        return DB_data


    def insert(self, name, Support, battleSkill):
        self._connect()

        try:

            self.c.execute(
                f'''
                insert into history (name, Support, battleSkill)
                values ("{name}", "{Support}", "{battleSkill}");
                '''
            )
        except sqlite3.IntegrityError:
            print('used name, plz change one \n')

        self._close()

    
    def delete(self, name):
        self._connect()

        self.c.execute(
            f'''
            delete from history where name="{name}";
            '''
        )

        self._close()




