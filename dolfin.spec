%define name    dolfin
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
BuildRequires:  ufc
BuildRequires:  armadillo
BuildRequires:  atlas
Requires:       boost
Requires:       ufc
Requires:       armadillo
Summary:        Dolfin

%description
Dolfin for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup -n %{inst}
cp -rf $RPM_SOURCE_DIR/dolfin-cmake/* $RPM_BUILD_DIR/%{inst}/


%build
export PYTHONPATH=/share/apps/lib/python2.6/site-packages/:/share/apps/lib64/python2.6/site-packages/:$PYTHONPATH
mkdir build
cd build
cmake -DCMAKE_PREFIX_PATH=/share/apps -DCMAKE_INSTALL_PREFIX=%{prefix} -DUFC_DIR=/share/apps/ -DARMADILLO_DIR=/share/apps -DUMFPACK_DIR=/share/apps/ -DSWIG_DIR=/share/apps/ ..
make

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -r $RPM_BUILD_ROOT
rm -r $RPM_BUILD_DIR/%{inst}


%files

/share/apps/bin/dolfin-convert
/share/apps/bin/dolfin-order
/share/apps/bin/dolfin-plot
/share/apps/bin/dolfin-version
/share/apps/include/dolfin.h
/share/apps/include/dolfin/
/share/apps/lib/libdolfin.so
/share/apps/lib/libdolfin.so.1.0
/share/apps/lib/libdolfin.so.1.0.0
/share/apps/lib/pkgconfig/dolfin.pc
/share/apps/lib/python2.6/site-packages/dolfin_utils/
/share/apps/lib64/python2.6/site-packages/dolfin/
/share/apps/share/dolfin/

%doc /share/apps/share/man/man1/dolfin-convert.1.gz
%doc /share/apps/share/man/man1/dolfin-order.1.gz
%doc /share/apps/share/man/man1/dolfin-plot.1.gz
%doc /share/apps/share/man/man1/dolfin-version.1.gz

