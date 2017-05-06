#!/usr/bin/env python

from parser import yacc

testScript = '''
defmodule Server do
    def examine(str) do
        if(str == "fuck") do
            print("You said fuck!")
        else if(lol) do
            return "murder me"
        end
    end
end
'''

tree = yacc.parse(testScript)
import pprint as pp
pp.pprint(tree)
