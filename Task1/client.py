from Task1.DocumentCreator import DocumentCreator
from typing import Type

objNames=['pdf','excel','word']

for name in objNames:
    res=DocumentCreator.create_document(name)
    if res:
        print(res.objType)