Name:           oohpack
Version:        0.1.0
Release:        1%{?dist}
Summary:        Encodes and decodes HTTP/2 HPACK header compression tables for debugging.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oohpack
Source0:        oohpack-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oohpack is a sovereign, capability-bounded HPACK INSPECTOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oohpack
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oohpack-uninstall

%files
/usr/bin/oohpack
/usr/bin/oohpack-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
