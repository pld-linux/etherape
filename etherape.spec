# Note that this is NOT a relocatable package
%define ver      0.4.6
%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix   /usr

Summary: Graphical network viewer modeled after etherman.
Name: etherape
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/Networking
Source: http://download.sourceforge.net/etherape/etherape-%{ver}.tar.gz
# Source1: ee-stdimg-new.xpm

BuildRoot: /var/tmp/etherape-%{PACKAGE_VERSION}-root
URL: http://etherape.sourceforge.net/
Docdir: %{prefix}/doc
Requires: gnome-libs >= 1.0.0

%description
Etherape is a graphical network monitor for Unix modeled after
etherman. Featuring ether, ip and tcp modes, it displays network
activity graphically. Hosts and links change in size with traffic. 
Color coded protocols display. It supports ethernet, ppp and slip 
devices. It can filter traffic to be shown, and can read traffic 
from a file as well as live from the network. 

%changelog
* Mon Apr 3 2000 Juan Toledo <toledo@sourceforge.net>
- Initial spec file copied from electric eyes

%prep
%setup -q

# insert new rh logo image
#cp %{SOURCE1} stdimg.xpm

%build
( export LINGUAS="$LINGUAS" && unset LINGUAS &&  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --enable-static-pcap )
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

strip $RPM_BUILD_ROOT%{prefix}/sbin/* ||:

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README FAQ README.help README.bugs README.thanks
%{prefix}/sbin/*
%{prefix}/share/locale/*/*/*
