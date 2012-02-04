%define name	lapack
%define dist	rocks
%define release	1
%define version 3.4.0
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
Source0:	%{name}-%{version}.tgz
Patch0:		%{name}-%{version}.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
Summary:	Linear Algebra PACKage.

%description
Linear Algebra PACKage for a Rocks Cluster.  Not intended for distribution.

%prep
cd $RPM_BUILD_DIR
%setup
cd $RPM_BUILD_DIR/%{name}-%{version}
cp INSTALL/make.inc.gfortran make.inc
%patch


%build
make blaslib lapacklib tmglib


%install
mkdir -p $RPM_BUILD_ROOT/%{prefix}/lib/
cp librefblas.so liblapack.so libtmglib.so $RPM_BUILD_ROOT/%{prefix}/lib/


%clean
cd $RPM_BUILD_DIR
rm -rf %{name}-%{version}


%files
   /share/apps/lib/liblapack.so
   /share/apps/lib/librefblas.so
   /share/apps/lib/libtmglib.so

