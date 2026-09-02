

from sqlalchemy import create_engine, String,select,and_,or_
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase,Session

engine = create_engine("sqlite:///test.db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key = True)
    name : Mapped[str] = mapped_column(String(100))
    age : Mapped[int]

Base.metadata.create_all(engine)


with Session(engine) as session:
    # users = session.execute(
    #     select(User)
    # ).scalars().all()

    # users = session.execute(
    #     select(User).where(User.age == 19)
    # ).scalars().all()

    # user = session.get(User , 1)
    # print(user.name)

    # user = session.execute(
    #     select(User).where(User.id == 1)
    # ).scalars().all()
    # for user in user:
    #     print(user.name)

    # user = session.get(User,1)
    # user.age = 21
    # session.commit()

    # user = session.get(User,2)
    # session.delete(user)
    # session.commit()

    # user1 = User(name = "Ali" , age = 24)
    # user2 = User(name = "Babak" , age = 37)
    # user3 = User(name = "Mmd" , age = 25)
    # user4 = User(name = "Hasan" , age = 14)
    # session.add(user1)
    # session.add(user2)
    # session.add_all([user1,user2,user3,user4])
    # session.commit()


    # user = session.execute(
    #     select(User).where(and_(User.name == "Ali",User.age > 20))
    # ).scalars().all()
    # for users in user:
    #     print( users.id)


    # users = session.execute(select(User).where(or_(User.age == 20, User.age == 30))
    # ).scalars().all()
    # for user in users:
    #     print(user.name)


    # users = session.execute(select(User).order_by(User.age.desc())
    # ).scalars().all()
    # for user in users:
    #     print(user.age)


    # users = session.execute(select(User).limit(2)
    # ).scalars().all()
    # for user in users:
    #     print(user)


    statement = select(User).where(User.age > 0)
    users = session.execute(statement).scalars().all()
    for user in users:
        print(f" id : {user.id} , name : {user.name} , age : {user.age} ")





