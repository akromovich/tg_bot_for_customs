import sqlalchemy as db


class DataBase:
    def __init__(self):
        self.engine = db.create_engine("sqlite:///database.db")
        self.connect = self.engine.connect()
        self.metadata = db.MetaData()
        self.users = db.Table(
            "users",
            self.metadata,
            db.Column(
                "id", db.Integer, primary_key=True, unique=True, autoincrement=True
            ),
            db.Column("user_id", db.Integer, unique=True),
            db.Column("full_name", db.Text),
            db.Column("phone_number", db.Text),
            db.Column("lang", db.Text),
            extend_existing=True,
        )

        self.contacts = db.Table(
            "contact_us",
            self.metadata,
            db.Column(
                "id", db.Integer, primary_key=True, unique=True, autoincrement=True
            ),
            db.Column("phone_number_1", db.Text),
            db.Column("phone_number_2", db.Text),
            extend_existing=True,
        )

        self.about_us = db.Table(
            "about_us",
            self.metadata,
            db.Column(
                "id", db.Integer, primary_key=True, unique=True, autoincrement=True
            ),
            db.Column("about_us", db.Text),
            extend_existing=True,
        )

        self.products = db.Table(
            'products',
            self.metadata,
            db.Column('id',db.Integer,primary_key=True,autoincrement=True),
            db.Column('name',db.Text,nullable=False),
            db.Column('decs',db.Text,nullable=False),
            db.Column('price',db.Integer),
            db.Column('category',db.Text),
            db.Column('photo',db.Text),
        )

        self.metadata.create_all(self.engine)
        self.connect.commit()
    async def create_tables(self):
        global users
        global contact

    async def add_user(self, data):
        with self.connect:
            insert_query = self.users.insert().values(
                [
                    {
                        "user_id": data["user_id"],
                        "full_name": data["full_name"],
                        "phone_number": data["phone_number"],
                        "lang": data["lang"],
                    },
                ]
            )
            self.connect.execute(insert_query)
            self.connect.commit()

    async def check_user(self, user_id):
        with self.engine.connect() as connect:
            user_data = db.select(self.users).where(
                self.users.columns.user_id == user_id
            )
            answer = connect.execute(user_data)
            return bool(len(answer.fetchall()))

    async def list_users_db(self):
        with self.engine.connect() as connect:
            res = db.select(self.users)
            result = connect.execute(res)
            # await message.answer(f'{i[0]}.{i[1]} {i[2]} \nдолжность:{i[3]}\n{i[4]}',reply_markup=kb_admin.del_or_send)
            g = []
            for i in result.fetchall():
                a = f"id:{i[0]}\ntg_id: <code>{i[1]}</code>\nF.I.O: {i[2]}\ntelefon nomeri: <code>{i[3]}</code>\ntanlagan tili: {i[4]}\n_____________\n"
                g.append(a)
            return "".join(g)

    async def db_settings(self, user_id):
        with self.engine.connect() as connect:
            res = db.select(self.users).where(self.users.columns.user_id == user_id)
            result = connect.execute(res)
            for i in result.fetchall():
                return (
                    f"F.I.O: {i[2]}\nTelefon raqami: <code>{i[3]}</code>\nTil: {i[4]}"
                )

    async def db_contacts(self):
        with self.engine.connect() as connect:
            res = db.select(self.contacts)
            result = connect.execute(res)
            # count = 0
            for i in result.fetchall():
                return f"Biz bilan bog`lanish uchun :\n<code>{i[1]}</code>\n<code>{i[2]}</code>\nraqamlariga qo`ng`iroq qilishingiz mumkin"

    async def db_about_us(self):
        with self.engine.connect() as connect:
            res = db.select(self.about_us)
            result = connect.execute(res)
            # count = 0
            for i in result.fetchall():
                return i[1]

    async def edit_fio(self, id,new_fio):
        print(id,new_fio)
        with self.engine.connect() as connect:
            res = db.update(self.users).where(self.users.columns.user_id==id).values(full_name=new_fio)
            connect.execute(res)
            print(1)
            connect.commit()
    
    async def edit_phone_number(self, id,new_phone_number):
        print(id,new_phone_number)
        with self.engine.connect() as connect:
            res = db.update(self.users).where(self.users.columns.user_id==id).values(phone_number=new_phone_number)
            connect.execute(res)
            print(1)
            connect.commit()

    async def edit_lang(self, id,new_lang):
        with self.engine.connect() as connect:
            res = db.update(self.users).where(self.users.columns.user_id==id).values(lang=new_lang)
            connect.execute(res)
            print(1)
            connect.commit()
  
    async def add_product(self,data):
        with self.engine.connect() as connect:
            insert_query = self.products.insert().values(
                [
                    {
                        'name':data['name'],
                        'decs':data['desc'],
                        'price':data['price'],
                        'category':data['category'],
                        'photo':data['photo_id'],
                    }
                ]
            )
            self.connect.execute(insert_query)
            self.connect.commit()

    async def show_all_product(self):
        with self.engine.connect() as connect:
            res = db.select(self.products)
            result = connect.execute(res)
            # count = 0
            return result.fetchall()
        
    async def category(self,category):
        with self.engine.connect() as connect:
            res = db.select(self.products).where(self.products.columns.category==category)
            result = connect.execute(res)
            # count = 0
            return result.fetchall()
            
    async def kb_category(self):
        with self.engine.connect() as connect:
            res = db.select(self.products)
            result = connect.execute(res)
            # count = 0
            return result.fetchall()

    async def insert_about_us(self,data):
        with self.engine.connect() as connect:
            res = db.update(self.about_us).where(self.about_us.columns.id==1).values(about_us=data)
            self.connect.execute(res)
            self.connect.commit()

    async def show_all_catalog(self):
        with self.engine.connect() as connect:
            res = db.select(self.products)
            result = connect.execute(res)
            # count = 0
            return result.fetchall()

# select_all = db.select(users)
# select_all_q = connect.execute(select_all)
# print(select_all_q.fetchall())
