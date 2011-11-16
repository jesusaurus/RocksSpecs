%define name	scalapack
%define dist	rocks
%define release	2
%define version 1.8.0
%define prefix	/share/apps
%define inst	%{name}-%{version}

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
Source:		%{inst}.tgz
Source1:	SLmake.rocks
Requires:	atlas
Requires:	blacs
BuildRequires:	atlas
BuildRequires:	blacs
Summary:	ScaLAPACK

%description
ScaLAPACK for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -q


%build
cp $RPM_SOURCE_DIR/SLmake.rocks $RPM_BUILD_DIR/%{inst}/SLmake.inc
sed -i "22 s!home!home = $RPM_BUILD_DIR/%{inst}!" $RPM_BUILD_DIR/%{inst}/SLmake.inc #inline patches, eww :(
make

%install
mkdir -p $RPM_BUILD_ROOT/%{prefix}/lib
cp $RPM_BUILD_DIR/%{inst}/libscalapack.a $RPM_BUILD_ROOT/%{prefix}/lib/


%clean


%files
/share/apps/lib/libscalapack.a
