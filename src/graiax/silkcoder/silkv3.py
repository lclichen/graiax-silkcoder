from . import _silkv3
import asyncio

def rate_round_down(rate: int, sorted_rate_list: list = [8000, 12000, 16000, 24000, 32000, 44100, 48000]):
    for i, x in enumerate(sorted_rate_list):
        if x > rate:
            return sorted_rate_list[i-1] if i > 0 else None
    return sorted_rate_list[-1]

def silk_encode(data: bytes, rate: int = -1, maximum_samplerate: int = 24000, bitrate: int = 25000, tencent: bool = True):
    if rate < 0:
        #保证压制出来的音频在1000kb上下，若音频时常在10min以内而不超过1Mb
        rate = rate_round_down(int(980 * 1024 / (len(data) / 24000 / 2) * 8))
    if rate not in [8000, 12000, 16000, 24000, 32000, 44100, 48000]:
        raise ValueError("input_samplerate should in [8000, 12000, 16000, 24000, 32000, 44100, 48000]")
    if maximum_samplerate not in [0, 8000, 12000, 16000, 24000]:
        raise ValueError("maximum_samplerate should in [8000, 12000, 16000, 24000]")
    return _silkv3.encode(data, rate, maximum_samplerate, bitrate, tencent = tencent)


async def async_silk_encode(data: bytes,
                            rate: int = -1,
                            maximum_samplerate: int = 24000,
                            bitrate: int = 25000,
                            tencent: bool = True):
    if rate < 0:
        #保证压制出来的音频在1000kb上下，若音频时常在10min以内而不超过1Mb
        rate = rate_round_down(int(980 * 1024 / (len(data) / 24000 / 2) * 8))
    if rate not in [8000, 12000, 16000, 24000, 32000, 44100, 48000]:
        raise ValueError("input_samplerate should in [8000, 12000, 16000, 24000, 32000, 44100, 48000]")
    if maximum_samplerate not in [0, 8000, 12000, 16000, 24000]:
        raise ValueError("maximum_samplerate should in [8000, 12000, 16000, 24000]")
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _silkv3.encode, data, rate, maximum_samplerate, bitrate, tencent = tencent)


def silk_decode(data: bytes):
    return _silkv3.decode(data)


async def async_silk_decode(data: bytes):
    return await asyncio.get_running_loop().run_in_executor(None, _silkv3.decode, data)


__all__ = ["silk_encode", "silk_decode", "async_silk_encode", "async_silk_decode"]