# -*- coding: utf-8 -*-

import argparse

from ssl_checker import SSLChecker


def main():
    parser = argparse.ArgumentParser(description='SSL Certificate Checker')
    parser.add_argument('hostname')
    args = parser.parse_args()
    SSLChecker(args.hostname)
