%define name	boost
%define dist	rocks
%define release	1
%define version 1.48.0
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
URL:		http://www.boost.org/
Source:		http://sourceforge.net/projects/boost/files/boost/1.48.0/boost_1_48_0.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
Summary:	Boost %{version}

%description
Boost %{version} for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup -n boost_1_48_0

%build
./bootstrap.sh --prefix=$RPM_BUILD_ROOT%{prefix}

%install
./b2 --with-mpi --debug-configuration install

%clean


%files
   /share/apps/include/boost
   /share/apps/lib/libboost_mpi.a
   /share/apps/lib/libboost_mpi.so
   /share/apps/lib/libboost_mpi.so.1.48.0
   /share/apps/lib/libboost_mpi_python.a
   /share/apps/lib/libboost_mpi_python.so
   /share/apps/lib/libboost_mpi_python.so.1.48.0
   /share/apps/lib/libboost_python.a
   /share/apps/lib/libboost_python.so
   /share/apps/lib/libboost_python.so.1.48.0
   /share/apps/lib/libboost_serialization.a
   /share/apps/lib/libboost_serialization.so
   /share/apps/lib/libboost_serialization.so.1.48.0
   /share/apps/lib/mpi.so

