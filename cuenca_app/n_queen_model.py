from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class NQueen(Base):
    __tablename__ = "nqueen"
    id = Column(Integer, primary_key=True)
    n_queen = Column(String)
    n_solution = Column(String)

    def __repr__(self):
        return "N Queen -> {}, N Solution -> {}".format(self.n_queen, self.n_solution)
