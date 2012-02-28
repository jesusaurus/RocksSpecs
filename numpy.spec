%define name	numpy
%define dist	rocks
%define release	1
%define version 1.6.1
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	python26
Requires:	python26
Summary:	NumPy

%description
NumPy for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup

echo '
[DEFAULT]
library_dirs = /share/apps/lib
include_dirs = /share/apps/include

[atlas]
atlas_libs = lapack, f77blas, cblas, atlas

[amd]
amd_libs = amd

[umfpack]
umfpack_libs = umfpack, gfortran

[fftw]
libraries = fftw3
' > site.cfg

%build
python26 setup.py build

%install
python26 setup.py install --prefix=$RPM_ROOT_DIR%{prefix}

%clean


%files
