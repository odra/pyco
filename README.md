# pyco

**Only works on Python >= 3**

Python library to manipulate code and function objects.

## Dependencies

* six==1.10.0
* schematics==1.1.1

## Installation

### Clonning repo

```sh
python setup.py install
```

### From zipfile

```sh
pip install https://github.com/odra/pyco/archive/master.zip
```

## Development

Install dependencies:

```sh
pip install -U -r requiements.txt
```

Run tests:

```
py.test -s
```

## Usage

This module provides two classes for function and code objects manipulation:

* pyco.function.Function: function object that stores function props
* pyco.code.Code: Code object that stores funcion code property

Both classes are used to create a new function/code object, change it as needed, serialize, call the function back, etc.

Check the examples folder for detailed used while a more detailed documentation is not available. 

## License

MIT License

Copyright 2017  Leonardo Rossetti <me@lrossetti.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
