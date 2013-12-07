Name:           telepathy-haze
Version:        0.7.1
Release:        5
Summary:        A multiprotocol connection manager based on pidgin

Group:          Networking/Instant messaging
License:        GPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:		telepathy-automake-1.13.patch

BuildRequires:  telepathy-glib-devel >= 0.9.2
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
#%{_datadir}/telepathy/managers/*.manager
%{_libdir}/%{name}
%{_mandir}/man*/*.xz

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

aclocal
autoheader
automake -a
autoconf

%build
%configure 
%make


%install
%makeinstall_std


%changelog
* Sat Nov 24 2012 Arkady L. Shane <ashejn@rosalab.ru> - 0.7.0-1
- update to 0.7.0

* Fri Apr 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.0-1
+ Revision: 793945
- version update 0.6.0

* Sat Aug 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 567250
- update to 0.4.0
- bump BR versions

* Mon Mar 08 2010 Frederik Himpe <fhimpe@mandriva.org> 0.3.4-1mdv2010.1
+ Revision: 516762
- Fix BuildRequires
- update to new version 0.3.4

* Mon Jan 25 2010 Frederik Himpe <fhimpe@mandriva.org> 0.3.3-1mdv2010.1
+ Revision: 496355
- update to new version 0.3.3

* Wed Nov 18 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.3.2-2mdv2010.1
+ Revision: 467208
- add pidgin-plugins as a Suggests since it's what contains the aim and yahoo plugins which telepathy-haze tries to dlopen when needed

* Tue Aug 25 2009 Frederik Himpe <fhimpe@mandriva.org> 0.3.2-1mdv2010.0
+ Revision: 421219
- update to new version 0.3.2

* Sat Jun 06 2009 Frederik Himpe <fhimpe@mandriva.org> 0.3.1-1mdv2010.0
+ Revision: 383192
- update to new version 0.3.1

* Tue Aug 19 2008 Frederik Himpe <fhimpe@mandriva.org> 0.2.1-1mdv2009.0
+ Revision: 274028
- Fix BuildRequires
- Use %%makeinstall_std
- Don't package COPYING
- Package NEWS
- update to new version 0.2.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 0.2.0-1mdv2008.1
+ Revision: 177224
- import telepathy-haze

