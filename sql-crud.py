from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql+psycopg2://postgres:1234@localhost/chinook")
base = declarative_base()

# create class based mdel for "Programmer" Table:
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

Session = sessionmaker(db)

# open above created session
session = Session()

base.metadata.create_all(db)

#  creating records on Programmer table

ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

robin_muller = Programmer(
    first_name="Robin",
    last_name="Muller",
    gender="M",
    nationality="South African",
    famous_for="Surfing 〜(￣▽￣〜)"
)


# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(robin_muller)

session.commit()

programmer = session.query(Programmer).filter_by(id=7).first()
programmer.famous_for = "King of the Galaxy"

session.commit()

programmers = session.query(Programmer)
for programmer in programmers:
    print(programmer.id,
    programmer.first_name + " " + programmer.last_name,
    programmer.gender,
    programmer.nationality,
    programmer.famous_for,
    sep = " | "
    )