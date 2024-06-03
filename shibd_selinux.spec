# vim: sw=4:ts=4:et


%define relabel_files() \
restorecon -R /usr/sbin/shibd /etc/shibboleth /var/log/shibboleth /var/cache/shibboleth /var/run/shibboleth ; \

%define selinux_policyver 38.1.23-1

Name:   shibd_selinux
Version:	1.1.1
Release:	1%{?dist}
Summary:	SELinux policy module for shibd

Group:	System Environment/Base
License:	GPLv2+
URL:		https://github.com/gvde/selinux-shibd
Source0:	shibd.pp
Source1:	shibd.if
Source2:	shibd_selinux.8


Requires: policycoreutils-python-utils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils-python-utils
Requires(postun): policycoreutils-python-utils
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for shibd.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man8/shibd_selinux.8
install -d %{buildroot}/etc/selinux/targeted/contexts/users/


%post
semodule -n -i %{_datadir}/selinux/packages/shibd.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files

fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r shibd
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       %relabel_files

    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/shibd.pp
%{_datadir}/selinux/devel/include/contrib/shibd.if
%{_mandir}/man8/shibd_selinux.8.*


%changelog
* Mon Apr  1 2024 YOUR NAME <YOUR@EMAILADDRESS> 1.0-1
- Initial version

