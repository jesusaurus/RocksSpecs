%define name	armadillo
%define dist	rocks
%define release	1
%define version 3.2.4
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
URL:		http://arma.sourceforge.net/
Source:		http://sourceforge.net/projects/arma/files/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	atlas
BuildRequires:	boost
Requires:	atlas
Requires:	boost
Summary:	Armadillo

%description
Armadillo for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup 

%build
cmake -DCMAKE_PREFIX_PATH=/share/apps -DBLAS_LIBRARY=/share/apps/lib/libatlas.a -DCMAKE_INSTALL_PREFIX=%{prefix} .
make


%install
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
/share/apps/include/armadillo
/share/apps/include/armadillo_bits
/share/apps/lib64/libarmadillo.so
/share/apps/lib64/libarmadillo.so.3
/share/apps/lib64/libarmadillo.so.%{version}
/share/apps/share/Armadillo/

