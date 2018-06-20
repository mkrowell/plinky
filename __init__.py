#!/usr/bin/env python
'''
.. module:: plinky
    :language: Python Version 2.7
    :platform: Windows 10
    :synopsis: manage SSH nonnections with Python

.. moduleauthor:: Jason Thorpe and Maura Rowell <mkrowell@uw.edu>
'''


from subprocess import  Popen, PIPE
from socket import socket,AF_INET,SOCK_STREAM

__plink__ = None

def test_connection(port, host = "127.0.0.1"):
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((host,port))
        return True
    except:
        return False
    finally:
        s.close()

def start(profile):
    global __plink__
    if __plink__ is not None:
        if __plink__.poll() is None:
            # plink is already running
            return
        else:
            __plink__ = None
    try:
        p = Popen(['plink.exe','-N','-load',profile],stdin = PIPE)
    except OSError as err:
        msg =  "Failed to start plink.  Please make sure plink.exe is on the system path."
        print msg
        err.message =  msg + "\n" + err.message
        p.kill()
        raise err
    except Exception as err:
        print "plink failed to start"
        p.kill()
        raise err
    __plink__ = p


def stop():
    global __plink__
    if __plink__ is not None:
        if __plink__.poll() is None:
            # plink is running
            __plink__.kill()
        __plink__ = None
