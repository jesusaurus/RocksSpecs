%define name	armadillo
%define dist	rocks
%define release	1
%define version 2.4.4
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
cmake -DCMAKE_PREFIX_PATH=/share/apps -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT%{prefix} .
make


%install
make install

%clean
rm -rf $RPM_BUILD_ROOT


%files
/share/apps/include/armadillo
/share/apps/include/armadillo_bits
/share/apps/include/armadillo_itpp
/share/apps/lib/libarmadillo.so
/share/apps/lib/libarmadillo.so.2
/share/apps/lib/libarmadillo.so.%{version}
/share/apps/share/Armadillo/CMake/ArmadilloConfig.cmake
/share/apps/share/Armadillo/CMake/ArmadilloConfigVersion.cmake
/share/apps/share/Armadillo/CMake/ArmadilloLibraryDepends-noconfig.cmake
/share/apps/share/Armadillo/CMake/ArmadilloLibraryDepends.cmake

