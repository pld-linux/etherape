Summary:	Graphical network viewer modeled after etherman
Summary(pl):	Graficzny monitor sieci
Summary(pt_BR):	Visualizador gr�fico de redes modelado como o etherman
Name:		etherape
Version:	0.9.0
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/etherape/%{name}-%{version}.tar.gz
# Source0-md5:	a712f4cb04897d1a02ce988cffbf254c
URL:		http://etherape.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Etherape is a graphical network monitor for Unix modeled after
etherman. Featuring ether, ip and tcp modes, it displays network
activity graphically. Hosts and links change in size with traffic.
Color coded protocols display. It supports ethernet, ppp and slip
devices. It can filter traffic to be shown, and can read traffic from
a file as well as live from the network.

%description -l pl
Etherape to graficzny monitor sieci dla uniks�w. Ma tryby ether, ip
oraz tcp, wy�wietla aktywno�� sieci graficznie. Hosty i po��czenia
zmienij� rozmiar wraz z ruchem. Protok�y obrazowane za pomoc�
kolor�w. Obs�uga urz�dze� ethernet, ppp i slip. Mo�e filtrowa� ruch
jaki pokazuje, czyta� z pliku lub bezpo�rednio z sieci.

%description -l pt_BR
O etherape � um monitor gr�fico de redes modelado como o etherman.
Cont�m modos ether, ip e tcp, mostrando de forma gr�fica a atividade
da rede: M�quinas e conex�es mudam em tamanho como o tr�fego e os
protocolos s�o codificados por cores. O Etherape suporta dispositivos
ethernet, ppp e slip.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pixmapsdir=%{_pixmapsdir} \
	Developmentdir=%{_desktopdir}

echo "Categories=Application;Network;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/etherape.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README* TODO
%attr(755,root,root) %{_bindir}/etherape
%{_datadir}/etherape
%{_mandir}/man1/etherape.1*
%{_desktopdir}/etherape.desktop
%{_pixmapsdir}/etherape.png
