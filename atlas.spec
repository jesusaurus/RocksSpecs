%define name	atlas
%define dist	rocks
%define release	1
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
Summary:	The ATLAS BLAS/LAPACK implementation.

%description
ATLAS BLAS/LAPACK implementation for a Rocks Cluster.  Not intended for distribution, tuned for rocks.research.pdx.edu.

%prep
%setup -n ATLAS
%patch0

cd $RPM_BUILD_DIR/ATLAS
mkdir LINUX


%build

cd $RPM_BUILD_DIR/ATLAS/LINUX
sed -i 's!\(DESTDIR\)=\([^ ]*\)!\1 \?= \2!' ../configure #we need a ?= instead of the =
../configure -Fa alg -fPIC --with-netlib-lapack-tarfile=$RPM_SOURCE_DIR/lapack-%{lversion}.tgz --shared --prefix=%{prefix}
make; make shared


%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}

cd $RPM_BUILD_DIR/ATLAS/LINUX
export DESTDIR=$RPM_BUILD_ROOT
make install


%clean
cd $RPM_BUILD_DIR
rm -rf ATLAS


%files
%defattr(-,root,root,-)
/include/atlas/
/include/cblas.h
/include/clapack.h
/lib/libatlas.a
/lib/libcblas.a
/lib/libf77blas.a
/lib/liblapack.a
/lib/libptcblas.a
/lib/libptf77blas.a
/lib/libsatlas.so
/lib/libtatlas.so
