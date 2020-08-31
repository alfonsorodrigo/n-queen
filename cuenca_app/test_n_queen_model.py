import unittest
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from n_queen_model import NQueen, Base
from n_queen import SolveNQueen


class ORMCreateSchemaTestCase(TestCase):
    def setUp(self) -> None:
        self.engine = create_engine("sqlite:///:memory:")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_create_schema(self):
        Base.metadata.create_all(self.engine)
        self.assertTrue(Base.metadata.tables[NQueen.__tablename__].exists(self.engine))


class ORMCreateExampleDataTestCase(TestCase):
    def setUp(self) -> None:
        self.engine = create_engine("sqlite:///:memory:")
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
