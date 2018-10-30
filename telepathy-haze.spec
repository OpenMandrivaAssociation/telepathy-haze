Name:		telepathy-haze
Version:	0.99.11
Release:	3
Summary:	A multiprotocol connection manager based on pidgin
Group:		Networking/Instant messaging
License:	GPLv2+
URL:		http://telepathy.freedesktop.org/wiki/
Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	telepathy-glib-devel >= 0.9.2
BuildRequires:	pkgconfig(purple) >= 2.6
BuildRequires:	xsltproc
Requires:	telepathy-filesystem
Suggests:	pidgin-plugins

%description
This connection manager allows you to use libpurple, pidgin backend, with 
telepathy, allowing you to access to numerous instant messaging network with
telepathy enabled software, such as empathy.

%files
%doc AUTHORS NEWS
%{_datadir}/dbus-1/services/*.service
#%{_datadir}/telepathy/managers/*.manager
%{_mandir}/man*/*.*
%{_libexecdir}/%{name}

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure PYTHON=%{__python2}
%make

%install
%makeinstall_std
