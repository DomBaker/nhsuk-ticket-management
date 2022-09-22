import pytest

from website.models import User, Ticket
from werkzeug.security import generate_password_hash


@pytest.fixture(scope="module")
def new_user():
    user = User(
        email="test@test.com",
        first_name="afirstname",
        last_name="alastname",
        password=generate_password_hash("apassword"),
        is_admin=True,
    )
    return user


@pytest.fixture(scope="module")
def new_ticket():
    ticket = Ticket(
        title="sometitle", description="somedescription", area_of_business="HR"
    )
    return ticket


# @pytest.fixture
# def client():
#     db_fd, website.app.config["DATABASE"] = tempfile.mkstemp()
#     website.app.config["TESTING"] = True

#     with website.app.test_client() as client:
#         with website.app.app_context():
#             website.init_db()
#         yield client

#     os.close(db_fd)
#     os.unlink(website.app.config["DATABASE"])
