%define name	suitesparse
%define dist	rocks
%define release	1
%define version 4.0.2
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	BSD
Source0:        http://www.cise.ufl.edu/research/sparse/SuiteSparse/SuiteSparse-%{version}.tar.gz
Patch0:		suitesparse.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
Requires:       atlas
BuildRequires:  atlas
Summary:	SuiteSparse

%description
Full SuiteSparse implementation for a Rocks Cluster.  Not intended for distribution, tuned for rocks.research.pdx.edu.


%prep
%setup -n SuiteSparse
%patch0


%build
export CFLAGS='-fPIC'
export CXXFLAGS='-fPIC'
cd $RPM_BUILD_DIR/SuiteSparse
make library

#Make shared libraries
#Thank you, http://repository.slacky.eu/slackware-12.1/development/suitesparse/3.1.0/src/suitesparse.SlackBuild

cd AMD
AMDM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
AMDV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libamd.so.${AMDM} -o libamd.so.${AMDV} `ls *.o`
ln -sf libamd.so.${AMDV} libamd.so.${AMDM}
ln -sf libamd.so.${AMDV} libamd.so
cd ../../

cd BTF
BTFM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
BTFV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libbtf.so.${BTFM} -o libbtf.so.${BTFV} `ls *.o`
ln -sf libbtf.so.${BTFV} libbtf.so.${BTFM}
ln -sf libbtf.so.${BTFV} libbtf.so
cd ../../

cd CAMD
CAMDM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
CAMDV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libcamd.so.${CAMDM} -o libcamd.so.${CAMDV} `ls *.o`
ln -sf libcamd.so.${CAMDV} libcamd.so.${CAMDM}
ln -sf libcamd.so.${CAMDV} libcamd.so
cd ../../

cd CCOLAMD
CCOLAMDM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
CCOLAMDV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libccolamd.so.${CCOLAMDM} -o libccolamd.so.${CCOLAMDV} `ls *.o`
ln -sf libccolamd.so.${CCOLAMDV} libccolamd.so.${CCOLAMDM}
ln -sf libccolamd.so.${CCOLAMDM} libccolamd.so
cd ../../

cd CHOLMOD
CHOLMODM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
CHOLMODV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libcholmod.so.${CHOLMODM} -o libcholmod.so.${CHOLMODV} `ls *.o`
ln -sf libcholmod.so.${CHOLMODV} libcholmod.so.${CHOLMODM}
ln -sf libcholmod.so.${CHOLMODV} libcholmod.so
cd ../../

cd COLAMD
COLAMDM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
COLAMDV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libcolamd.so.${COLAMDM} -o libcolamd.so.${COLAMDV} `ls *.o`
ln -sf libcolamd.so.${COLAMDV} libcolamd.so.${COLAMDM}
ln -sf libcolamd.so.${COLAMDV} libcolamd.so
cd ../../

cd CSparse
CSparseM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
CSparseV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libcsparse.so.${CSparseM} -o libcsparse.so.${CSparseV} `ls *.o`
ln -sf libcsparse.so.${CSparseV} libcsparse.so.${CSparseM}
ln -sf libcsparse.so.${CSparseV} libcsparse.so
cd ../../

cd CXSparse
CXSparseM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
CXSparseV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libcxsparse.so.${CXSparseM} -o libcxsparse.so.${CXSparseV} `ls *.o`
ln -sf libcxsparse.so.${CXSparseV} libcxsparse.so.${CXSparseM}
ln -sf libcxsparse.so.${CXSparseV} libcxsparse.so
cd ../../

cd KLU
KLUM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
KLUV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libklu.so.${KLUM} -o libklu.so.${KLUV} `ls *.o`
ln -sf libklu.so.${KLUV} libklu.so.${KLUM}
ln -sf libklu.so.${KLUV} libklu.so
cd ../../

cd LDL
LDLM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
LDLV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libldl.so.${LDLM} -o libldl.so.${LDLV} `ls *.o`
ln -sf libldl.so.${LDLV} libldl.so.${LDLM}
ln -sf libldl.so.${LDLV} libldl.so
cd ../../

cd RBio
RBioM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
RBioV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,librbio.so.${RBioM} -o librbio.so.${RBioV} `ls *.o`
ln -sf librbio.so.${RBioV} librbio.so.${RBioM}
ln -sf librbio.so.${RBioV} librbio.so
cd ../../

cd SPQR
SPQRM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
SPQRV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libspqr.so.${SPQRM} -o libspqr.so.${SPQRV} `ls *.o`
ln -sf libspqr.so.${SPQRV} libspqr.so.${SPQRM}
ln -sf libspqr.so.${SPQRV} libspqr.so
cd ../../

cd SuiteSparse_config
SuiteSparse_configM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
SuiteSparse_configV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
#cd Lib
gcc -shared -Wl,-soname,libsuitesparseconfig.so.${SuiteSparse_configM} -o libsuitesparseconfig.so.${SuiteSparse_configV} `ls *.o`
ln -sf libsuitesparseconfig.so.${SuiteSparse_configV} libsuitesparseconfig.so.${SuiteSparse_configM}
ln -sf libsuitesparseconfig.so.${SuiteSparse_configV} libsuitesparseconfig.so
#cd ../../
cd ../

cd UMFPACK
UMFPACKM=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2| cut -d. -f1)
UMFPACKV=$(grep VERSION Makefile| cut -d= -f2 -s| cut -d\  -f2)
cd Lib
gcc -shared -Wl,-soname,libumfpack.so.${UMFPACKM} -o libumfpack.so.${UMFPACKV} `ls *.o`
ln -sf libumfpack.so.${UMFPACKV} libumfpack.so.${UMFPACKM}
ln -sf libumfpack.so.${UMFPACKV} libumfpack.so
cd ../../

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/{lib,include}

cd $RPM_BUILD_DIR/SuiteSparse
export DESTDIR=$RPM_BUILD_ROOT
make install

#Manual install of shared libs
for i in AMD/ CAMD/ CHOLMOD/ LDL/ BTF/ CCOLAMD/ COLAMD/ CSparse/ CXSparse/ KLU/ UMFPACK/ RBio/ SPQR/; do
    cp -a $i/Lib/{*.a,*.so*} $RPM_BUILD_ROOT%{prefix}/lib/;
done
cp -a SuiteSparse_config/{*.a,*.so*} $RPM_BUILD_ROOT%{prefix}/lib/;


%clean
cd $RPM_BUILD_DIR
rm -rf SuiteSpares


%files
%defattr(-,root,root,-)
/share/apps/include
/share/apps/lib
