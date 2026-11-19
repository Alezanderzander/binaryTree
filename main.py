from binaryTree import *

tree = binaryTree()
students = [("stevj01", "John Stevenson"),("smitj02", "Jane Smith"),
    ("wilst03", "Tim Wilson"),
    ("stevk04", "Kate Stevenson"),
    ("palmk05", "Kate Palmer"),
    ("eastt06", "Tom Eastman"),
    ("greel07", "Laura Green"),
    ("watsm08", "Mike Watson"),
    ("blacs09", "Sally Black"),
    ("ramsm10", "Mark Ramsey")]
for student in students:
    tree.insert(student)
tree.print()
print("----")

tree = binaryTree()
for v in [(1005, "Aoife"), (1002, "Liam"), (1002, "Amy"), (9204, "Rob"), (277, "John"), (61, "Deep")]:   # same key, should use names
    tree.insert(v)
tree.print()
print("----")
