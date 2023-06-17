import sqlalchemy as db


class DataBase:
    def __init__(self):
        self.engine = db.create_engine('sqlite:///database.db')
        self.connect = self.engine.connect()
        self.metadata = db.MetaData()
        self.users = db.Table('users', self.metadata,
                              db.Column('id', db.Integer, primary_key=True,
                                        unique=True, autoincrement=True),
                              db.Column('user_id', db.Integer, unique=True),
                              db.Column('f.i.o', db.Text),
                              db.Column('phone_number', db.Text),
                              db.Column('lang', db.Text),

                              extend_existing=True
                              )

        self.metadata.create_all(self.engine)
    async def create_tables(self):
        global users
        global contact

    async def add_user(self, data):
        with self.connect:
            insert_query = self.users.insert().values([
                {'user_id': data['user_id'], 'f.i.o':data['f.i.o'],
                    'phone_number':data['phone_number'], 'lang':data['lang']},
            ])
            self.connect.execute(insert_query)
            print(1)
            self.connect.commit()

    async def check_user(self, user_id):

        user_data = db.select(self.users).where(self.users.columns.user_id == user_id)
        answer = self.connect.execute(user_data)
        return bool(answer)
# select_all = db.select(users)
# select_all_q = connect.execute(select_all)
# print(select_all_q.fetchall())
