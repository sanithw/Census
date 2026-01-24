# Python Development Best Practices

This document outlines the best practices and coding standards for Python development in this project.

## Code Style - PEP 8

Follow [PEP 8](https://pep8.org/) style guide for Python code:

### Indentation
- Use 4 spaces per indentation level
- Never mix tabs and spaces

### Line Length
- Limit lines to 79 characters for code
- Limit docstrings/comments to 72 characters
- Use implied line continuation inside parentheses, brackets, and braces

### Imports
- Import standard library modules first, then third-party modules, then local modules
- Use separate lines for each import
- Avoid wildcard imports (`from module import *`)
- Use absolute imports over relative imports when possible

```python
# Good
import os
import sys
from typing import List, Dict

import numpy as np
import pandas as pd

from myproject import mymodule
```

### Naming Conventions
- **Variables and functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_CASE_WITH_UNDERSCORES`
- **Private attributes/methods**: prefix with single underscore `_private_method`
- **Avoid single character names** except for counters or iterators

### Whitespace
- Use blank lines to separate functions and classes
- Use blank lines sparingly inside functions to indicate logical sections
- Avoid extraneous whitespace in expressions and statements

```python
# Good
spam(ham[1], {eggs: 2})

# Bad
spam( ham[ 1 ], { eggs: 2 } )
```

## Documentation

### Docstrings
Use docstrings for all public modules, functions, classes, and methods:

```python
def fetch_data(url: str, params: dict) -> dict:
    """
    Fetch data from the specified URL with given parameters.

    Args:
        url: The API endpoint URL
        params: Dictionary of query parameters

    Returns:
        Dictionary containing the API response data

    Raises:
        requests.RequestException: If the API request fails
    """
    pass
```

### Comments
- Write comments that explain "why", not "what"
- Keep comments up-to-date with code changes
- Use inline comments sparingly

## Type Hints

Use type hints for function signatures (Python 3.5+):

```python
from typing import List, Dict, Optional

def process_records(records: List[Dict[str, str]],
                   filter_key: Optional[str] = None) -> List[Dict[str, str]]:
    """Process and filter records."""
    pass
```

## Error Handling

### Exception Handling
- Catch specific exceptions rather than using bare `except:`
- Don't silence exceptions without good reason
- Use context managers for resource management

```python
# Good
try:
    with open('file.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    logger.error("File not found")
    raise
except IOError as e:
    logger.error(f"IO error occurred: {e}")
    raise
```

### Custom Exceptions
Create custom exceptions for domain-specific errors:

```python
class DataValidationError(Exception):
    """Raised when data validation fails."""
    pass
```

## Code Organization

### Function Design
- Keep functions small and focused on a single task
- Use descriptive names that indicate what the function does
- Limit the number of parameters (preferably 3 or fewer)
- Return early to reduce nesting

### Class Design
- Follow Single Responsibility Principle
- Use `@property` for getters and setters
- Use `@staticmethod` and `@classmethod` appropriately

## Best Practices

### General
- **Don't repeat yourself (DRY)**: Extract common code into reusable functions
- **Keep it simple**: Prefer simple, readable code over clever one-liners
- **Use list/dict comprehensions** for simple transformations
- **Use context managers** (`with` statements) for resource management
- **Prefer explicit over implicit**: Be clear about your intentions

### String Formatting
Use f-strings (Python 3.6+) for string formatting:

```python
name = "Alice"
age = 30
# Good
message = f"Hello, {name}! You are {age} years old."

# Avoid (older style)
message = "Hello, %s! You are %d years old." % (name, age)
```

### Comparisons
```python
# Use 'is' for None checks
if value is None:
    pass

# Use 'is not'
if value is not None:
    pass

# For booleans, don't compare explicitly
if is_valid:  # Good
    pass

if is_valid == True:  # Bad
    pass
```

### List/Dict Operations
```python
# Use 'in' for membership testing
if key in dictionary:
    pass

# Use .get() for dictionaries with defaults
value = dictionary.get('key', default_value)
```

## Testing

- Write unit tests for all functions and methods
- Use descriptive test names that explain what is being tested
- Follow the Arrange-Act-Assert pattern
- Aim for high test coverage but focus on critical paths

```python
def test_fetch_data_returns_valid_response():
    # Arrange
    url = "https://api.example.com/data"
    params = {"key": "value"}

    # Act
    result = fetch_data(url, params)

    # Assert
    assert isinstance(result, dict)
    assert "data" in result
```

## Dependencies

- Keep dependencies up to date
- Pin versions in `requirements.txt` for reproducibility
- Use virtual environments for project isolation
- Document any system-level dependencies

## Security

- Never hardcode sensitive information (API keys, passwords)
- Use environment variables or secure configuration management
- Validate and sanitize all external inputs
- Keep dependencies updated to patch security vulnerabilities

## Performance

- Profile before optimizing
- Use generators for large datasets
- Cache expensive computations when appropriate
- Consider using built-in functions and libraries (they're usually optimized)

## Tools

Consider using these tools to maintain code quality:
- **black**: Code formatter
- **flake8**: Linting
- **mypy**: Static type checking
- **pylint**: Code analysis
- **pytest**: Testing framework
