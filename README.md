# **Protolingo**

## **Protolingo** is a powerful meta-language framework for creating custom configuration DSL(s) with YAML.

> ## With Protolingo your custom DSL will support:
> 1. **Custom tags**
> 2. **Topological sorting**
> 3. **A powerful templating language**
> 4. **Implict state management**
>_____________________________________________________

## To get started experimenting with your own custom DSL create the following directory structure
```
--myDSL
    |_dialects
    |   |_ __init__.py
    |   |_ echo.py
    |_ __init__.py
    |_ test.py
    |_ test.yaml
```

##  Install **Protolingo** into your virtual environment
```bash
pip install protolingo
```

##  Declare a new tag by placing the following code into the **echo.py** file in your **dialects** directory
```python
import sys
from protolingo.yaml.YAMLExpression import YAMLExpression

class Echo(YAMLExpression):
    yaml_tag = u'!echo'

    def __init__(self, id, depends_on, message, output=None, exit=None, exitCode=None):
        super(YAMLExpression, self).__init__(id, depends_on, output, exit, exitCode)
        self.message = message
        

    def exec(self,**kwargs):
        try:
            print(self.message)
            sys.exit(0)
        except Exception as e:
            raise
 
    def __repr__(self):
        return "%s(id=%r)" % (
            self.__class__.__name__, self.id)
```

## Use your new tags in the **test.yaml** configuration in your project root
```yaml
-   config:
      exit_on_error : false
-   !echo:
    id: this_id_must_be_unique
    message: "{{demo}}"
    depends_on: []
```

## In your **test.py** import **protolingo** and bootstrap your environment
```python
import sys
from protolingo import __main__ as module

if __name__ == "__main__":
    module.main(sys.argv[1:])

```

## Run the following command to test your work
```bash
$ python test.py test.yaml -params '{"demo":"Hello world"}'
********************************************************
*                this_id_must_be_unique
********************************************************
Hello world

```
