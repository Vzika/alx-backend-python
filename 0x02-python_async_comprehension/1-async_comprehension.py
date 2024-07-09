#!/usr/bin/env python3
"""Async Comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ collect random numbers using an async comprehensing over
    async_generator, then return the 10 random numbers.
    """
    return [numbers async for numbers in async_generator()]


# async def main():
#    print(await async_comprehension())
#
# asyncio.run(main())
