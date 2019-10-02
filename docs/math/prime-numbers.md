# Prime Numbers

Using prime numbers is common in many problems. We implement various algorithms using them.

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.math import prime_lower

print(prime_lower(18))
# -> [2, 3, 5, 7, 11, 13, 17]

print(prime_lower(-1))
# -> []

print(prime_lower(1000001))
# -> []
```

## API

### prime_lower(query)

> Return array of prime numbers lower than `query`, `query` must be lower than `10e6` to avoid memory problems.

##### Params:

- `query`: superior limit for the array of prime number
