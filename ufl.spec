%define name	UFL
%define dist	rocks
%define release	1
%define version 1.0.0
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
URL:		https://launchpad.net/ufl
Source:		http://launchpad.net/ufl/1.0.x/1.0.0/+download/ufl-1.0.0.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	python26
Requires:	python26
Summary:	UFL

%description
UFL for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup -n ufl-1.0.0

%build


%install
python26 setup.py install --prefix=$RPM_BUILD_ROOT%{prefix}

%clean


%files
     /share/apps/bin/form2ufl
     /share/apps/bin/ufl-analyse
     /share/apps/bin/ufl-convert
     /share/apps/bin/ufl-version
     /share/apps/bin/ufl2py
     /share/apps/lib/python2.6/site-packages/UFL-1.0.0-py2.6.egg-info
     /share/apps/lib/python2.6/site-packages/ufl/
%doc /share/apps/share/man/man1/form2ufl.1.gz
%doc /share/apps/share/man/man1/ufl-analyse.1.gz
%doc /share/apps/share/man/man1/ufl-convert.1.gz
%doc /share/apps/share/man/man1/ufl-version.1.gz
%doc /share/apps/share/man/man1/ufl2py.1.gz 
