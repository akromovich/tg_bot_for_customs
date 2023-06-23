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
            self.connect.commit()

    async def check_user(self, user_id):
        with self.engine.connect()  as connect:
            user_data = db.select(self.users).where(self.users.columns.user_id == user_id)
            answer = connect.execute(user_data)
            return bool(len(answer.fetchall()))


    async def list_users_db(self):
        with self.engine.connect()  as connect:
            res=db.select(self.users)
            result = connect.execute(res)
            # await message.answer(f'{i[0]}.{i[1]} {i[2]} \nдолжность:{i[3]}\n{i[4]}',reply_markup=kb_admin.del_or_send)
            g = []
            for i in result.fetchall():
                a= f'id:{i[0]}\ntg_id: <code>{i[1]}</code>\nF.I.O: {i[2]}\ntelefon nomeri: <code>{i[3]}</code>\ntanlagan tili: {i[4]}\n_____________\n'
                g.append(a)
            return ''.join(g)

    async def db_settings(self,user_id):
        with self.engine.connect() as connect:
            res = db.select(self.users).where(self.users.columns.user_id == user_id)
            result = connect.execute(res)
            for i in result.fetchall():
                return f'F.I.O: {i[2]}\nTelefon raqami: {i[3]}\nTil: {i[4]}'
# select_all = db.select(users)
# select_all_q = connect.execute(select_all)
# print(select_all_q.fetchall())
