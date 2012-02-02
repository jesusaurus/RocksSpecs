%define name	python26-numpy
%define dist	rocks
%define release	1
%define version 1.6.1
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
BuildRequires:	python26-devel
Requires:	python26
Summary:	NumPy

%description
NumPy for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n numpy-%{version}


%build
export BLAS=/share/apps/lib/libblas.a
export LAPACK=/share/apps/lib/liblapack.a
export ATLAS=/share/apps/lib/libatlas.a
python26 setup.py build


%install
mkdir -p $RPM_BUILD_ROOT%{prefix}
python26 setup.py install --prefix=$RPM_BUILD_ROOT%{prefix}


%clean


%files
/share/apps/bin/f2py26
/share/apps/lib64/python2.6/site-packages/numpy-1.6.1-py2.6.egg-info
/share/apps/lib64/python2.6/site-packages/numpy/
