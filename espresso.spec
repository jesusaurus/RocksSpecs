%define name		quantum-espresso
%define dist		rocks
%define release		1
%define version		4.3
%define wversion	2.1.1
%define prefix		/share/apps
%define inst		espresso-%{version}

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
Source0:	espresso-%{version}.tar.gz
Source1:	want-%{wversion}.tar.gz
Summary:	Quantum Espresso with WanT

%description
Quantum Espresso with WanT plugin for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n %{inst} -q
%setup -T -D -a 1 -n %{inst}


%build
cd $RPM_BUILD_DIR/%{inst}
mkdir -p $RPM_BUILD_ROOT%{prefix}
./configure --enable-parallel CC=mpicc LIBDIRS="/share/apps/lib /opt/openmpi/lib" FFLAGS="-I/opt/openmpi/include" CFLAGS="-I/opt/openmpi/include"
make pwall want


%install
mkdir -p $RPM_BUILD_ROOT/%{prefix}/bin
cd $RPM_BUILD_DIR/%{inst}
cp bin/* $RPM_BUILD_ROOT/%{prefix}/bin/
rm -rf WANT/bin/CVS
cp WANT/bin/* $RPM_BUILD_ROOT/%{prefix}/bin/

%clean


%files
   /share/apps/bin/average.x
   /share/apps/bin/band_plot.x
   /share/apps/bin/bands.x
   /share/apps/bin/bands_FS.x
   /share/apps/bin/blc2wan.x
   /share/apps/bin/conductor.x
   /share/apps/bin/current.x
   /share/apps/bin/d3.x
   /share/apps/bin/disentangle.x
   /share/apps/bin/dist.x
   /share/apps/bin/dos.x
   /share/apps/bin/dynmat.x
   /share/apps/bin/epsilon.x
   /share/apps/bin/ev.x
   /share/apps/bin/fqha.x
   /share/apps/bin/gcube2plt.x
   /share/apps/bin/generate_vdW_kernel_table.x
   /share/apps/bin/initial_state.x
   /share/apps/bin/iotk
   /share/apps/bin/iotk.x
   /share/apps/bin/iotk_print_kinds.x
   /share/apps/bin/kgrid.x
   /share/apps/bin/kpoints.x
   /share/apps/bin/kvecs_FS.x
   /share/apps/bin/lambda.x
   /share/apps/bin/matdyn.x
   /share/apps/bin/midpoint.x
   /share/apps/bin/neb.x
   /share/apps/bin/path_interpolation.x
   /share/apps/bin/ph.x
   /share/apps/bin/phcg.x
   /share/apps/bin/plan_avg.x
   /share/apps/bin/plot.x
   /share/apps/bin/plotband.x
   /share/apps/bin/plotproj.x
   /share/apps/bin/plotrho.x
   /share/apps/bin/pmw.x
   /share/apps/bin/pp.x
   /share/apps/bin/projwfc.x
   /share/apps/bin/pw.x
   /share/apps/bin/pw2gw.x
   /share/apps/bin/pw2wannier90.x
   /share/apps/bin/pw_export.x
   /share/apps/bin/pwcond.x
   /share/apps/bin/pwi2xsf.x
   /share/apps/bin/q2r.x
   /share/apps/bin/sumpdos
   /share/apps/bin/sumpdos.x
   /share/apps/bin/vdw.x
   /share/apps/bin/wannier.x
   /share/apps/bin/wannier_ham.x
   /share/apps/bin/wannier_plot.x
   /share/apps/bin/wfdd.x

