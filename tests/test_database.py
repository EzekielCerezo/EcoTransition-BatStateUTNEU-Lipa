import unittest
from app import create_app, db
from app.models import User, Signatory


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_creation(self):
        with self.app.app_context():
            user = User(
                email="test@ecotransition.com", password="testpassword", role="Guest"
            )
            db.session.add(user)
            db.session.commit()

            fetched_user = User.query.filter_by(email="test@ecotransition.com").first()
            self.assertIsNotNone(fetched_user)
            self.assertEqual(fetched_user.email, "test@ecotransition.com")

    def test_signatory_creation(self):
        with self.app.app_context():
            user = User(
                email="signatory@ecotransition.com",
                password="testpassword",
                role="Signatory",
            )
            db.session.add(user)
            db.session.commit()

            fetched_user = User.query.filter_by(
                email="signatory@ecotransition.com"
            ).first()
            self.assertIsNotNone(fetched_user)
            self.assertEqual(fetched_user.role, "Signatory")

    def test_signatory_to_organization_relationship(self):
        with self.app.app_context():
            user = User(
                email="adviser@ecotransition.com",
                password="testpassword",
                role="Signatory",
            )
            db.session.add(user)
            db.session.commit()

            signatory = Signatory(
                user_id=user.id,
                name="John Doe",
                designation="Adviser",
                department="CS",
            )
            db.session.add(signatory)
            db.session.commit()

            fetched_signatory = Signatory.query.filter_by(user_id=user.id).first()
            self.assertIsNotNone(fetched_signatory)
            self.assertEqual(fetched_signatory.name, "John Doe")
