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
Requires:	boost
Requires:	FFC
Requires:	fftw
Requires:	FIAT
Requires:       python-scientific
Requires:       python26-numpy
Summary:	Portable, Extensible Toolkit for Scientific Computation

%description
PETSc for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n petsc-3.2-p7


%build
./configure --with-cxx=mpiCC --with-boost-dir=/share/apps/ --with-mpi-dir=/opt/openmpi --with-fftw=1 --with-numpy=/share/apps/lib64/python2.6/site-packages/numpy --with-ffc-dir=/share/apps/lib/python2.6/site-packages/ffc --with-fiat-dir=/share/apps/lib/python2.6/site-packages/FIAT --with-scientificpython-dir=/share/apps/lib64/python2.6/site-packages/Scientific --with-x=0 --prefix=%{prefix}
make all test


%install


%clean
rm -r $RPM_BUILD_ROOT
rm -r $RPM_BUILD_DIR/%{name}-%{version}


%files

