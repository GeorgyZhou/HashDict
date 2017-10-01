## HashDict Usage

- To use *HashDict*, you need to import the library in your python project as: `from HashDict import HashDict` or `import HashDict`

*HashDict* provides following function:

- `set(key, value)` : Insert a (key, value) pair into hash table. If there's no slot found for the key, the method would return `false`, otherwise return `true`.
- `get(key)`: Get value from the hash table using the input key. If there's such pair return the value otherwise return `None`.
- `delete(key)`: Delete value from the hash table using the input key. If there's such pair return the value otherwise return `None`.
- `load()`: Return the load factor indicating how slots are currently occupied inside the hashtable. The load factor is calculated by `(items in hash map) /(size of hashDict)`
- `HashDict(size)`: Constructor to create an instance of HashDict with fixed size of `size`.

### Example

```python
from HashDict import HashDict

dic = HashDict(10)
dic.set('Hello World', 'Hello Michael') # Return True
dic.load() # Return 0.1 (1/10)
dic.get('Hello World') # Return 'Hello Michael'
dic.delete('Hello World') # Return 'Hello Michael' and delete corresponding pair
dic.load() # Return 0.0
```



## Test Usage

Run the following command under the main project directory: `python test.py`

If you want to add more test cases in the test script, just go ahead to `test.py`  and add more test cases under corresponding method.



## Implementation

*HashDict*  uses `list()` to store the (key, value) pair and uses *Open Addressing: Linear Probing* to deal with collision. 