%define name	matplot
%define dist	rocks
%define release	1
%define version 1.1.0
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	PSF
URL:		http://matplotlib.sourceforge.net/
Source:		%{name}lib-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	python26-devel
BuildRequires:	numpy
BuildRequires:	geos-devel
Requires:	glibc
Requires:	python26
Requires:	python26-numpy
Requires:	geos
Summary:	Matplot

%description
Matplot for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n %{name}lib-%{version}


%build
export GEOS_DIR=/usr
export PYTHONPATH=/share/apps/lib/python2.6/site-packages:/share/apps/lib64/python2.6/site-packages:$PYTHONPATH
python26 setup.py build


%install
export GEOS_DIR=/usr
export PYTHONPATH=/share/apps/lib/python2.6/site-packages:/share/apps/lib64/python2.6/site-packages:$PYTHONPATH
python26 setup.py install --prefix=$RPM_BUILD_ROOT%{prefix}


%clean


%files
