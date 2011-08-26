%define name	atlas
%define dist	rocks
%define release	1
%define version 3.8.4

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
Source0:	%{name}%{version}.tar.bz2
Source1:	AMD.tar.gz
Source2:	UMFPACK.tar.gz
Source3:	UFconfig.tar.gz
Source4:	lapack-3.2.2.tgz
Patch0:		UFconfig.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/share/apps
Summary:	The ATLAS BLAS implementation.

%description
ATLAS BLAS implementation for a Rocks Cluster.  Not intended for distribution, tuned for rocks.research.pdx.edu.

%prep
#env; exit
cd $RPM_BUILD_DIR
rm -rf ATLAS
tar -jxvf $RPM_SOURCE_DIR/%{name}%{version}.tar.bz2
if [ $? -ne 0 ]; then
  exit $?
fi

%setup -n sparse -T -a 1 -c
%setup -n sparse -D -T -a 2
%setup -n sparse -D -T -a 3
%patch
%setup -T -b 4

cd $RPM_BUILD_DIR/ATLAS
mkdir ATLAS_LINUX


%build
cd $RPM_BUILD_DIR/ATLAS/ATLAS_LINUX
../configure -Fa alg -fPIC -Si cputhrchk 0 -Ss flapack $RPM_BUILD_DIR/lapack-3.2.2 --prefix=/share/apps
sed -i '113 s/gcc/gcc -fPIC/' src/blas/gemv/Make.inc #inline patch, eww :(
make
cd lib
make shared; make ptshared

cd $RPM_BUILD_DIR/sparse/UMFPACK
make library


%install
cd $RPM_BUILD_DIR/ATLAS/ATLAS_LINUX
DESTDIR=$RPM_BUILD_ROOT make install
cd ../../sparse/UMFPACK
DESTDIR=$RPM_BUILD_ROOT make install
cd ../AMD
DESTDIR=$RPM_BUILD_ROOT make install


%clean
cd $RPM_BUILD_DIR
rm -rf ATLAS
rm -rf sparse


%files
