#!/usr/bin/env python

from parser import yacc

testScript = '''
def hey(hello, hahaha) {
    x = 15 * hello;
    return x;
}

hey(20, "FUCK");
'''

tree = yacc.parse(testScript)
import pprint as pp
pp.pprint(tree)
