#!/usr/bin/env python

from parser import yacc

testScript = '''
defmodule Server do
    const default_host = "192.125.0.2"
    const default_port = "12390"

    tcp = TCPListener()

    def start(host = default_host, port = default_port) do
        tcp.listen(host, port)
        _logStart()
    end

    defp _logStart() do
        print("Server started...\n")
    end
end
'''

tree = yacc.parse(testScript)
import pprint as pp
pp.pprint(tree)
