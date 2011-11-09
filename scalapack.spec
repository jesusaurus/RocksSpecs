%define name	scalapack
%define dist	rocks
%define release	1
%define version 1.8.0
%define prefix	/share/apps
%define inst	%{name}_installer_0.96

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
Source:		http://www.netlib.org/scalapack/scalapack_installer.tgz
Requires:	atlas
BuildRequires:	atlas
BuildRequires:	python
Summary:	ScaLAPACK and BLACS

%description
ScaLAPACK and BLACS for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n %{inst} -q


%build
cd $RPM_BUILD_DIR/%{inst}
mkdir -p $RPM_BUILD_ROOT/share/apps
./setup.py --prefix=$RPM_BUILD_ROOT/share/apps --blaslib=/share/apps/lib/libblas.a --lapacklib=/share/apps/lib/liblapack.a  


%install
mkdir -p %{prefix}
cp -R $RPM_BUILD_ROOT%{prefix}/* %{prefix}/

%clean


%files
   /share/apps/lib/blacs.a
   /share/apps/lib/blacsC.a
   /share/apps/lib/blacsF77.a
   /share/apps/lib/libscalapack.a
   /share/apps/log/blacslog
   /share/apps/log/scalog

