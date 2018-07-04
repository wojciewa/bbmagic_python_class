#!/bin/sh
libv="1.2"
## prepare dynamic library bbmagic_lib to dynamic library
wget http://bbmagic.net/download/bin/bbmagic_lib_$libv.tar.gz
tar -zxvf bbmagic_lib_$libv.tar.gz
cd bbmagic_lib_$libv
ar -xv bbmagic_lib_$libv.a bbmagic_lib_$libv.o
wget http://bbmagic.net/download/bin/libbluetooth.a
gcc -shared -o bbmagic_lib_$libv.so bbmagic_lib_$libv.o libbluetooth.a
rm bbmagic_lib_$libv.a bbmagic_lib_$libv.o libbluetooth.a
cd ..
rm bbmagic_lib_$libv.tar.gz
ls
