%define name	siesta
%define dist	rocks
%define release	1
%define version 3.0
%define prefix	/share/apps
%define inst	%{name}-%{version}-rc2

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
Source:		siesta-3.0-rc2.tgz
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
../Src/configure --prefix=%{prefix} --with-blas=%{prefix}/lib/libblas.a --with-lapack=%{prefix}/lib/liblapack.a --with-scalapack=%{prefix}/lib/libscalapack.a --with-blacs=%{prefix}/lib/blacs.a
make


%install
cd Obj/
mkdir -p $RPM_BUILD_ROOT/%{prefix}/bin
cp siesta $RPM_BUILD_ROOT/%{prefix}/bin/

%clean


%files
/share/apps/bin/siesta
