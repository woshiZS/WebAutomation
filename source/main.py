import getpass
from connect_db import MyDataBase
from auto_operations import MyDriver

host = input("Please input your host ip address.\n")
user = input("Please input your user name\n")
password = getpass.getpass("Please input your database password")
database = input("Please input your target database name\n")

my_db = MyDataBase(host,user,password,database)
result = my_db.data()

# REMEMBER to download a webdriver according to your browser
# You can specify a path on your own pc or server
PATH = "E:\CS_learnig\Snake-Python-tutorial-\WebBot\chromedriver.exe"

for item in result:
    driver = MyDriver(PATH)
    driver.login(item[0],item[1])
    driver.fill_forms(item)
    driver.quit()

# Thus end
