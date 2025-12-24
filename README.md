# LIST METHODS
- append()	Adds an element at the end of the list
- clear()	Removes all the elements from the list
- copy()	Returns a copy of the list
- count()	Returns the number of elements with the specified value
- extend()	Adds the elements of a list (or any iterable) to the end of the current list
- index()	Returns the index of the first element with the specified value
- insert()	Adds an element at the specified position
- pop()	Removes the element at the specified position
- remove()	Removes the item with the specified value
- reverse()	Reverses the order of the list

## Modules – datetime

| Directive | Description | Example |
|----------|-------------|---------|
| `%a` | Weekday, short version | Wed |
| `%A` | Weekday, full version | Wednesday |
| `%w` | Weekday as a number (0–6), where 0 is Sunday | 3 |
| `%d` | Day of month (01–31) | 31 |
| `%b` | Month name, short version | Dec |
| `%B` | Month name, full version | December |
| `%m` | Month as a number (01–12) | 12 |
| `%y` | Year, short version (without century) | 18 |
| `%Y` | Year, full version | 2018 |
| `%H` | Hour (00–23) | 17 |
| `%I` | Hour (00–12) | 05 |
| `%p` | AM / PM | PM |
| `%M` | Minute (00–59) | 41 |
| `%S` | Second (00–59) | 08 |
| `%f` | Microsecond (000000–999999) | 548513 |

## Modules – math

| Method | Description |
|--------|------------|
| `math.acos(x)` | Returns the arc cosine of x |
| `math.acosh(x)` | Returns the inverse hyperbolic cosine of x |
| `math.asin(x)` | Returns the arc sine of x |
| `math.asinh(x)` | Returns the inverse hyperbolic sine of x |
| `math.atan(x)` | Returns the arc tangent of x (in radians) |
| `math.atan2(y, x)` | Returns the arc tangent of y/x (in radians) |
| `math.atanh(x)` | Returns the inverse hyperbolic tangent of x |
| `math.ceil(x)` | Rounds x up to the nearest integer |
| `math.comb(n, k)` | Returns number of ways to choose k items from n without repetition |
| `math.copysign(x, y)` | Returns x with the sign of y |
| `math.cos(x)` | Returns cosine of x |
| `math.cosh(x)` | Returns hyperbolic cosine of x |
| `math.degrees(x)` | Converts radians to degrees |
| `math.dist(p, q)` | Returns Euclidean distance between points p and q |
| `math.erf(x)` | Returns the error function of x |
| `math.erfc(x)` | Returns the complementary error function |
| `math.exp(x)` | Returns e raised to the power x |
| `math.expm1(x)` | Returns eˣ − 1 |
| `math.fabs(x)` | Returns absolute value of x |
| `math.factorial(x)` | Returns factorial of x |
| `math.floor(x)` | Rounds x down to the nearest integer |
| `math.fmod(x, y)` | Returns remainder of x / y |
| `math.frexp(x)` | Returns mantissa and exponent of x |
| `math.fsum(iterable)` | Returns precise floating-point sum |
| `math.gamma(x)` | Returns the gamma function of x |
| `math.gcd(a, b)` | Returns greatest common divisor |
| `math.hypot(x, y)` | Returns √(x² + y²) |
| `math.isclose(a, b)` | Checks if two values are close |
| `math.isfinite(x)` | Checks if x is finite |
| `math.isinf(x)` | Checks if x is infinite |
| `math.isnan(x)` | Checks if x is NaN |
| `math.ldexp(x, i)` | Returns x × (2ⁱ) |
| `math.log(x)` | Returns natural logarithm |
| `math.log10(x)` | Returns base-10 logarithm |
| `math.log2(x)` | Returns base-2 logarithm |
| `math.modf(x)` | Returns fractional and integer parts |
| `math.perm(n, k)` | Returns number of permutations |
| `math.pow(x, y)` | Returns x raised to power y |
| `math.radians(x)` | Converts degrees to radians |
| `math.sin(x)` | Returns sine of x |
| `math.sinh(x)` | Returns hyperbolic sine |
| `math.sqrt(x)` | Returns square root |
| `math.tan(x)` | Returns tangent of x |
| `math.tanh(x)` | Returns hyperbolic tangent |
| `math.trunc(x)` | Truncates decimal part |

## Built-in Exceptions in Python

| Exception Name | Description |
|----------------|-------------|
| `BaseException` | Base class for all built-in exceptions |
| `Exception` | Base class for all non-exit exceptions |
| `ArithmeticError` | Base class for arithmetic-related errors |
| `ZeroDivisionError` | Division or modulo by zero |
| `OverflowError` | Numerical result exceeds maximum limit |
| `FloatingPointError` | Floating-point operation failure |
| `AssertionError` | Raised when an `assert` statement fails |
| `AttributeError` | Attribute reference or assignment fails |
| `IndexError` | Sequence index out of range |
| `KeyError` | Dictionary key not found |
| `TypeError` | Invalid type for an operation |
| `ValueError` | Correct type but invalid value |
| `NameError` | Variable name not defined |
| `ImportError` | Module import fails |
| `ModuleNotFoundError` | Module not found |
| `FileNotFoundError` | File or directory not found |
| `PermissionError` | Permission denied |
| `RuntimeError` | Error with no specific category |
| `NotImplementedError` | Feature not implemented |
| `StopIteration` | Raised by `next()` to stop iteration |
| `KeyboardInterrupt` | Program interrupted by user (Ctrl+C) |

| Exception Name | Description |
|----------------|-------------|
| `LookupError` | Base class for lookup-related errors |
| `UnicodeError` | Base class for Unicode-related errors |
| `UnicodeEncodeError` | Raised when Unicode encoding fails |
| `UnicodeDecodeError` | Raised when Unicode decoding fails |
| `UnicodeTranslateError` | Raised during Unicode translation |
| `EOFError` | Raised when `input()` reaches end-of-file |
| `MemoryError` | Raised when memory allocation fails |
| `RecursionError` | Raised when maximum recursion depth is exceeded |
| `SystemError` | Raised when the interpreter detects an internal error |
| `TimeoutError` | Raised when a system function times out |
| `OSError` | Raised for OS-related errors |
| `IsADirectoryError` | Raised when a file operation is attempted on a directory |
| `NotADirectoryError` | Raised when a directory operation is attempted on a file |
| `BrokenPipeError` | Raised when a pipe is broken |
| `ConnectionError` | Base class for connection-related errors |

