%define name	harminv
%define dist	rocks
%define release	1
%define version 1.3.1

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
BuildRequires:	atlas
BuildRequires:	hdf5
BuildRequires:	guile-devel
Summary:	Harminv 1.3.1

%description
Harminv for a Rocks Cluster.  Not intended for redistribution.

%prep
%setup


%build
cd $RPM_BUILD_DIR/%{name}-%{version}
export F77=mpif77
export LDFLAGS="-L/share/apps/lib $LDFLAGS" 
export CPPFLAGS="-I/share/apps/include $CPPFLAGS" 
./configure --prefix=/share/apps --with-lapack=/share/apps/lib/liblapack.a
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
/share/apps/bin/harminv
/share/apps/include/harminv.h
/share/apps/lib/libharminv.a
/share/apps/lib/libharminv.la
/share/apps/lib/pkgconfig/harminv.pc
%doc /share/apps/man/man1/harminv.1

