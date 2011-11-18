%define name		quantum-espresso
%define dist		rocks
%define release		1
%define version		4.3
%define wversion	2.1.1
%define prefix		/share/apps
%define inst		espresso-%{version}

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
Source0:	espresso-%{version}.tar.gz
Source1:	want-%{wversion}.tar.gz
Summary:	Quantum Espresso with WanT

%description
Quantum Espresso with WanT plugin for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n %{inst} -q
%setup -T -a 1


%build
cd $RPM_BUILD_DIR/%{inst}
mkdir -p $RPM_BUILD_ROOT%{prefix}
./configure --enable-parallel CC=mpicc LIBDIRS="/share/apps/lib"
make want


%install
mkdir -p $RPM_BUILD_ROOT/%{prefix}/bin
cp bin/* $RPM_BUILD_ROOT/%{prefix}/bin/

%clean


%files
