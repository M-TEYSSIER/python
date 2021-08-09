#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser()

#Reply first arg
"""
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
"""

parser.add_argument("square", help="display a square of a given number", type=int)
args=parser.parse_args()
print(args.square**2)