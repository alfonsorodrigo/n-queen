import os
import time
import unittest
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from n_queen_model import NQueen, Base
from n_queen import SolveNQueen


DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")


class ORMCreateSchemaTestCase(TestCase):
    def setUp(self) -> None:
        while True:
            try:
                self.engine = create_engine(
                    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
                )
                self.engine.execute("select 1")
            except OperationalError:
                print("Waiting for database...")
                time.sleep(1)
            else:
                break
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_create_schema(self):
        Base.metadata.create_all(self.engine)
        self.assertTrue(Base.metadata.tables[NQueen.__tablename__].exists(self.engine))


class ORMCreateExampleDataTestCase(TestCase):
    def setUp(self) -> None:
        while True:
            try:
                self.engine = create_engine(
                    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
                )
                self.engine.execute("select 1")
            except OperationalError:
                print("Waiting for database...")
                time.sleep(1)
            else:
                break
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_create_example_four_queen(self):
        n_queen = 4
        solution = SolveNQueen(n_queen).solve()
        n_queen_saved = NQueen(n_queen=n_queen, n_solution=solution)
        self.assertEqual(n_queen_saved.n_solution, 2)

    def test_create_example_eight_queen(self):
        n_queen = 8
        solution = SolveNQueen(n_queen).solve()
        n_queen_saved = NQueen(n_queen=n_queen, n_solution=solution)
        self.assertEqual(n_queen_saved.n_solution, 92)


if __name__ == "__main__":
    unittest.main()
