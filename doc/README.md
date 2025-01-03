# Analysis for TEX yoda file format

## Open questions

1. Can the key mapping be excluded by not having it in the file, from first glance appears to be the case for fn layer

## Binary header

~~The header appears to be affected by changes such as adding macro or creating binding on new layers.~~

The binary always start with `0x4359 0x4649 0x0000`(CYFI), The next byte appears to be counting the number of
8 byte sequences, before the keymap section of the first profile. Basically configuration related to the profiles.
> The byte after that always seems to remain zero, warrants further investigation.

After the header we find some configuration related to the keyboard profiles, currently supports max 3 profiles?
For each profile we have 8 bytes that marks the starting address of their respective key map section 
Address is stored as 16 bit little endian(LE)

```
+---------+-------+--------------------------+-------+
|Profile  |fixed  |Profile Start Address(LE) |fixed  |
+---------+-------+--------------------------+-------+
| 0x0001  |0x0000 |0x2000                    |0x0000 |
+---------+-------+--------------------------+-------+
```

```
+-------------------+-------+--------------------------+-------+
|    Profile        | Fixed |Macro Start Address(LE)   |fixed  |
+-----------+-------+-------+--------------------------+-------+
|Macro Field|Index  |       |                          |       |
+-----------+-------+-------+--------------------------+-------+
| 0x01      | 0x01  |0x0000 |        0x2000            |0x0000 |
+---------+-------+---------+--------------------------+-------+
```

## Key format

After the Binary header there is the key configuration for each profile.
Each profile has a key map section and an FN layer switching key binding section

### Key map format

Key bindings consists of 8 bytes. Beginning with **0x0220** and ends with two NULL bytes(**0x0000**).
The remaining 4 bytes is the hardware key and value. The first two bytes are the hardware key and last the value/action.
```
+-------------------------+
|Preamble |key |value|end |
+---------+----+-----+----+
|0220     |1602|0400 |0000|
+-------------------------+
```

The value to which the hardware key binds to only appears to be contained within the first byte.
It is possible that the second byte has another use.
There are few keys where this does not appear to be the case,
one appears to be trackpoint speed control.

keys can be disabled by setting the value to **ff00** or somteimes **0000**
TEST: Disable all fn1 keys

The hardware keys can be configured with up to 4 different values, one for each layer, 3 FN layers and the normal layer.
The hardware key is made up of two parts, the actual key and the layer, see below:

```
+-----------+
|    Key    |
+-----------+
|key  |layer|
+-----+----+-
|0x16 |0x01 |
+-----------+
```

Layers for letter **a** on standard ansi-US layout.
```
+-----+------+--------------+
|Layer| value| Descrption   |
+-----+------+--------------+
|0    | 0400 | Normal layer |
|1    | 0401 | fn 1 layer   |
|2    | 0402 | fn 2 layer   |
|3    | 0403 | fn 3 layer   |
+-----+------+--------------+
```

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

### FN Layers

At the the end of each keymap section of a profile there is an FN lay configuration for which hardware keys that can be
used to switch to a specific FN layer, The sequence begins with three fixed bytes **0x029**.
This is then followed by a single byte indicating which layer to switch to when a given key is pressed, starting at
**0x4**

> Note: At the moment we know it is possible to configure up to 3 FN layers

 ```
+---------+---------+----------+---------+------+------+------+------+---------------------------+
|Preamble |FN Layer |num keys  |Delimiter|Key1  |Key2  |key3  |key4  | Terminating               |
+---------+---------+----------+---------+------+------+------+------+---------------------------+
|0x029    | 0x4     |   0x02   | 0x00    | 0x20 | 0x46 | 0xff | 0xff |0x0000 0x0000 0x0000 0x0000|
+---------+---------+----------+---------+------+------+------+------+---------------------------+
```

There can at most be 4 keys for each **fn** at any given moment all of which have their own designated byte.
The num keys byte indicate how many keys are set. **0xff** is disabled.

It appear this sequence can be extended when a new fn layer is enabled.
Then a second sequence is added after the separator.


> 1. 0294 = fn1
> 2. 0295 = fn2
> 3. 0296 = fn3

Key is indicating which key that FN2 layer action is bound to. Normal key mappings appear to be unaffected
which would mean that this works as a global override for the key.

The key does not appear to match the value of the same hardware key used in the normal key mapping nor does it appear to 
derived from it.

When bound to `q` the key was **0x05**, but when bound to `w` it was **0d**

Afterwards the key mapping can proceed as normal, starting from the first key.

> **Note**: that it does seem that the first layer must always exist and if there are no keys mapped
> it should default to the two keys **4f4e**

#### Bugs?
> Keys such as the middle mouse are a bit weird, when alone is uses 2 bytes(really only the first 12 bit)
> but when other keys are added it uses just a single byte encoding. And this only occurs when the key is bound to **fn1**
> **Possible bug?**


### Macros

Macros sequences are stored at the end of the third and final profile
The macro byte sequence does not have any byte that initializes the sequence it simply starts at the end of the key mapping section.
It does however have termination sequence **00fc c800** and a seperator **5a00**.

Only two bytes are used to indicated the key and action. Actions being press or release.
The key is only indicated by the first byte.
The second byte is used to indicated the action. A key press for the letter s would be **163c**
and release would then be **165c**. 

Below is a single macro byte sequence for pressing the key `s`
```
163c 5a00 165c 5a00 00fc c800
```

When apply a micro binding for a key of a given layer the first two bytes are
changed to **0218** from **0220** && the key bytes are zeroed The
remaining bytes of the value are changes to  **<key byte>3c**, finally the terminating
bytes are set to "0100" it is possible that is referencing the macro sequence.

```
Layer 0 for key s
+---------------------+
|Start|key |value|end |
+-----+----+-----+----+
|0218 |0000|043c |0100|
+---------------------+
```

It does seem that a single macro sequence appears multiple times, which could
indicated that it is possible to configure macro sequences per profile.

For every macro added there appears to be some changes made to the start of the
file however it is not now how this is done at the moment

