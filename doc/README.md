# Analysis for TEX yoda file format

## Know information

1. The TEX file format does not contain a checksums
2. The first 16 bytes are always the same and doesn't appear contain any key mappings?

## Open questions

2. Can the key mapping be excluded by not having it in the file, from first glance appears to be the case for fn layer

# Codes

It is speculated that the key codes are derived from their value such as
> 1. value + 1 = key code on fn layer
> 2. value + 2 = key code on default layer
> 3. value + 3 = key code on unknown

It appears that there are currently 4 different keys codes for a single key, will be referring to them layers from now
on.

```
+-----+------+---------------------------+
|Layer| value| Descrption                |
+-----+------+---------------------------+
|0    | 0400 | Unkown(affected by macro) |
|1    | 0401 | fn layer                  |
|2    | 0402 | normal layer              |
|3    | 0403 | Unkown(affected by macro) |
+-----+------+---------------------------+
```

It is currently unknown that the purpose is for the third and zero layer.
However they're both affected differently by macro assignment.


```
+----+-----+------+
| key| code| value|
+----+-----+------+
|a   | 0402| 0400 |
|s   | 1602| 1600 |
|q   | 1402| 1400 |
|fn_q| 1401|      |
+-----------------+
```
## Key format

### Key map format

Key maps are encoded using 8 bytes. It starts with **0220** and ends with a two NULL byte(**0000**).
The remaining to bytes is the actual key mapping. The first two bytes is the key and the second two bytes is the value/key it
should be mapped to.
```
+---------------------+
|Start|key |value|end |
+-----+----+-----+----+
|0220 |1602|0400 |0000|
+---------------------+
```

The value only appears to be contained withi the first byte.
It is possible that the second byte has another use.
there are few keys where this does not appear to be the case, could the be trackpoint speed control?.

### Profile

The file is divider into 3 profile.
Beginning of a new profile is indicated by setting the next 16 bytes to the following:

 ```
0294 0200 2046 ffff 0000 0000 0000 0000
```

Afterwards the key mapping can proceed as normal, starting from the first key.

### Macros

Macros mapping are stored at end of the key map sections indicated by the following bytes

```
 0294 0200 2046 ffff 0000 0000 0000 0000
```

The macro byte sequence does not have any byte that initializes the sequence it simply starts at the end of the key mapping section.
It does however have 4 terminating bytes **00fc c800** and a two separator bytes **5a00**.

A two bytes are used to indicated the key and action. Actions being press or release.
As mentioned in previous section the value or which key to press is only indicated by the first byte.
The second byte is used to indicated the action. A key press for the letter s would be **163c**
and release would then be **165c**. 

Below is a single macro byte sequence for pressing the key `s`
```
163c 5a00 165c 5a00 00fc c800
```

When configuring a macro the normal key value both the normal and unknown layer should be set to zero does not affect the fn layer.
Note that the test was done by binding a macro to the default layer which perhaps why the fn layer was not affected.
I assume this reset is to prevent a macro from calling itself infinitely.

The zero layer will be changed

The first two bytes are changed to **0218** from **0220** && the key bytes are set to zero
The remaining byte of the value are changes to **3c**, finally the terminating bytes are set to "0100"

```
Layer 0 for key s
+---------------------+
|Start|key |value|end |
+-----+----+-----+----+
|0218 |0000|043c |0100|
+---------------------+
```
It does seem that a single macro sequence appears multiple times, which could indicated that it is possible to configure macro sequences per profile.

For every macro added there appears to be some changes made to the start of the file however it is not now how this is done at the moment

