%define name    Dolfin
%define dist    rocks
%define release 1
%define version 1.0.0
%define prefix  /share/apps
%define inst    dolfin-%{version}

Name:           %{name}
Version:        %{version}
Release:        %{dist}.%{release}
Group:          Rocks
License:        unknown
URL:            https://launchpad.net/dolfin
Source:         http://launchpad.net/dolfin/1.0.x/1.0.0/+download/dolfin-1.0.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:         %{prefix}
BuildRequires:  cmake
BuildRequires:  boost
BuildRequires:  UFC
BuildRequires:  armadillo
Requires:       boost
Requires:       UFC
Requires:       armadillo
Summary:        Dolfin

%description
Dolfin for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup -n %{inst}
cp -rf $RPM_SOURCE_DIR/dolfin-cmake/* $RPM_BUILD_DIR/%{inst}/cmake/modules/


%build
export PYTHONPATH=/share/apps/:$PYTHONPATH
cmake -DCMAKE_PREFIX_PATH=/share/apps -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT%{prefix} -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python26 -DPYTHON_INCLUDE_PATH:PATH=/usr/include/python2.6/:/share/apps/ -DPYTHON_LIBRARY:FILEPATH=/usr/lib64/libpython2.6.so.1.0 -DUFC_DIR=/share/apps/ -DBLAS_LIBRARIES='-L/share/apps/lib -lamd -lcblas -lf77blas -lptcblas -lptf77blas -latlas' -DLAPACK_LIBRARIES='-L /share/apps/lib -llapack' -DARMADILLO_DIR=/share/apps -DUMFPACK_DIR=/share/apps/ -DSWIG_DIR=/share/apps/ .
make

%install
make install

%clean


%files

