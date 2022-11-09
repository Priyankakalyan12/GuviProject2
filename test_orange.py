import pytest
import orange

o = orange.Orange()
url = "https://opensource-demo.orangehrmlive.com/"
userName = "Admin"
pwd = "admin123"
fname = "Prateek"
mname = "Raj"
lname = "Purohit"
newUsername = "Prateek1990"
newPwd = "Prateek1990#"


# test for login
@pytest.mark.first
def test_login():
    o.login(url, userName, pwd)
    assert o.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"


# test to add new Employee
@pytest.mark.second
def test_addNewEmployee():
    o.addNewEmployee(fname, mname, lname)


# test to add new Employee As Admin
@pytest.mark.third
def test_addNewUserInAdmin():
    o.addNewEmployeeInAdmin(fname, newUsername, newPwd)

# test to search User in Admin Section
@pytest.mark.forth
def test_searchUserInAdminSection():
    assert o.searchUserInAdminSection(newUsername).text == newUsername

# test to logout from portal
@pytest.mark.fifth
def test_logout():
    o.logout()
    assert o.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# test for login
@pytest.mark.sixth
def test_newuserlogin():
    o.login(url, newUsername, newPwd)
    assert o.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewMyDetails"
    o.driver.close()
