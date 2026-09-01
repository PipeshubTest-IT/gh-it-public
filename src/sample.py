def greet(name: str) -> str:
    if not name:
        raise ValueError("name must not be empty")
    return f"hello {name}"


def farewell(name: str) -> str:
    return f"bye {name}"
