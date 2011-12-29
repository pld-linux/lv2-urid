Summary:	LV2 URID extension - features for mapping URIs to and from integers
Summary(pl.UTF-8):	Rozszerzenie LV2 URID - odwzorowywanie między URI a liczbami całkowitymi
Name:		lv2-urid
Version:	1.0
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	9c3459d46e6cc19747a567a547f7d195
URL:		http://lv2plug.in/ns/ext/urid/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
Requires:	lv2core >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 URID extension defines a simple mechanism for plugins to map URIs
to and from integers, usually for performance reasons (e.g. processing
events typed by URIs in real time). Typically, plugins map URIs to
integers for things they "understand" at instantiation time, and store
those values for use in the audio thread without doing any string
comparison. This allows the extensibility of RDF with the performance
of integers (or centrally defined enumerations).

Note: this extension is intended as an improved and simplified
replacement for the uri-map extension.

%description -l pl.UTF-8
Rozszerzenie LV2 URID definiuje prosty mechanizm dla wtyczek,
pozwalający odwzorowywać między URI a liczbami całkowitymi - głównie
ze względu na wydajność (np. przetwarzanie w czasie rzeczywistym
zdarzeń mających typy definiowane przez URI). Zwykle wtyczki
odwzorowują URI na liczby całkowite dla elementów, które są zrozumiałe
w czasie tworzenia instancji, a następnie zapisywanie tych wartości w
celu użycia w wątku dźwiękowym bez wykonywania żadnego porównywania
łańcuchów znaków. Pozwala to na rozszerzanie RDF-a z wydajnością liczb
całkowitych (lub globalnie zdefiniowanymi wyliczeniami).

Uwaga: to rozszerzenie jest pomyślane jako ulepszony i uproszczony
zamiennik rozszerzenia uri-map.

%package devel
Summary:	Header file for LV2 URID extension
Summary(pl.UTF-8):	Plik nagłówkowy rozszerzenia LV2 URID
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core-devel >= 6.0

%description devel
Header file for LV2 URID extension.

%description devel -l pl.UTF-8
Plik nagłówkowy rozszerzenia LV2 URID.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%dir %{_libdir}/lv2/urid.lv2
%{_libdir}/lv2/urid.lv2/urid.ttl
%{_libdir}/lv2/urid.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
%{_libdir}/lv2/urid.lv2/urid.h
%{_includedir}/lv2/lv2plug.in/ns/ext/urid
%{_pkgconfigdir}/lv2-lv2plug.in-ns-ext-urid.pc
