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
Source2:	Bmake.rocks
Requires:	atlas
BuildRequires:	atlas
Summary:	BLACS

%description
BLACS for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n %{inst} -q
%setup -T -D -b 1 -n %{inst}


%build
cd $RPM_BUILD_DIR/%{inst}
mkdir -p $RPM_BUILD_ROOT/share/apps
cp $RPM_SOURCE_DIR/Bmake.rocks $RPM_BUILD_DIR/%{inst}/Bmake.inc

echo "
BTOPdir = $RPM_BUILD_DIR/%{inst}
" >> $RPM_BUILD_DIR/%{inst}/Bmake.inc

make mpi

%install
mkdir -p $RPM_BUILD_ROOT/%{prefix}/lib
cp -R $RPM_BUILD_DIR/%{inst}/LIB/*MPI.a $RPM_BUILD_ROOT/%{prefix}/lib/

%clean


%files
   /share/apps/lib/blacs_MPI.a
   /share/apps/lib/blacsCinit_MPI.a
   /share/apps/lib/blacsF77init_MPI.a

