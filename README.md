# WebAutomation
This repository is mainly for storing my  automation code, which fill the health report  every day.\
This code is currently only for zju's site. If I have time I will add some other school's site.
![structure](img/structure.PNG)
Above is the rough frame work.And below will teach you how to automate this work through a daemon.
![automation](img/automate.PNG)

### Steps

1. ```git clone https://github.com/woshiZS/WebAutomation```(国内克隆速度太慢的自行搜索淘宝源进行加速):jack_o_lantern:
2. run /source/init.sql in your mysql client.
3. Insert your information into your tables.
4. run ```python3 main.py```
5. For fully automation you need crontab or windows task scheduler.

### Tips
* If you don't want to use database, you could store username and password in a local file(not recommend for security reasons)
* Remember to add headingless options to webdriver when you run this program under systems with no graphic interface.
* Some times the website will request for a https licence otherwise it will return ssl error,Just ignore it and it has no effects on our program cause the server end will not reset the connection like google :laughing:.
* If there is any problem, please raise an issue to inform me of that.
* Update(0927), the same code runs much faster on my centos server than on windows computer.
* Sometime this script will fail if the port is banned on your pc or server(like 9221 port I used before).
