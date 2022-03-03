# Analysis for TEX yoda file format

## Know information

1. The TEX file format does not contain a checksums
2. The first 16 bytes are always the same and doesn't appear contain any key mappings?

## Open questions

1. Address `00001850` and onwards appears to be unused, speculated that this are intended for macros?
2. Can the key mapping be excluded by not having it in the file, from first glance appears to be the case for fn layer

# Codes

It is speculated that the key codes are derived from their value such as
1. value + 1 = key code on fn layer
2. value + 2 = key code on default layer

key  code  value
a    0402  0400
s    1602  1600
q    1402  1400
fn_q 1401

## Key format

### Key map format

Key maps are encoded using 4 bytes. It starts with **0020** and ends with a NULL byte(**0000**).
The remaining to bytes is the actual key mapping. The first bytes is the key and the second byte is the value/key it
should be mapped to.
+---------------------+
|Start|key |value|end |
+-----+----+-----+----+
|0020 |1602|0400 |0000|
+---------------------+

### Profile

The file is divider into 3 profile.
Beginning of a new profile is indicated by setting the next 8 bytes to the following:

 ```
0294 0200 2046 ffff 0000 0000 0000 0000
```

Afterwards the key mapping can proceed as normal, starting from the first key.
