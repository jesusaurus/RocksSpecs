%define name	meep
%define dist	rocks
%define release	1
%define version 1.1.1

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
Source0:	%{name}-%{version}.tar.gz
Source1:	libctl-3.1.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/share/apps
Requires:	atlas
Requires:	guile
Requires:	hdf5 
Requires:	harminv
Requires:	libctl
BuildRequires:	atlas
BuildRequires:	guile-devel
BuildRequires:	hdf5-devel
BuildRequires:	harminv
BuildRequires:	libctl
Summary:	Meep 1.1.1 with Harminv 1.3.1 and libCtl 3.1

%description
Meep for a Rocks Cluster.  Not intended for redistribution.

%prep
%setup
%setup -n libctl-3.1 -T -b 1


%build
cd ../meep-1.1.1
F77=gfortran LDFLAGS="-L/share/apps/lib" CPPFLAGS="-I/share/apps/include" ./configure --with-libctl=$RPM_BUILD_DIR/libctl-3.1 --with-mpi=/opt/openmpi/lib --prefix=/share/apps
make


%install
cd $RPM_BUILD_DIR/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT/
mkdir -p $RPM_BUILD_ROOT/
DESTDIR=$RPM_BUILD_ROOT make install


%clean
cd $RPM_BUILD_DIR
rm -rf %{name}-%{version}

%files
/share/apps/bin/meep
/share/apps/include/meep.hpp
/share/apps/include/meep/mympi.hpp
/share/apps/include/meep/vec.hpp
/share/apps/lib/libmeep.a
/share/apps/lib/libmeep.la
/share/apps/lib/pkgconfig/meep.pc
/share/apps/share/meep/casimir.scm
/share/apps/share/meep/meep-enums.scm
/share/apps/share/meep/meep.scm
