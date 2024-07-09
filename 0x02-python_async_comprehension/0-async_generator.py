#!/usr/bin/env python3
"""asyn generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator: coroutine that loops 10 times, each time asynchronously
    waits 1 second, then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


# async def print_yielded_values():
#    result = []
#    async for i in async_generator():
#        result.append(i)
#    print(result)
#
# asyncio.run(print_yielded_values())
