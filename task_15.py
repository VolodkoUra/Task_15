from sqlalchemy import create_engine, Column, String, Integer, FLOAT, MetaData, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

"""
Создать таблицу продуктов.
Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для продуктов.
Создать пользовательский интерфейс.
"""
engine = create_engine('sqlite:///ProductDB.db', echo=True)
base = declarative_base()
session = sessionmaker(bind=engine)()

metadata = MetaData()

"""product = Table('products', metadata, 
                Column('id', Integer, primary_key=True),
                Column('name_product', String),
                Column('price', FLOAT),
                Column('count', FLOAT),
                Column('Comment', String))

metadata.create_all(engine)"""


class Product(base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name_product = Column(String)
    price = Column(FLOAT)
    count = Column(FLOAT)
    comment = Column(String)

    @classmethod
    def __init__(cls, name_product, price, count, comment):
        cls.name_product = name_product
        cls.price = price
        cls.count = count
        cls.comment = comment

    #@classmethod
    def __repr__(self):
        return "<Product('%s', '%f', '%f', '%s')>" % \
               (self.name_product, self.price, self.count, self.comment)

    @classmethod
    def create_prod(cls, name, price, count, comment=""):
        p = Product(name, price, count, comment)
        session.add(p)
        session.commit()

    @classmethod
    def delete_prod(cls, id):
        session.query(Product).filter_by(Product.id == id).delete()
        session.commit()

    """def update_prod_name(self, name_old, name_new):
        session.query(Product).filter(Product.name_product == name_old).update({Product.name_product: name_new},
                                                                              synchronize_session=False)
        session.commit()"""

    @classmethod
    def read_prod(cls):
        s = input("Введите название продукта, которое хотите прочитать: ")
        x = session.query(Product).filter(Product.name_product == s).all()
        print(x)
    @classmethod
    def update_prod(cls, id):
        print("1.Название продукта\n2.Цена\n3.Количество\n4.Выход\n")
        s = input("Введите параметр который хотите изменить: ")
        if s == "1":
            n_new = input("Введите новое название продукта: ")
            session.query(Product).filter(Product.id == id).update(
                {Product.name_product: n_new},
                synchronize_session=False)
            session.commit()

        if s == "2":
            p_name = input("Введите название продукта, цену которого хотите изменить: ")
            p_new = input("Введите новую цену продукта: ")
            session.query(Product).filter(Product.id == id).update(
                {Product.price: p_new},
                synchronize_session=False)
            session.commit()

        if s == "3":
            c_name = input("Введите название продукта, количество которого хотите изменить: ")
            c_new = input("Введите новое название продукта: ")
            session.query(Product).filter(Product.id == id).update(
                {Product.count: c_new},
                synchronize_session=False)
            session.commit()

        if s == "4":
            return "Выход из метода изменения цены"

        else:
            print("Введите другое значение")

    """def update_prod_price(self, price_old, price_new):
        session.query(Product).filter(Product.name_product == price_old and ).update({Product.name_product: price_new},
                                                                              synchronize_session=False)
        session.commit()
    
    def update_prod_count(self, count_old, count_new):
        session.query(Product).filter(Product.name_product == count_old).update({Product.name_product: count_new},
                                                                              synchronize_session=False)
        session.commit()
        
    def update_prod_name(self, name_old, name_new):
        session.query(Product).filter(Product.name_product == name_old).update({Product.name_product: name_new},
                                                                              synchronize_session=False)"""


base.metadata.create_all(engine)

"""tomat = Product('Tomat', 3.5, 8.5, "Свежий")


cucumber = Product('Огурец', 1.5, 10, "")


banana = Product('Банан', 3, 10, "")


bread = Product('Хлеб', 2, 4, "")


rice = Product('Рис', 3, 2, "")


cheese = Product('Сыр', 15, 6, "")


potato = Product('Картофель', 2, 15, "")


carrot = Product('Морковь', 1.5, 17, "")


sugar = Product('Сахар', 1.5, 5, "")


beer = Product('Пивко', 2, 20, "")"""

"""session.commit()"""

"""session.query(Product).filter_by().delete()
session.commit()
"""

"""session.query(Product).update({Product.price: 4}, synchronize_session = False)
session.commit()
session.rollback()"""
"""session.commit()"""

"""session.rollback()"""

"""session.query(Product).filter(Product.name_product == 'Пивко').update({Product.price: 20}, synchronize_session = False)
session.commit()"""


x= session.query(Product).filter_by(name_product = "Рис").first()
print(x)
