Name:           telepathy-haze
Version:        0.2.0
Release:        %mkrel 3
Summary:        A multiprotocol connection manager based on pidgin

Group:          Networking/Instant messaging
License:        GPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  telepathy-glib
BuildRequires:  pkgconfig(purple)
Requires:       telepathy-filesystem

%description
This connection manager allows you to use libpurple, pidgin backend, with 
telepathy, allowing you to access to numerous instant messaging network with
telepathy enabled software, such as empathy.

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_libdir}/%{name}
%{_mandir}/man*/*.lzma

#--------------------------------------------------------------------

%prep
%setup -q


%build
%configure 
%make


%install
rm -rf %buildroot
make install DESTDIR=%buildroot


%clean
rm -rf %buildroot
