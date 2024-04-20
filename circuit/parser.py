import re


def parse_verilog(filename):
    # map from wire name -> (gate, name of the wires that are inputs to the gate...)
    circuit = {}
    inputs = []
    outputs = []

    filecontents = open(filename, 'r').read()
    for l in filecontents.split(';'):
        if not l:
            continue
        l = re.sub(r"/\*.*?\*/", '', l, flags=re.DOTALL)
        l = re.sub(r'//.*$', '', l, flags=re.MULTILINE)
        l = l.strip()
        tokens = l.split(' ')
        if tokens[0] == 'module':
            continue
        if tokens[0] == 'endmodule':
            continue
        tokens[-1] = tokens[-1].rstrip(';')
        if tokens[0] in ('wire', 'output', 'input'):
            if len(tokens) != 2:
                raise ValueError('unsupported statement:', l)
            typ, name = tokens
            if typ == 'input':
                inputs.append(name)
            elif typ == 'output':
                outputs.append(name)
            circuit[name] = None
        elif tokens[0] == 'assign':
            if tokens[2] != '=':
                raise ValueError('unsupported statement:', l)
            lhs = tokens[1]
            if '[' in lhs or ':' in lhs:
                raise ValueError('unsupported statement:', l)
            rhs = [*filter(bool, re.split(r'\b', ''.join(tokens[3:])))]

            match rhs:
                case['~', var]:
                    rhs = ('not', var)
                case[var1, '&', var2]:
                    rhs = ('and', var1, var2)
                case[var1, '|', var2]:
                    rhs = ('or', var1, var2)
                case[var1, '^', var2]:
                    rhs = ('xor', var1, var2)
                case[var1, '|~(', var2, ')']:
                    rhs = ('ornot', var1, var2)
                case[var1, '&~(', var2, ')']:
                    rhs = ('andnot', var1, var2)
                case['~(', var1, '&', var2, ')']:
                    rhs = ('nand', var1, var2)
                case['~(', var1, '|', var2, ')']:
                    rhs = ('nor', var1, var2)
                case['~(', var1, '^', var2, ')']:
                    rhs = ('xnor', var1, var2)
                case['1', "'", val]:
                    if not re.match(r'h(0|1)', val):
                        raise ValueError('unsupported statement:', l)
                    rhs = ('const_' + val[1],)
                case _:
                    raise ValueError('unsupported statement:', l)

            circuit[lhs] = rhs
            for var in rhs[1:]:
                if var not in circuit:
                    raise ValueError('undefined variable:',
                                     var, 'in statement', l)
        else:
            raise ValueError('unsupported statement:', l)
    for wire, value in circuit.items():
        if not value and wire not in inputs:
            raise ValueError('wire was never assigned:', wire)
    return circuit, inputs, outputs
