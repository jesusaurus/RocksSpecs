%define name	blacs
%define dist	rocks
%define release	1
%define version 1.1
%define prefix	/share/apps
%define inst	BLACS

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
Source0:	mpiblacs.tgz
Source1:	mpiblacs-patch03.tgz
Requires:	atlas
BuildRequires:	atlas
Summary:	BLACS

%description
BLACS for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n %{inst} -q
%setup -T -b 1
exit


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

