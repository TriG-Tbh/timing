# Timing
A relatively short single script project that can be used for timing bits of code

Example usage:
```python
import timing

timing.start("foo")
time.sleep(0)
timing.stop("foo")

timing.start("bar")
time.sleep(2)
timing.stop("bar")

timing.start("foobar")
time.sleep(1)
timing.stop("foobar")

timing.display(["foo", "bar", "foobar"])
```
Output:

1: foo (1.0013580322265625e-05)
2: foobar (1.0010757446289062)
3: bar (2.000251054763794)
