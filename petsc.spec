%define name	petsc
%define dist	rocks
%define release	1
%define version 3.2.7
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	Other
URL:		http://www.mcs.anl.gov/petsc/index.html
Source:		http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.2-p7.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	boost
BuildRequires:	FFC
BuildRequires:	fftw
BuildRequires:	FIAT
BuildRequires:  python-scientific
BuildRequires:  python26-numpy
BuildRequires:  valgrind-devel
Requires:	boost
Requires:	FFC
Requires:	fftw
Requires:	FIAT
Requires:       python-scientific
Requires:       python26-numpy
Requires:       valgrind
Summary:	Portable, Extensible Toolkit for Scientific Computation

%description
PETSc for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n petsc-3.2-p7


%build
python26 configure --with-blas-lapack-dir=/share/apps/lib --download-blacs=yes --with-mpi-dir=/opt/openmpi --with-hdf5-dir=/share/apps --with-umfpack-dir=/share/apps --with-scalapack-dir=/share/apps/ --with-numpy=/share/apps/lib64/python2.6/site-packages/numpy  --with-fiat-dir=/share/apps/lib/python2.6/site-packages/FIAT --with-scientificpython-dir=/share/apps/lib64/python2.6/site-packages/Scientific --with-x=0 --prefix=$RPM_BUILD_ROOT/%{prefix}
make all test


%install
make install


%clean
rm -r $RPM_BUILD_ROOT
rm -r $RPM_BUILD_DIR/%{name}-%{version}


%files

