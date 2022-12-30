import functools

from src.shared.exceptions import NotFoundException


def _check_exist():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            result = await func(*args, **kwargs)
            if result is None:
                raise NotFoundException
            return result

        return wrapped

    return wrapper


check_exist = _check_exist()
