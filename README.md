Build and tested for EL9. Requires policycoreutils-devel 

$ sudo dnf -y install policycoreutils-devel

To build policy module:

$ make -f /usr/share/selinux/devel/Makefile shibd.pp

To install module:

$ sudo semodule -i shibd.pp

Check for AVCs with

$ sudo ausearch -m avc

Currently shibd_t is set to permissive for testing.

To build RPM with shibd.sh:

$ sudo dnf -y install rpm-build
$ sh ./shibd.sh
