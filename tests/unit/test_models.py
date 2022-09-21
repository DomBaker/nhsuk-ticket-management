def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN the email, first name, last name, password and admin status
    are correctly defined
    """

    assert new_user.email == "test@test.com"
    assert new_user.first_name == "afirstname"
    assert new_user.last_name == "alastname"
    assert new_user.password != "apassword"
    # 1 = True, 2 = False
    assert new_user.is_admin == 1


def test_new_ticket(new_ticket):
    """
    GIVEN a Ticket model
    WHEN a new Ticket is created
    THEN the title, description and area of business
    are correctly defined
    """

    assert new_ticket.title == "sometitle"
    assert new_ticket.description == "somedescription"
    assert new_ticket.area_of_business == "HR"
