%define name	atlas
%define dist	rocks
%define release	3
%define version 3.8.4
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
Source0:	%{name}%{version}.tar.bz2
Source1:	AMD.tar.gz
Source2:	UMFPACK.tar.gz
Source3:	UFconfig.tar.gz
Patch0:		UFconfig.patch
Requires:	lapack
BuildRequires:	lapack
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
Summary:	The ATLAS BLAS implementation.

%description
ATLAS BLAS implementation for a Rocks Cluster.  Not intended for distribution, tuned for rocks.research.pdx.edu.

%prep
cd $RPM_BUILD_DIR
rm -rf ATLAS
tar -jxvf $RPM_SOURCE_DIR/%{name}%{version}.tar.bz2
if [ $? -ne 0 ]; then
  exit $?
fi

%setup -n sparse -T -a 1 -c
%setup -n sparse -D -T -a 2
%setup -n sparse -D -T -a 3
%patch

cd $RPM_BUILD_DIR/ATLAS
mkdir ATLAS_LINUX


%build
cd $RPM_BUILD_DIR/ATLAS/ATLAS_LINUX
sed -i 's!\(DESTDIR\)=\([^ ]*\)!\1 \?= \2!' ../configure #we need a ?= instead of the =
../configure -Fa alg -fPIC -Si cputhrchk 0 -Ss flapack $RPM_BUILD_ROOT/%{prefix}/lib/liblapack.a --prefix=%{prefix}
sed -i '113 s/gcc/gcc -fPIC/' src/blas/gemv/Make.inc #inline patches, eww :(
make
cd lib
make shared; make ptshared

cd $RPM_BUILD_DIR/sparse/UMFPACK
make library


%install
cd $RPM_BUILD_DIR/ATLAS/ATLAS_LINUX
DESTDIR=$RPM_BUILD_ROOT/%{prefix} make install
cd ../../sparse/UMFPACK
DESTDIR=$RPM_BUILD_ROOT/%{prefix} make install
cd ../AMD
DESTDIR=$RPM_BUILD_ROOT/%{prefix} make install
cd $RPM_BUILD_DIR/lapack-3.2.2
cp lapack_LINUX.a $RPM_BUILD_ROOT/share/apps/lib/liblapack.a


%clean
cd $RPM_BUILD_DIR
rm -rf ATLAS
rm -rf sparse


%files
/share/apps/include/amd.h
/share/apps/include/atlas/
/share/apps/include/cblas.h
/share/apps/include/clapack.h
/share/apps/include/umfpack.h
/share/apps/include/umfpack_col_to_triplet.h
/share/apps/include/umfpack_defaults.h
/share/apps/include/umfpack_free_numeric.h
/share/apps/include/umfpack_free_symbolic.h
/share/apps/include/umfpack_get_determinant.h
/share/apps/include/umfpack_get_lunz.h
/share/apps/include/umfpack_get_numeric.h
/share/apps/include/umfpack_get_symbolic.h
/share/apps/include/umfpack_global.h
/share/apps/include/umfpack_load_numeric.h
/share/apps/include/umfpack_load_symbolic.h
/share/apps/include/umfpack_numeric.h
/share/apps/include/umfpack_qsymbolic.h
/share/apps/include/umfpack_report_control.h
/share/apps/include/umfpack_report_info.h
/share/apps/include/umfpack_report_matrix.h
/share/apps/include/umfpack_report_numeric.h
/share/apps/include/umfpack_report_perm.h
/share/apps/include/umfpack_report_status.h
/share/apps/include/umfpack_report_symbolic.h
/share/apps/include/umfpack_report_triplet.h
/share/apps/include/umfpack_report_vector.h
/share/apps/include/umfpack_save_numeric.h
/share/apps/include/umfpack_save_symbolic.h
/share/apps/include/umfpack_scale.h
/share/apps/include/umfpack_solve.h
/share/apps/include/umfpack_symbolic.h
/share/apps/include/umfpack_tictoc.h
/share/apps/include/umfpack_timer.h
/share/apps/include/umfpack_transpose.h
/share/apps/include/umfpack_triplet_to_col.h
/share/apps/include/umfpack_wsolve.h
/share/apps/lib/libamd.2.2.2.a
/share/apps/lib/libamd.a
/share/apps/lib/libatlas.a
/share/apps/lib/libcblas.a
/share/apps/lib/libf77blas.a
/share/apps/lib/liblapack.a
/share/apps/lib/libptcblas.a
/share/apps/lib/libptf77blas.a
/share/apps/lib/libumfpack.5.5.1.a
/share/apps/lib/libumfpack.a
/share/apps/lib/libblas.a
/share/apps/lib/libtmglib.a
