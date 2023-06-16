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
        users = db.Table('users',self.metadata,
            db.Column('id',db.Integer,primary_key=True,unique=True,autoincrement=True),
            db.Column('user_id',db.Integer,unique=True),
            db.Column('f.i.o',db.Text),
            db.Column('phone_number',db.Text),extend_existing=True
        )
        user_data = db.select(users).where(users.columns.user_id==user_id)
        answer = self.connect.execute(user_data)
        return bool(answer)
# select_all = db.select(users)
# select_all_q = connect.execute(select_all)
# print(select_all_q.fetchall())

