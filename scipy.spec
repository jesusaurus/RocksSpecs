%define name	scipy
%define dist	rocks
%define release	1
%define version 0.10.0
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
Summary:	SciPy

%description
SciPy for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup

echo '
[DEFAULT]
library_dirs = /share/apps/lib:/share/apps/lib64
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
export PYTHONPATH=/share/apps/lib/python2.6/site-packages:/share/apps/lib64/python2.6/site-packages:$PYTHONPATH
python26 setup.py build

%install
export PYTHONPATH=/share/apps/lib/python2.6/site-packages:/share/apps/lib64/python2.6/site-packages:$PYTHONPATH
python26 setup.py install --prefix=$RPM_BUILD_ROOT%{prefix}

%clean


%files
