from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Todos

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        sample1 = Todos(task = "Perform tests")
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('todo'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Perform tests', response.data)

class TestAdd(TestBase):

    def test_add_post(self):
        response = self.client.post(
            url_for('add'),
            data = dict(task = "Shower"),
            follow_redirects=True
        )
        self.assertIn(b'Shower',response.data)