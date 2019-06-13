from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
engine = create_engine('sqlite:///sqlite/sales.db')#, echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship

from sqlalchemy.orm import sessionmaker

class Customer(Base):
   __tablename__ = 'customers'

   id = Column(Integer, primary_key = True)
   name = Column(String)
   address = Column(String)
   email = Column(String)
   invoices = relationship("Invoice", back_populates = "customer")

class Invoice(Base):
   __tablename__ = 'invoices'
   
   id = Column(Integer, primary_key = True)
   custid = Column(Integer, ForeignKey('customers.id'))
   invno = Column(Integer)
   amount = Column(Integer)
   customer = relationship("Customer", back_populates = "invoices")

#Customer.invoices = relationship("Invoice", order_by = Invoice.id, back_populates = "customer")

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()

row = Customer(name='Joe', address='13 Norton Lees RD', email='jdineen21@gmail.com')
row.invoices = [Invoice(invno = 10, amount = 15000), Invoice(invno = 14, amount = 3850)]
session.add(row)
result = session.query(Customer).join(Invoice)
for row in result:
   for inv in row.invoices:
      print (row.id, row.name, inv.invno, inv.amount)

session.commit()