# TEX keyboard configuration tool
> **This project is in no way affiliated with TEX Electronics.**

This is an open source alternative to the proprietary web configurator\
for [TEX](https://tex.com.tw/) keyboards, such as the `Yoda2`, `Shinobi` and
`Shura`.

## Goal

I aim to reverse engineer the .TEX binary format and develop a tool that allow\
fellow TEX keyboard owners to configure their own keyboards locally without the web\
configurator.


It begun out of concern that at some point in the future the server will be shutdown\
and also t of the frustrating experience of making minor patches to my\
current configuration. I had to recreate my entire configuration each time.

Though this started out with the intention only to support the Yoda2,\
the extend the scope to also include support for the following keyboard models:

* Yoda2
* Shura
* Shinobi

Unsupported keyboard

* Kodachi
* Yoda1

## Repo

> 1. ./doc : Information on the binary format.
> 2. ./src/TexConfig : Python source files

My personal configuration for each model can be found [here](src/tex.py)

## Example
```python
shura: TexConfigurator = TexConfiguratorShura
shura: TexConfigurator = TexConfiguratorShura()
# Binding Shura's fn key to fn layer 2, disables the caps-lock functionally
# binding to layer1 will keep the functionality
shura.addConfigFnEntry(TexProfile.PROFILE_1, TexFnLayer.FN_LAYER2, "fn")
shura.addConfigFnEntry(TexProfile.PROFILE_1, TexFnLayer.FN_LAYER2, "right_shift")
shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "e", "vol+")
shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "left", "home")

texBuilder = TexBinaryBuilder(shura)
texBuilder.binaryGenerate("KEYMAP.TEX")
```

## Missing features

* Limited macro support
* GUI
