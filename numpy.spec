%define name	numpy
%define dist	rocks
%define release	1
%define version 1.6.2
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
URL:		http://www.scipy.org/
Source:		numpy-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
Summary:	NumPy

%description
NumPy for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n numpy-%{version}

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
python setup.py build


%install
mkdir -p $RPM_BUILD_ROOT%{prefix}
python setup.py install --prefix=$RPM_BUILD_ROOT%{prefix}


%clean


%files
/share/apps/bin/f2py
/share/apps/lib64/python2.6/site-packages/numpy-%{version}-py2.6.egg-info
/share/apps/lib64/python2.6/site-packages/numpy/

