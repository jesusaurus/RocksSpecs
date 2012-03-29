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
Requires:	FFC
Requires:	FIAT
Requires:	Instant
Requires:	Viper
Requires:	UFL
Requires:	Dolfin
Requires:	UFC
Summary:	Fenics Project Meta-Package

%description
Fenics Project meta-project for a Rocks Cluster.  Not intended for redistribution.
Contains FFC, FIAT, Instant, Viper, UFL, Dolfin, and UFC.

%prep


%build


%install


%clean


%files
