%define name	atlas
%define dist	rocks
%define release	2
%define version 3.10.0
%define lversion 3.4.1
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
Source0:	%{name}%{version}.tar.bz2
Source1:	http://www.netlib.org/lapack/lapack-%{lversion}.tgz
Patch0:		atlas.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
Provides:       atlas
Provides:       atlas-devel
Provides:       atlas-3dnow
Provides:       atlas-sse3
Summary:	The ATLAS BLAS/LAPACK implementation.

%description
ATLAS BLAS/LAPACK implementation for a Rocks Cluster.  Not intended for distribution, tuned for rocks.research.pdx.edu.

%prep
%setup -n ATLAS
%patch0

cd $RPM_BUILD_DIR/ATLAS
mkdir LINUX


%build
# make sure that cpu throttling is off
# /usr/bin/cpufreq-selector -g performance

cd $RPM_BUILD_DIR/ATLAS/LINUX
sed -i 's!\(DESTDIR\)=\([^ ]*\)!\1 \?= \2!' ../configure #we need a ?= instead of the =
../configure -Fa alg -fPIC --with-netlib-lapack-tarfile=$RPM_SOURCE_DIR/lapack-%{lversion}.tgz --shared --prefix=%{prefix}
make; make shared


%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}

cd $RPM_BUILD_DIR/ATLAS/LINUX
export DESTDIR=$RPM_BUILD_ROOT%{prefix}
make install


%clean
cd $RPM_BUILD_DIR
rm -rf ATLAS


%files
%defattr(-,root,root,-)
/share/apps/include/atlas/
/share/apps/include/cblas.h
/share/apps/include/clapack.h
/share/apps/lib/libatlas.a
/share/apps/lib/libcblas.a
/share/apps/lib/libf77blas.a
/share/apps/lib/liblapack.a
/share/apps/lib/libptcblas.a
/share/apps/lib/libptf77blas.a
/share/apps/lib/libsatlas.so
/share/apps/lib/libtatlas.so
