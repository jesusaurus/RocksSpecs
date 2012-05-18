%define name	repast-hpc
%define dist	rocks
%define release	1
%define version 1.0.1
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
URL:		http://repast.sourceforge.net/
Source:		repasthpc-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	netcdf
BuildRequires:	hdf5
Requires:	netcdf
Requires:	hdf5
Summary:	Repast HPC

%description
Repast HPC for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n repasthpc-%{version}


%build
CFLAGS="-I/share/apps/include" CPPFLAGS=$CFLAGS LDFLAGS="-L/share/apps/lib -L/share/apps/lib64" ./configure --with-pic --with-gnu-ld --with-boost=/share/apps/ --prefix=$RPM_BUILD_ROOT/%{prefix}
make


%install
make install


%clean
rm -rf $RPM_BUILD_ROOT


%files
   /share/apps/include/relogo/
   /share/apps/include/repast_hpc/
   /share/apps/lib/librelogo-1.0.1.a
   /share/apps/lib/librelogo-1.0.1.la
   /share/apps/lib/librelogo-1.0.1.so
   /share/apps/lib/librelogo-1.0.1.so.0
   /share/apps/lib/librelogo-1.0.1.so.0.0.0
   /share/apps/lib/librepast_hpc-1.0.1.a
   /share/apps/lib/librepast_hpc-1.0.1.la
   /share/apps/lib/librepast_hpc-1.0.1.so
   /share/apps/lib/librepast_hpc-1.0.1.so.0
   /share/apps/lib/librepast_hpc-1.0.1.so.0.0.0

