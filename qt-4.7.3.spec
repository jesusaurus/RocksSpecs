%define rocks		rocks
%define name		qt-%{rocks}
%define release		1
%define version		4.7.3
%define buildroot %{_topdir}/%{name}-%{version}-root

BuildRoot:		%{buildroot}
Summary: 		QT %{version} for a Rocks Cluster
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		qt-everywhere-opensource-src-%{version}.tar.gz
Prefix:			/share/apps
Group:			Rocks

%description
QT opensource for a Rocks Cluster (installed into the nfs share /share/apps).

%prep
%setup -q

%build
./configure
make

%install
make install prefix=$RPM_BUILD_ROOT/share/apps

%files
