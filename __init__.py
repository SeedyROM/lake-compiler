#!/usr/bin/env python

from parser import yacc

testScript = '''
defmodule MyModule do
    const name = "Zack"
    def func(x) do
        x = 15
    end

    defp _hiddenFunc() do
        return false
    end
end
defmodule Test do
    const tester = 2.43
end
'''

tree = yacc.parse(testScript)
import pprint as pp
pp.pprint(tree)
