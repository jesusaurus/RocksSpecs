%define name	fenics
%define dist	rocks
%define release	1
%define version 0

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		/share/apps
Requires:	ffc
Requires:	fiat
Requires:	instant
Requires:	viper
Requires:	ufl
Requires:	dolfin
Requires:	ufc
Summary:	Fenics Project Meta-Package

%description
Fenics Project meta-project for a Rocks Cluster.  Not intended for redistribution.
Contains FFC, FIAT, Instant, Viper, UFL, Dolfin, and UFC.

%prep
mkdir -p $RPM_BUILD_ROOT


%build


%install


%clean
rmdir $RPM_BUILD_ROOT


%files
