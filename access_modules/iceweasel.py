#!/usr/bin/python
# MozRepl Plugin must be installed and r-kiosk Plugin for fullscreen
import telnetlib

HOST = 'localhost'
PORT = 4242


def open_url(url):
    tn = telnetlib.Telnet(HOST, PORT)
    cmd = "content.location.href = 'http://{url}'".format(url=url)
    tn.read_until("repl> ")
    tn.write(cmd + "\n")
    tn.write("repl.quit()\n")
    tn.close()
