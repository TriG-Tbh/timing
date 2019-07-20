# Timing
A relatively short single script project that can be used for timing bits of code

Example usage:
```python
import timing
import time

timing.start("test1")
time.sleep(0)
timing.stop("test1")

timing.start("test2")
time.sleep(2)
timing.stop("test2")

timing.start("test3")
time.sleep(1)
timing.stop("test3")


timing.display(["test1", "test2", "test3"])

```
