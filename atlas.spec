%define name	atlas
%define dist	rocks
%define release	4
%define version 3.8.4
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
Source0:	%{name}%{version}.tar.bz2
Source1:	http://www.cise.ufl.edu/research/sparse/amd/current/AMD.tar.gz
Source2:	http://www.cise.ufl.edu/research/sparse/umfpack/current/UMFPACK.tar.gz
Source3:	http://www.cise.ufl.edu/research/sparse/UFconfig/current/UFconfig.tar.gz
Source4:	http://www.netlib.org/lapack/lapack-3.2.2.tgz
Patch0:		UFconfig.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
Summary:	The ATLAS BLAS implementation.

%description
ATLAS BLAS implementation for a Rocks Cluster.  Not intended for distribution, tuned for rocks.research.pdx.edu.

%prep
#env; exit
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
%setup -T -b 4 -n lapack-3.2.2

cd $RPM_BUILD_DIR/ATLAS
mkdir ATLAS_LINUX


%build
cd $RPM_BUILD_DIR/lapack-3.2.2
cp INSTALL/make.inc.gfortran make.inc
sed -i '20 s/$/ -fPIC -m64/' make.inc
sed -i '22 s/$/ -fPIC -m64/' make.inc
#make
make blaslib lapacklib tmglib
mkdir -p $RPM_BUILD_ROOT/%{prefix}/lib/
cp blas_LINUX.a $RPM_BUILD_ROOT/%{prefix}/lib/libblas.a
cp lapack_LINUX.a $RPM_BUILD_ROOT/%{prefix}/lib/liblapack.a
cp tmglib_LINUX.a $RPM_BUILD_ROOT/%{prefix}/lib/libtmglib.a

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
DESTDIR=$RPM_BUILD_ROOT%{prefix} make install
cd ../../sparse/UMFPACK
DESTDIR=$RPM_BUILD_ROOT%{prefix} make install
cd ../AMD
DESTDIR=$RPM_BUILD_ROOT%{prefix} make install
cd ../UFconfig
cp UFconfig.h $RPM_BUILD_ROOT${prefix}
cd $RPM_BUILD_DIR/lapack-3.2.2
cp lapack_LINUX.a $RPM_BUILD_ROOT/share/apps/lib/liblapack.a


%clean
cd $RPM_BUILD_DIR
rm -rf ATLAS
rm -rf sparse


%files
/share/apps/include/amd.h
/share/apps/include/atlas/atlas_buildinfo.h
/share/apps/include/atlas/atlas_cNCmm.h
/share/apps/include/atlas/atlas_cacheedge.h
/share/apps/include/atlas/atlas_cmv.h
/share/apps/include/atlas/atlas_cmvN.h
/share/apps/include/atlas/atlas_cmvS.h
/share/apps/include/atlas/atlas_cmvT.h
/share/apps/include/atlas/atlas_cr1.h
/share/apps/include/atlas/atlas_csNKB.h
/share/apps/include/atlas/atlas_csysinfo.h
/share/apps/include/atlas/atlas_ctrsmXover.h
/share/apps/include/atlas/atlas_dNCmm.h
/share/apps/include/atlas/atlas_dmv.h
/share/apps/include/atlas/atlas_dmvN.h
/share/apps/include/atlas/atlas_dmvS.h
/share/apps/include/atlas/atlas_dmvT.h
/share/apps/include/atlas/atlas_dr1.h
/share/apps/include/atlas/atlas_dsysinfo.h
/share/apps/include/atlas/atlas_dtrsmXover.h
/share/apps/include/atlas/atlas_pthreads.h
/share/apps/include/atlas/atlas_sNCmm.h
/share/apps/include/atlas/atlas_smv.h
/share/apps/include/atlas/atlas_smvN.h
/share/apps/include/atlas/atlas_smvS.h
/share/apps/include/atlas/atlas_smvT.h
/share/apps/include/atlas/atlas_sr1.h
/share/apps/include/atlas/atlas_ssysinfo.h
/share/apps/include/atlas/atlas_strsmXover.h
/share/apps/include/atlas/atlas_trsmNB.h
/share/apps/include/atlas/atlas_type.h
/share/apps/include/atlas/atlas_zNCmm.h
/share/apps/include/atlas/atlas_zdNKB.h
/share/apps/include/atlas/atlas_zmv.h
/share/apps/include/atlas/atlas_zmvN.h
/share/apps/include/atlas/atlas_zmvS.h
/share/apps/include/atlas/atlas_zmvT.h
/share/apps/include/atlas/atlas_zr1.h
/share/apps/include/atlas/atlas_zsysinfo.h
/share/apps/include/atlas/atlas_ztrsmXover.h
/share/apps/include/atlas/cXover.h
/share/apps/include/atlas/cmm.h
/share/apps/include/atlas/dXover.h
/share/apps/include/atlas/dmm.h
/share/apps/include/atlas/sXover.h
/share/apps/include/atlas/smm.h
/share/apps/include/atlas/zXover.h
/share/apps/include/atlas/zmm.h
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
