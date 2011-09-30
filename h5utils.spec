%define name    h5utils
%define dist    rocks
%define release 1
%define version 1.12.1

Name:           %{name}
Version:        %{version}
Release:        %{dist}.%{release}
Group:          Rocks
License:       	GPL
URL:		http://ab-initio.mit.edu/wiki/index.php/H5utils
Source0:        h5utils-1.12.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:         /share/apps
Requires:       hdf5
BuildRequires:  hdf5-devel
Summary:        Tools for HDF5

%description
For a Rocks Cluster.  Not intended for redistribution.

%prep
%setup


%build
cd $RPM_BUILD_DIR/%{name}-%{version}
export F77=gfortran
export LDFLAGS="-L/share/apps/lib $LDFLAGS"
export CPPFLAGS="-I/share/apps/include $CPPFLAGS"
./configure --without-octave --prefix=/share/apps
make


%install
cd $RPM_BUILD_DIR/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT/
mkdir -p $RPM_BUILD_ROOT/
DESTDIR=$RPM_BUILD_ROOT make install


%clean
cd $RPM_BUILD_ROOT
rm -rf %{name}-%{version}


%files

/share/apps/bin/h5fromtxt
/share/apps/bin/h5topng
/share/apps/bin/h5totxt
/share/apps/bin/h5tovtk
/share/apps/share/h5utils/colormaps/autumn
/share/apps/share/h5utils/colormaps/bluered
/share/apps/share/h5utils/colormaps/bone
/share/apps/share/h5utils/colormaps/colorcube
/share/apps/share/h5utils/colormaps/cool
/share/apps/share/h5utils/colormaps/copper
/share/apps/share/h5utils/colormaps/dkbluered
/share/apps/share/h5utils/colormaps/flag
/share/apps/share/h5utils/colormaps/gray
/share/apps/share/h5utils/colormaps/green
/share/apps/share/h5utils/colormaps/hot
/share/apps/share/h5utils/colormaps/hsv
/share/apps/share/h5utils/colormaps/jet
/share/apps/share/h5utils/colormaps/lines
/share/apps/share/h5utils/colormaps/pink
/share/apps/share/h5utils/colormaps/prism
/share/apps/share/h5utils/colormaps/spring
/share/apps/share/h5utils/colormaps/summer
/share/apps/share/h5utils/colormaps/vga
/share/apps/share/h5utils/colormaps/winter
/share/apps/share/h5utils/colormaps/yarg
/share/apps/share/h5utils/colormaps/yellow
/share/apps/share/man/man1/h5fromtxt.1
/share/apps/share/man/man1/h5topng.1
/share/apps/share/man/man1/h5totxt.1
%doc /share/apps/share/man/man1/h5tovtk.1

