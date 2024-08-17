#!/usr/bin/env python3
"""
Main file
"""
from pprint import pprint

Server = __import__('2-hypermedia_pagination').Server

server = Server()

pprint(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print("---")
print(server.get_hyper(3000, 100))
