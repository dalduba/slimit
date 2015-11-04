__author__ = 'dal'

from slimit.ast import *

root = Program()
identifier = Identifier("f1")
params = [Identifier("p1"),Identifier("p2")]
elements = [ExprStatement(Assign("=", Identifier("a"),BinOp("+", Identifier("p1"), Identifier("p2")))),
            Return(Identifier("a"))]
funcdecl = FuncDecl(identifier, params, elements)
root._children_list.append(funcdecl)

print(root.to_ecma())
