# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2019/5/28 11:34 PM'

from os.path import realpath, dirname
import json


def get_config(name):
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())