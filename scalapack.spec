%define name	scalapack
%define dist	rocks
%define release	1
%define version 2.0.1
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
BuildRequires:	atlas
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
#cp $RPM_BUILD_DIR/%{inst}/libscalapack.a $RPM_BUILD_ROOT/%{prefix}/lib/
make install


%clean


%files
