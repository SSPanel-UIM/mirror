Name:           sing-box
Version:        0.0.1
Release:        1%{?dist}
Summary:        The universal proxy platform.
Group:          Unspecified
License:        GPL-3.0
URL:            https://github.com/SagerNet/sing-box
Packager:       SSPanel-UIM Team <package@sspanel.org>
BuildRequires:  systemd

%description
The universal proxy platform.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/sing-box
mkdir -p %{buildroot}%{_sysconfdir}/sing-box
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/sing-box-amd64-linux %{buildroot}/usr/local/sing-box/sing-box
install -m 644 %{_builddir}/%{name}-%{version}/README.md %{buildroot}/usr/local/sing-box/README.md
install -m 644 %{_builddir}/%{name}-%{version}/LICENSE %{buildroot}/usr/local/sing-box/LICENSE
install -m 644 %{_builddir}/%{name}-%{version}/config.json %{buildroot}%{_sysconfdir}/sing-box/config.json
install -m 644 %{_builddir}/%{name}-%{version}/sing-box.service %{buildroot}%{_sysconfdir}/systemd/system

%post
ln -s /usr/local/sing-box/sing-box %{_bindir}/sing-box

%postun
rm -f %{_bindir}/sing-box

%clean
rm -rf %{buildroot}

%files
%attr(0755, root, root) /usr/local/sing-box
%attr(0755, root, root) /usr/local/sing-box/sing-box
%attr(0644, root, root) /usr/local/sing-box/README.md
%attr(0644, root, root) /usr/local/sing-box/LICENSE
%attr(0644, root, root) %{_sysconfdir}/sing-box
%attr(0644, root, root) %{_sysconfdir}/sing-box/config.json
%attr(0644, root, root) %{_sysconfdir}/systemd/system/sing-box.service

%changelog
* Sun Jul 24 2022 SSPanel-UIM Team <package@sspanel.org> - 1.4.3-1
 - https://github.com/SagerNet/sing-box/releases/tag/v1.4.3
