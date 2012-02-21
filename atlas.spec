%define name	atlas
%define dist	rocks
%define release	4
%define version 3.8.4
%define lversion 3.4.0
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
Source4:	lapack-%{lversion}.tgz
Patch0:		sparse.patch
Patch1:		lapack-%{lversion}.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
Summary:	The ATLAS BLAS/LAPACK implementation.

%description
ATLAS BLAS/LAPACK implementation for a Rocks Cluster.  Not intended for distribution, tuned for rocks.research.pdx.edu.

%prep
%setup -n ATLAS

%setup -n sparse -T -a 1 -c
%setup -n sparse -D -T -a 2
%setup -n sparse -D -T -a 3
%patch0

%setup -n lapack-%{lversion} -T -b 4
cd $RPM_BUILD_DIR/lapack-%{lversion}
cp INSTALL/make.inc.gfortran make.inc
%patch1

cd $RPM_BUILD_DIR/ATLAS
mkdir ATLAS_LINUX


%build
cd $RPM_BUILD_DIR/lapack-%{lversion}
make blaslib lapacklib tmglib
cp librefblas.so liblapack.so libtmglib.so $RPM_BUILD_ROOT/%{prefix}/lib/


cd $RPM_BUILD_DIR/ATLAS/ATLAS_LINUX
sed -i 's!\(DESTDIR\)=\([^ ]*\)!\1 \?= \2!' ../configure #we need a ?= instead of the =
../configure -Fa alg -fPIC -Si cputhrchk 0 --with-netlib-lapack=$RPM_BUILD_ROOT%{prefix}/lib/liblapack.so --prefix=$RPM_BUILD_ROOT%{prefix}
sed -i '113 s/gcc/gcc -fPIC/' src/blas/gemv/Make.inc #inline patches, eww :(
make
cd lib
make shared; make ptshared

cd $RPM_BUILD_DIR/sparse/UMFPACK
make library

cd $RPM_BUILD_DIR/sparse/AMD
make


%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}

cd $RPM_BUILD_DIR/ATLAS/ATLAS_LINUX
export DESTDIR=$RPM_BUILD_ROOT%{prefix}
make install
cp lib/*so $RPM_BUILD_ROOT%{prefix}/lib/

cd ../../sparse/UMFPACK
export DESTDIR=$RPM_BUILD_ROOT
make install

cd ../AMD
export DESTDIR=$RPM_BUILD_ROOT
make install

cd ../UFconfig
cp UFconfig.h $RPM_BUILD_ROOT%{prefix}/include


%clean
#cd $RPM_BUILD_DIR
#rm -rf ATLAS
#rm -rf sparse


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
/share/apps/include/UFconfig.h
/share/apps/lib/libamd.2.2.3.a
/share/apps/lib/libamd.a
/share/apps/lib/libatlas.a
/share/apps/lib/libcblas.a
/share/apps/lib/libf77blas.a
/share/apps/lib/liblapack.a
/share/apps/lib/libptcblas.a
/share/apps/lib/libptf77blas.a
/share/apps/lib/libumfpack.5.5.2.a
/share/apps/lib/libumfpack.a
/share/apps/lib/libatlas.so
/share/apps/lib/libcblas.so
/share/apps/lib/libf77blas.so
/share/apps/lib/liblapack.so
/share/apps/lib/librefblas.so
/share/apps/lib/libtmglib.so
/share/apps/lib/libptcblas.so
/share/apps/lib/libptf77blas.so

