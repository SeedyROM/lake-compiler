# lake-compiler

## What is it? 👿
It's a simple attempt at making a compiler, I'm only at the parsing stage though. 💕

### Here's an example program:
```
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
```

### Here's the parse tree that's generated!

```
('MODULE',
 'Server',
 ('DO_BLOCK',
  ((((('CONST_ASSIGN', 'default_host', ('VAL_CONST', '"192.125.0.2"')),
      ('CONST_ASSIGN', 'default_port', ('VAL_CONST', '"12390"'))),
     ('ASSIGN', 'tcp', ('FUNC_CALL', 'TCPListener', ('ARGS', ())))),
    ('FUNC_DEF',
     'start',
     ('ARGS',
      (('ARG', ('ASSIGN', 'host', ('VAL_VAR', 'default_host'))),
       ('ARG', ('ASSIGN', 'port', ('VAL_VAR', 'default_port'))))),
     ('DO_BLOCK',
      ((('VAL_VAR', 'tcp'),
        ('FUNC_CALL',
         'listen',
         ('ARGS',
          (('ARG', ('VAL_VAR', 'host')), ('ARG', ('VAL_VAR', 'port')))))),
       ('FUNC_CALL', '_logStart', ('ARGS', ())))))),
   ('PRIV_FUNC_DEF',
    '_logStart',
    ('ARGS', ()),
    ('DO_BLOCK',
     ('FUNC_CALL',
      'print',
      ('ARGS', ('ARG', ('VAL_CONST', '"Server started...\n"')))))))))
```

#### This is so rough, but it's been fun reading "Compilers: Principles, Techniques and Tools"

# 👍
