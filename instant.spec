%define name	Instant
%define dist	rocks
%define release	1
%define version 1.0.0
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
URL:		https://launchpad.net/instant
Source:		http://launchpad.net/instant/1.0.x/1.0.0/+download/instant-1.0.0.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	python26
Requires:	python26
Summary:	Instant

%description
Instant for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup -n instant-1.0.0

%build


%install
python26 setup.py install --prefix=$RPM_BUILD_ROOT%{prefix}

%clean


%files
     /share/apps/bin/instant-clean
     /share/apps/bin/instant-showcache
     /share/apps/lib/python2.6/site-packages/instant-1.0.0-py2.6.egg-info
     /share/apps/lib/python2.6/site-packages/instant/
%doc /share/apps/share/man/man1/instant-clean.1.gz
%doc /share/apps/share/man/man1/instant-showcache.1.gz
