%define name    hdf5
%define dist    rocks
%define release 1
%define version 1.8.8

Name:           %{name}
Version:        %{version}
Release:        %{dist}.%{release}
Group:          Rocks
License:       	Other
URL:		http://hdfgroup.org/
Source0:        hdf5-1.8.8.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:         /share/apps
Summary:        Parallel HDF5

%description
Parallel HDF5 with Fortran support for a Rocks Cluster.  Not intended for redistribution.

%prep
%setup


%build
cd $RPM_BUILD_DIR/%{name}-%{version}
CC=mpicc LDFLAGS="-L/share/apps/lib $LDFLAGS" CPPFLAGS="-I/share/apps/include $CPPFLAGS" ./configure --prefix=/share/apps --enable-parallel --enable-fortran"
make


%install
cd $RPM_BUILD_DIR/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT/
mkdir -p $RPM_BUILD_ROOT/
DESTDIR=$RPM_BUILD_ROOT make install


%clean
cd $RPM_BUILD_ROOT
rm -rf %{name}-%{version}


%files
