import sqlalchemy as db
class DataBase:
    def __init__(self):
        self.engine = db.create_engine('sqlite:///database.db')
        self.connect = self.engine.connect()
        self.metadata = db.MetaData()

    async def create_tables(self):
        global users
        global contact
        
        # metadata.create_all(engine)
    async def add_user(self,data):
        with self.connect:
            insert_query = users.insert().values([
                {'user_id':1109419484,'f.i.o':'Ochilov Akrom Niz','phone_number':'+998997179771'},
            ])
            self.connect.execute(insert_query)

    async def check_user(self,user_id):
        
        user_data = db.select(users).where(users.columns.id==1).values(['user_id'])
        answer = self.connect.execute(user_data)
        return bool(len(answer))
# select_all = db.select(users)
# select_all_q = connect.execute(select_all)
# print(select_all_q.fetchall())

