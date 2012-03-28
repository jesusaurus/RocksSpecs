%define name	FIAT
%define dist	rocks
%define release	1
%define version 1.0.0
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
URL:		https://launchpad.net/fiat
Source:		http://launchpad.net/fiat/1.0.x/1.0.0/+download/fiat-1.0.0.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	python26
Requires:	python26
Summary:	FIAT

%description
FIAT for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup -n fiat-1.0.0

%build


%install
python26 setup.py install --prefix=$RPM_BUILD_ROOT%{prefix}

%clean


%files
   /share/apps/lib/python2.6/site-packages/FIAT-1.0.0-py2.6.egg-info
   /share/apps/lib/python2.6/site-packages/FIAT/
