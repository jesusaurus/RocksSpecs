%define name	siesta
%define dist	rocks
%define release	3
%define version 3.1
%define prefix	/share/apps
%define inst	%{name}-%{version}

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
Source:		siesta-%{version}.tgz
Requires:	scalapack
BuildRequires:	scalapack
Summary:	Siesta

%description
Siesta for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n %{inst} -q


%build
cd $RPM_BUILD_DIR/%{inst}
mkdir -p $RPM_BUILD_ROOT%{prefix}
cd Obj/
../Src/obj_setup.sh
../Src/configure --prefix=%{prefix} --with-blas="-L/share/apps/lib -lcblas -lf77blas -latlas" --with-lapack="-L/share/apps/lib -llapack" --with-scalapack=%{prefix}/lib/libscalapack.a --with-blacs=%{prefix}/lib/libscalapack.a --enable-mpi
make


%install
cd Obj/
mkdir -p $RPM_BUILD_ROOT/%{prefix}/bin
cp siesta $RPM_BUILD_ROOT/%{prefix}/bin/

%clean


%files
/share/apps/bin/siesta
