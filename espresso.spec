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
%setup -T -D -a 1 -n %{inst}


%build
cd $RPM_BUILD_DIR/%{inst}
mkdir -p $RPM_BUILD_ROOT%{prefix}
./configure --enable-parallel CC=mpicc LIBDIRS="/share/apps/lib /opt/openmpi/lib" FFLAGS="-I/opt/openmpi/include" CFLAGS="-I/opt/openmpi/include"
make pwall want


%install
mkdir -p $RPM_BUILD_ROOT/%{prefix}/bin
cd $RPM_BUILD_DIR/%{inst}
cp bin/* $RPM_BUILD_ROOT/%{prefix}/bin/
cp WANT/bin/* $RPM_BUILD_ROOT/%{prefix}/bin/

%clean


%files
