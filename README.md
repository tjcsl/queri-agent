mhacksiv-agent
==============

The Queri Agent is a piece of client software intended to be run anywhere that you would want to monitor. By default, it runs on port 5000, and that is where the Queri server will look for it. You can give Queri either your IP address, or your domain name.

Setup
-----

To set up the Queri Agent, either create a virtualenv and run the below, or change to root and run the below, to install the necessary python modules:
```pip install -r requirements.txt```.
Then, simply start up the server with
```python rest_server.py```.
Make sure that port 5000 is open in your firewall, and that your computer either has a public IP, or port 5000 is port forwarded to your computer. You should then be good to go.
