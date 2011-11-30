%define name	libctl
%define dist	rocks
%define release	1
%define version 3.1

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/share/apps
Requires:	atlas
Requires:	guile
Requires:	hdf5 
Requires:	harminv
BuildRequires:	atlas
BuildRequires:	guile-devel
BuildRequires:	hdf5
BuildRequires:	harminv
Summary:	libCtl 3.1

%description
libCtl for a Rocks Cluster.  Not intended for redistribution.

%prep
%setup


%build
cd ../%{name}-%{version}
F77=mpif77 LDFLAGS="-L/share/apps/lib" CPPFLAGS="-I/share/apps/include" ./configure --prefix=/share/apps 
make


%install
cd $RPM_BUILD_DIR/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT/
mkdir -p $RPM_BUILD_ROOT/
DESTDIR=$RPM_BUILD_ROOT make install


%clean
cd $RPM_BUILD_DIR
rm -rf %{name}-%version}


%files
/share/apps/bin/gen-ctl-io
/share/apps/include/ctl.h
/share/apps/include/ctlgeom-types.h
/share/apps/include/ctlgeom.h
/share/apps/lib/libctl.a
/share/apps/lib/libctl.la
/share/apps/lib/libctlgeom.a
/share/apps/lib/libctlgeom.la
/share/apps/share/libctl/base/class.scm
/share/apps/share/libctl/base/ctl.scm
/share/apps/share/libctl/base/extern-funcs.scm
/share/apps/share/libctl/base/help.scm
/share/apps/share/libctl/base/include.scm
/share/apps/share/libctl/base/interaction.scm
/share/apps/share/libctl/base/io-vars.scm
/share/apps/share/libctl/base/main.c
/share/apps/share/libctl/base/math-utils.scm
/share/apps/share/libctl/base/matrix3x3.scm
/share/apps/share/libctl/base/simplex.scm
/share/apps/share/libctl/base/utils.scm
/share/apps/share/libctl/base/vector3.scm
/share/apps/share/libctl/utils/ctl-io.scm
/share/apps/share/libctl/utils/geom.c
/share/apps/share/libctl/utils/geom.scm
/share/apps/share/libctl/utils/nlopt-constants.scm
/share/apps/share/libctl/utils/nlopt.c
%doc /share/apps/share/man/man1/gen-ctl-io.1

