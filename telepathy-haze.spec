Name:           telepathy-haze
Version:        0.4.0
Release:        %mkrel 1
Summary:        A multiprotocol connection manager based on pidgin

Group:          Networking/Instant messaging
License:        GPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  libtelepathy-glib-devel >= 0.9.2
BuildRequires:  pkgconfig(purple) >= 2.6
BuildRequires:  xsltproc
Requires:       telepathy-filesystem
Suggests:	pidgin-plugins

%description
This connection manager allows you to use libpurple, pidgin backend, with 
telepathy, allowing you to access to numerous instant messaging network with
telepathy enabled software, such as empathy.

%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS
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
%makeinstall_std

%clean
rm -rf %buildroot
