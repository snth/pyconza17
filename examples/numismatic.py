
from streamz import Stream
source = Stream()
printer = source.map(print)
L = []
collector = source.map(L.append)

from numismatic.exchanges import BitfinexExchange
bfx = BitfinexExchange(stream)
subscription = bfx.listen('BTCUSD', 'trades')

import asyncio
loop = asyncio.get_event_loop()
future = asyncio.wait([subscription], timeout=10)
loop.run_until_complete(future)
