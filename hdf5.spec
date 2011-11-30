%define name    hdf5
%define dist    rocks
%define release 1
%define version 1.8.8

Name:           %{name}
Version:        %{version}
Release:        %{dist}.%{release}
Group:          Rocks
License:       	Other
URL:		http://hdfgroup.org/
Source0:        hdf5-1.8.8.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:         /share/apps
Summary:        Parallel HDF5

%description
Parallel HDF5 with Fortran support for a Rocks Cluster.  Not intended for redistribution.

%prep
%setup


%build
cd $RPM_BUILD_DIR/%{name}-%{version}
CC=mpicc LDFLAGS="-L/share/apps/lib $LDFLAGS" CPPFLAGS="-I/share/apps/include $CPPFLAGS" ./configure --prefix=/share/apps --enable-parallel --enable-fortran
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

   /share/apps/bin/gif2h5
   /share/apps/bin/h52gif
   /share/apps/bin/h5copy
   /share/apps/bin/h5debug
   /share/apps/bin/h5diff
   /share/apps/bin/h5dump
   /share/apps/bin/h5import
   /share/apps/bin/h5jam
   /share/apps/bin/h5ls
   /share/apps/bin/h5mkgrp
   /share/apps/bin/h5pcc
   /share/apps/bin/h5perf
   /share/apps/bin/h5perf_serial
   /share/apps/bin/h5pfc
   /share/apps/bin/h5redeploy
   /share/apps/bin/h5repack
   /share/apps/bin/h5repart
   /share/apps/bin/h5stat
   /share/apps/bin/h5unjam
   /share/apps/bin/ph5diff

   /share/apps/include/H5ACpublic.h
   /share/apps/include/H5Apublic.h
   /share/apps/include/H5Cpublic.h
   /share/apps/include/H5DSpublic.h
   /share/apps/include/H5Dpublic.h
   /share/apps/include/H5Epubgen.h
   /share/apps/include/H5Epublic.h
   /share/apps/include/H5FDcore.h
   /share/apps/include/H5FDdirect.h
   /share/apps/include/H5FDfamily.h
   /share/apps/include/H5FDlog.h
   /share/apps/include/H5FDmpi.h
   /share/apps/include/H5FDmpio.h
   /share/apps/include/H5FDmpiposix.h
   /share/apps/include/H5FDmulti.h
   /share/apps/include/H5FDpublic.h
   /share/apps/include/H5FDsec2.h
   /share/apps/include/H5FDstdio.h
   /share/apps/include/H5Fpublic.h
   /share/apps/include/H5Gpublic.h
   /share/apps/include/H5IMpublic.h
   /share/apps/include/H5Ipublic.h
   /share/apps/include/H5LTpublic.h
   /share/apps/include/H5Lpublic.h
   /share/apps/include/H5MMpublic.h
   /share/apps/include/H5Opublic.h
   /share/apps/include/H5PTpublic.h
   /share/apps/include/H5Ppublic.h
   /share/apps/include/H5Rpublic.h
   /share/apps/include/H5Spublic.h
   /share/apps/include/H5TBpublic.h
   /share/apps/include/H5Tpublic.h
   /share/apps/include/H5Zpublic.h
   /share/apps/include/H5api_adpt.h
   /share/apps/include/H5f90i.h
   /share/apps/include/H5f90i_gen.h
   /share/apps/include/H5overflow.h
   /share/apps/include/H5pubconf.h
   /share/apps/include/H5public.h
   /share/apps/include/H5version.h
   /share/apps/include/h5_dble_interface.mod
   /share/apps/include/h5a.mod
   /share/apps/include/h5a_provisional.mod
   /share/apps/include/h5d.mod
   /share/apps/include/h5d_provisional.mod
   /share/apps/include/h5ds.mod
   /share/apps/include/h5e.mod
   /share/apps/include/h5e_provisional.mod
   /share/apps/include/h5f.mod
   /share/apps/include/h5fdmpio.mod
   /share/apps/include/h5fortran_types.mod
   /share/apps/include/h5g.mod
   /share/apps/include/h5global.mod
   /share/apps/include/h5i.mod
   /share/apps/include/h5im.mod
   /share/apps/include/h5l.mod
   /share/apps/include/h5l_provisional.mod
   /share/apps/include/h5lib.mod
   /share/apps/include/h5lib_provisional.mod
   /share/apps/include/h5lt.mod
   /share/apps/include/h5o.mod
   /share/apps/include/h5o_provisional.mod
   /share/apps/include/h5p.mod
   /share/apps/include/h5p_provisional.mod
   /share/apps/include/h5r.mod
   /share/apps/include/h5r_provisional.mod
   /share/apps/include/h5s.mod
   /share/apps/include/h5t.mod
   /share/apps/include/h5t_provisional.mod
   /share/apps/include/h5tb.mod
   /share/apps/include/h5z.mod
   /share/apps/include/hdf5.h
   /share/apps/include/hdf5.mod
   /share/apps/include/hdf5_hl.h
   /share/apps/lib/libhdf5.a
   /share/apps/lib/libhdf5.la
   /share/apps/lib/libhdf5.settings
   /share/apps/lib/libhdf5_fortran.a
   /share/apps/lib/libhdf5_fortran.la
   /share/apps/lib/libhdf5_hl.a
   /share/apps/lib/libhdf5_hl.la
   /share/apps/lib/libhdf5hl_fortran.a
   /share/apps/lib/libhdf5hl_fortran.la

%doc /share/apps/share/hdf5_examples/
