%define name	netcdf
%define dist	rocks
%define release	1
%define version 4.1.3
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	NetCDF
URL:		http://www.unidata.ucar.edu/software/netcdf/
Source:		http://www.unidata.ucar.edu/downloads/netcdf/ftp/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	hdf5
Requires:	hdf5
Summary:	NetCDF

%description
NetCDF for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup


%build
LDFLAGS='-L/share/apps/lib64 -L/share/apps/lib -L/opt/openmpi/lib -lmpi' CFLAGS='-I/share/apps/include -I/opt/openmpi/include' CPPFLAGS='-I/share/apps/include -I/opt/openmpi/include'  ./configure --prefix=$RPM_BUILD_ROOT/%{prefix}
make


%install
make install


%clean
rm -rf $RPM_BUILD_ROOT 


%files
   /share/apps/bin/nc-config
   /share/apps/bin/nccopy
   /share/apps/bin/ncdump
   /share/apps/bin/ncgen
   /share/apps/bin/ncgen3
   /share/apps/include/ncvalues.h
   /share/apps/include/netcdf.h
   /share/apps/include/netcdf.hh
   /share/apps/include/netcdf.inc
   /share/apps/include/netcdf.mod
   /share/apps/include/netcdf_par.h
   /share/apps/include/netcdfcpp.h
   /share/apps/include/typesizes.mod
   /share/apps/lib/libnetcdf.a
   /share/apps/lib/libnetcdf.la
   /share/apps/lib/libnetcdf.so
   /share/apps/lib/libnetcdf.so.7
   /share/apps/lib/libnetcdf.so.7.1.1
   /share/apps/lib/libnetcdf_c++.a
   /share/apps/lib/libnetcdf_c++.la
   /share/apps/lib/libnetcdf_c++.so
   /share/apps/lib/libnetcdf_c++.so.4
   /share/apps/lib/libnetcdf_c++.so.4.1.0
   /share/apps/lib/libnetcdff.a
   /share/apps/lib/libnetcdff.la
   /share/apps/lib/libnetcdff.so
   /share/apps/lib/libnetcdff.so.5
   /share/apps/lib/libnetcdff.so.5.1.0
   /share/apps/lib/pkgconfig/netcdf.pc
   /share/apps/share/info/netcdf-c.info
   /share/apps/share/info/netcdf-c.info-1
   /share/apps/share/info/netcdf-c.info-2
   /share/apps/share/info/netcdf-cxx.info
   /share/apps/share/info/netcdf-f77.info
   /share/apps/share/info/netcdf-f77.info-1
   /share/apps/share/info/netcdf-f77.info-2
   /share/apps/share/info/netcdf-f90.info
   /share/apps/share/info/netcdf-install.info
   /share/apps/share/info/netcdf-tutorial.info
   /share/apps/share/info/netcdf.info
   /share/apps/share/man/man1/nccopy.1
   /share/apps/share/man/man1/ncdump.1
   /share/apps/share/man/man1/ncgen.1
   /share/apps/share/man/man1/ncgen3.1
   /share/apps/share/man/man3/netcdf.3
   /share/apps/share/man/man3/netcdf_f77.3
   /share/apps/share/man/man3/netcdf_f90.3

