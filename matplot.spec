%define name	matplot
%define dist	rocks
%define release	1
%define version 1.0.2
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	PSF
URL:		http://matplotlib.sourceforge.net/
Source:		basemap-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	python26-devel
BuildRequires:	python26-numpy
BuildRequires:	geos-devel
Requires:	glibc
Requires:	python26
Requires:	python26-numpy
Requires:	geos
Summary:	Matplot

%description
Matplot for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n basemap-%{version}


%build
export GEOS_DIR=/usr
python26 setup.py build


%install
export GEOS_DIR=/usr
python26 setup.py install --prefix=$RPM_BUILD_ROOT%{prefix}


%clean


%files
/share/apps/lib64/python2.6/site-packages/_geoslib.so
/share/apps/lib64/python2.6/site-packages/basemap-1.0.2-py2.6.egg-info
/share/apps/lib64/python2.6/site-packages/mpl_toolkits/
