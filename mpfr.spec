%define name	mpfr
%define dist	rocks
%define release	1
%define version 3.0.1
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
Requires:	gmp
BuildRequires:	gmp-devel
Summary:	mpfr

%description
mpfr for a Rocks Cluster.  Not intended for redistribution.

%prep
%setup


%build
cd $RPM_BUILD_DIR/%{name}-%{version}
export LDFLAGS="-L/share/apps/lib $LDFLAGS" 
export CPPFLAGS="-I/share/apps/include $CPPFLAGS" 
./configure --prefix=%{prefix}
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

/share/apps/include/mpf2mpfr.h
/share/apps/include/mpfr.h
/share/apps/lib/libmpfr.a
/share/apps/lib/libmpfr.la
/share/apps/lib/libmpfr.so
/share/apps/lib/libmpfr.so.4
/share/apps/lib/libmpfr.so.4.0.1
%doc /share/apps/share/doc/mpfr/AUTHORS
%doc /share/apps/share/doc/mpfr/BUGS
%doc /share/apps/share/doc/mpfr/COPYING
%doc /share/apps/share/doc/mpfr/COPYING.LESSER
%doc /share/apps/share/doc/mpfr/FAQ.html
%doc /share/apps/share/doc/mpfr/NEWS
%doc /share/apps/share/doc/mpfr/TODO
%doc /share/apps/share/doc/mpfr/examples/ReadMe
%doc /share/apps/share/doc/mpfr/examples/divworst.c
%doc /share/apps/share/doc/mpfr/examples/rndo-add.c
%doc /share/apps/share/doc/mpfr/examples/sample.c
%doc /share/apps/share/doc/mpfr/examples/version.c
%doc /share/apps/share/info/mpfr.info

