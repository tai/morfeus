morfeus.py - Python API for moRFeus mixer/signal generator
==========================================================

MoRFeus is a mixer/signal generator produced by the Othernet Inc.

- https://www.crowdsupply.com/outernet/morfeus
- https://othernet.is/products/morfeus-1

This API allows you to control various parameters of the moRFeus
over USB HID API, such as mixer/generator mode control and output/mixer
LO frequency.

No official doc on HID protocol is yet released, so this library is
created based on information found on the Othernet forum:

- https://forums.othernet.is/t/rf-product-morfeus-frequency-converter-and-signal-generator/5025/58

Some features were also discovered by trial-and-error.

# API Usage

Using the API is quite easy. All parameters can be accessed as
property variables, so all you need is to read/write each property
variable directly:

```python
import morfeus

mrf = morfeus.MoRFeus()
mrf.mode = morfeus.Mode.MIXER
mrf.freq = 120000000
mrf.bias = 0
mrf.current = 1
```

# CLI Usage

This library also comes with morfeus(1) command for an easy access
to the device over CLI. Usage is also easy as the API:

```sh
$ morfeus mode
MIXER
$ morfeus mode GENERATOR
$ morfeus freq 120000000
$ morfeus bias 0
$ morfeus current 0
```

# Installation
```
$ pip install morfeus
```

# Supported Platforms
It has been tested on all Linux, OSX, and Windows platforms,
with one caveat that it's not clear where and how to get morfeus(1)
command installed on Windows automatically.

# Requirements
This library depends on following runtime and libraries:

* Python3 (as it uses recent Python3 features)
* hidapi (cython-hidapi and underlying platform-dependent hidapi library)
