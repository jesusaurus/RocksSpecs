%define name	viper
%define dist	rocks
%define release	1
%define version 1.0.0
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
URL:		https://launchpad.net/fenics-viper
Source:		http://launchpad.net/fenics-viper/1.0.x/1.0.0/+download/viper-1.0.0.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	python
Requires:	python
Summary:	Viper

%description
Viper for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup -n viper-1.0.0

%build
python setup.py build


%install
python setup.py install --prefix=$RPM_BUILD_ROOT%{prefix}

%clean


%files
     /share/apps/bin/viper
     /share/apps/lib/python2.6/site-packages/viper-1.0.0-py2.6.egg-info
     /share/apps/lib/python2.6/site-packages/viper/
%doc /share/apps/share/man/man1/viper.1.gz
