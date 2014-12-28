Summary:	Graphical network viewer modeled after etherman
Summary(pl.UTF-8):	Graficzny monitor sieci
Summary(pt_BR.UTF-8):	Visualizador gráfico de redes modelado como o etherman
Name:		etherape
Version:	0.9.7
Release:	7
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/etherape/%{name}-%{version}.tar.gz
# Source0-md5:	7b5783090d92abe79634da4b582c6b48
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-resolv.patch
Patch3:		%{name}-Makefile.patch
URL:		http://etherape.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Etherape is a graphical network monitor for Unix modeled after
etherman. Featuring ether, ip and tcp modes, it displays network
activity graphically. Hosts and links change in size with traffic.
Color coded protocols display. It supports ethernet, ppp and slip
devices. It can filter traffic to be shown, and can read traffic from
a file as well as live from the network.

%description -l pl.UTF-8
Etherape to graficzny monitor sieci dla uniksów. Ma tryby ether, ip
oraz tcp, wyświetla aktywność sieci graficznie. Hosty i połączenia
zmieniają rozmiar wraz z ruchem. Protokóły obrazowane za pomocą
kolorów. Obsługa urządzeń ethernet, ppp i slip. Może filtrować ruch
jaki pokazuje, czytać z pliku lub bezpośrednio z sieci.

%description -l pt_BR.UTF-8
O etherape é um monitor gráfico de redes modelado como o etherman.
Contém modos ether, ip e tcp, mostrando de forma gráfica a atividade
da rede: Máquinas e conexões mudam em tamanho como o tráfego e os
protocolos são codificados por cores. O Etherape suporta dispositivos
ethernet, ppp e slip.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pixmapsdir=%{_pixmapsdir} \
	Developmentdir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_desktop_database_post

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README* TODO
%attr(755,root,root) %{_bindir}/etherape
%{_datadir}/etherape
%{_mandir}/man1/etherape.1*
%{_desktopdir}/etherape.desktop
%{_pixmapsdir}/etherape.png
%{_omf_dest_dir}/%{name}
