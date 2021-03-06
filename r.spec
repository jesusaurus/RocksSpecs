%define name	R
%define dist	rocks
%define release	2
%define version 2.15.1
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	GPL
URL:		http://www.r-project.org/
Source:		R-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	readline-devel
BuildRequires:	atlas-devel
Requires:	readline
Requires:	atlas
Summary:	R Project for Statistical Computing

%description
R Project for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup


%build
BLAS_LIBS="-L/share/apps/lib -lcblas -lf77blas -latlas" LAPACK_LIBS="-L/share/apps/lib -llapack" ./configure --prefix=%{prefix} --with-blas --with-lapack --enable-R-shlib
make


%install
DESTDIR="$RPM_BUILD_ROOT" make install


%clean
rm -r "$RPM_BUILD_ROOT"


%files
%{prefix}/bin/R
%{prefix}/bin/Rscript
%{prefix}/lib64/R
%{prefix}/lib64/pkgconfig/libR.pc
%doc %{prefix}/share/man/man1/
