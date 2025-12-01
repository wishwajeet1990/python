"""                
🚦 Access Levels in Python vs C++/Java

+------------------+---------------------+-----------------------+
|     Access        |   Python (Rules)    |   C++ / Java Rules   |
+------------------+---------------------+-----------------------+
| PUBLIC            | name                | public               |
|                   | ✅ Accessible       | ✅ Accessible       |
|                   | everywhere          | everywhere           |
+------------------+---------------------+-----------------------+
| PROTECTED         | _name               | protected            |
|                   | ⚠ Convention only   | ✅ Accessible in    |
|                   | - Allowed in class  | class & subclasses   |
|                   | - Allowed in        | ❌ Not from outside  |
|                   | subclasses          |                      |
|                   | - Allowed outside   |                      |
|                   | (discouraged)       |                      |
+------------------+---------------------+-----------------------+
| PRIVATE           | __name              | private              |
|                   | 🔒 Name Mangling    | ✅ Accessible in     |
|                   | - Inside class only | class only           |
|                   | - Not directly      | ❌ Not from outside  |
|                   | accessible outside  | or subclass          |
|                   | (unless _Class__var)|                      |
+------------------+---------------------+-----------------------+

🔹 Name Mangling Example in Python:
    self.__var  →  self._ClassName__var
"""