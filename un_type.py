import ast
import astunparse

import pathlib


class DocString:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return self.string


class TypeHintRemover(ast.NodeTransformer):

    def visit_FunctionDef(self, node):
        # print(ast.get_docstring(node))
        # remove the return type defintion
        node.returns = None
        # remove all argument annotations
        if node.args.args:
            for arg in node.args.args:
                arg.annotation = None
        return node

    def visit_Import(self, node):
        new_names = []
        for n in node.names:
            if n.name != "typing":
                new_names.append(n)
        node.names = new_names
        return node if node.names else None

    def visit_ImportFrom(self, node):
        return node if node.module != "typing" else None

    def visit_Assign(self, node):
        if isinstance(node.value, ast.Call):
            if node.value.func.id == "TypeVar":
                return None
        return node

    def visit_Expr(self, node):
        if not isinstance(node.value.s, DocString):
            nv = node.value.s.rstrip("'").lstrip("'")
            node.value.s = DocString(f'"""{nv}"""')
        return node


class DocStringInitPreserver(ast.NodeTransformer):

    def visit_FunctionDef(self, node):
        if node.name == "__init__":
            ds = node.body[0]
            if isinstance(ds, ast.Expr) and isinstance(ds.value, ast.Str):
                nv = ds.value.s.rstrip("'").lstrip("'")
                ds.value.s = DocString(f'"""{nv}"""')
        return node


if __name__ == "__main__":
    with open("cripy/protocol/network/types.py", "r") as iin:
        source = iin.read()
    parsed_source = ast.parse(source, "cripy/protocol/network/types.py")
    print(astunparse.dump(parsed_source))
    transformed = TypeHintRemover().visit(parsed_source)
    transformed = DocStringInitPreserver().visit(parsed_source)
    # convert the AST back to source code
    with open("it.py", "w") as out:
        out.write(astunparse.unparse(transformed))
