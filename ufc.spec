%define name	ufc
%define dist	rocks
%define release	1
%define version 2.0.5
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
URL:		https://launchpad.net/ufc
Source:		http://launchpad.net/ufc/2.0.x/2.0.5/+download/ufc-2.0.5.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	cmake
BuildRequires:	swig
Requires:	swig
Summary:	UFC

%description
UFC for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup -n ufc-2.0.5

%build
cmake -DCMAKE_PREFIX_PATH=/share/apps -DCMAKE_INSTALL_PREFIX=%{prefix} .
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean


%files
   /share/apps/include/ufc.h
   /share/apps/lib/pkgconfig/ufc-1.pc
   /share/apps/lib64/python2.6/site-packages/ufc_utils/
   /share/apps/share/ufc/
   /share/apps/include/swig/ufc.i
   /share/apps/lib64/python2.6/site-packages/ufc/
