Summary:	Graphical network viewer modeled after etherman
Summary(pl):	Graficzny monitor sieci
Summary(pt_BR):	Visualizador gráfico de redes modelado como o etherman
Name:		etherape
Version:	0.8.2
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	ftp://download.sourceforge.net/pub/sourceforge/etherape/%{name}-%{version}.tar.gz
URL:		http://etherape.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-gnome-devel
BuildRequires:	libpcap-devel
BuildRequires:	libtool
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

%description -l pl
Etherape to graficzny monitor sieci dla uniksów. Ma tryby ether, ip
oraz tcp, wy¶wietla aktywno¶æ sieci graficznie. Hosty i po³±czenia
zmienij± rozmiar wraz z ruchem. Protokó³y obrazowane za pomoc±
kolorów. Obs³uga urz±dzeñ ethernet, ppp i slip. Mo¿e filtrowaæ ruch
jaki pokazuje, czytaæ z pliku lub bezpo¶rednio z sieci.

%description -l pt_BR
O etherape é um monitor gráfico de redes modelado como o etherman.
Contém modos ether, ip e tcp, mostrando de forma gráfica a atividade
da rede: Máquinas e conexões mudam em tamanho como o tráfego e os
protocolos são codificados por cores. O Etherape suporta dispositivos
ethernet, ppp e slip.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I /usr/X11R6/include/libglade-1.0"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Developmentdir=%{_applnkdir}/Network/Misc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README FAQ README.help README.bugs README.thanks
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/etherape
%{_mandir}/man?/*
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/*
