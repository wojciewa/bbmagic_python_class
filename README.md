# BBMagic python class

Python class for support BBMagic devices http://bbmagic.net/
Class based on project https://github.com/z1mEk/bbmagic_python_class . The original one uses the version 1.4 library and unfortunately for some reasons it does not work with the new BBagic modules (at least in my case). Unfortunately it was also not possible to get version 2.0 from BBMagic. So, I decide to encapsulate bbmagic_lib_2.0.a in new library which can be used from within Python

## Install

1. Clone plugin repository.
```bash
sudo git clone https://github.com/wojciewa/bbmagic_python_class.git bbmagic_lib
```
2. Change directory to bbmagic_python_class
```bash
cd bbmagic_python_class
```
3. Install dependent libraries.
```bash
sudo sh install_bbm_lib.sh
```
