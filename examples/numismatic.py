
from streamz import Stream
stream = Stream()
sink = stream.map(print)

from numismatic.exchanges import BitfinexExchange
bfx = BitfinexExchange(stream)
subscription = bfx.listen('BTCUSD', 'trades')

import asyncio
loop = asyncio.get_event_loop()
future = asyncio.wait([subscription], timeout=10)
loop.run_until_complete(future)
