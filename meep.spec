%define name	meep
%define dist	rocks
%define release	4
%define version 1.2

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/share/apps
Requires:	atlas
Requires:	guile
Requires:	hdf5
Requires:	harminv
Requires:	fftw
Requires:	gsl
Requires:	libctl
BuildRequires:	atlas-devel
BuildRequires:	guile-devel
BuildRequires:	hdf5-devel
BuildRequires:	h5utils-devel
BuildRequires:	harminv
BuildRequires:	fftw-devel
BuildRequires:	gsl-devel
BuildRequires:	libctl
Summary:	Meep %{version} with libctl %{cversion}

%description
Meep for a Rocks Cluster.  Not intended for redistribution.

%prep
%setup


%build
cd ../meep-%{version}
F77=mpif77 CC=mpicc CXX=mpiCC MPICXX=mpiCC MPILIBS="-lmpi" LDFLAGS="-L/share/apps/lib -L/opt/openmpi/lib $LDFLAGS" CPPFLAGS="-I/share/apps/include -I/opt/openmpi/include -DH5_USE_16_API=1 $CPPFLAGS" ./configure --with-mpi --with-libctl=/share/apps/share/libctl --prefix=/share/apps
make


%install
cd $RPM_BUILD_DIR/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT/
mkdir -p $RPM_BUILD_ROOT/share/apps
DESTDIR=$RPM_BUILD_ROOT make install


%clean
cd $RPM_BUILD_DIR
rm -rf %{name}-%{version}

%files
/share/apps/bin/meep-mpi
/share/apps/include/meep.hpp
/share/apps/include/meep/mympi.hpp
/share/apps/include/meep/vec.hpp
/share/apps/lib/libmeep_mpi.a
/share/apps/lib/libmeep_mpi.la
/share/apps/lib/pkgconfig/meep_mpi.pc
/share/apps/share/meep/casimir.scm
/share/apps/share/meep/meep-enums.scm
/share/apps/share/meep/meep.scm
