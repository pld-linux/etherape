Summary:	Graphical network viewer modeled after etherman
Name:		etherape
Version:	0.5.6
Release:	1
License:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://download.sourceforge.net/pub/sourceforge/etherape/%{name}-%{version}.tar.gz
Patch0:		etherape-DESTDIR.patch
URL:		http://etherape.sourceforge.net/
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sbindir	%{_bindir}

%description
Etherape is a graphical network monitor for Unix modeled after
etherman. Featuring ether, ip and tcp modes, it displays network
activity graphically. Hosts and links change in size with traffic.
Color coded protocols display. It supports ethernet, ppp and slip
devices. It can filter traffic to be shown, and can read traffic from
a file as well as live from the network.

%prep
%setup -q
%patch0 -p1

%build
automake
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README FAQ README.help README.bugs \
	README.thanks

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/etherape
%{_mandir}/man?/*
