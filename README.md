Build and tested for EL9 using `shibboleth-3.4.1-1.x86_64` and `httpd-2.4.57-5.el9.x86_64`

Requires policycoreutils-devel 
```
$ sudo dnf -y install policycoreutils-devel
```
Initial skeleton generated on AlmaLinux 9.3 with
```
$ sepolicy generate --init /sbin/shibd
```
To build policy module:
```
$ make -f /usr/share/selinux/devel/Makefile shibd.pp
```
To install module:
```
$ sudo semodule -i shibd.pp
$ sudo restorecon -Rv /usr/sbin/shibd /etc/shibboleth /var/log/shibboleth /var/cache/shibboleth /var/run/shibboleth
$ sudo systemctl restart httpd shibd
```
Check for AVCs with
```
$ sudo ausearch -m avc
```
It should show nothing related to `shibd`.

Currently `shibd_t` is set to permissive for testing!

To build RPM with shibd.sh:
```
$ sudo dnf -y install rpm-build
$ sh ./shibd.sh
```
