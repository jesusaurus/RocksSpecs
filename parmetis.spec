%define name    parmetis                                                                                                
%define dist    rocks                                                                                                    
%define release 2.%{dist}
%define version 4.0.2
%define prefix  /share/apps 

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	ParMETIS

Group:		Rocks
License:	MIT
URL:		http://glaros.dtc.umn.edu/gkhome/metis/parmetis
Source0:	http://glaros.dtc.umn.edu/gkhome/fetch/sw/parmetis/parmetis-4.0.2.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Prefix:         /share/apps
BuildRequires:	cmake

%description
ParMETIS for a Rocks cluster.

%prep
%setup -q


%build
make config shared=1 prefix=%{prefix}
cd metis
make config shared=1 prefix=%{prefix}
make %{?_smp_mflags}
cd ..
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
cd metis
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/share/apps/bin/mtest
/share/apps/bin/parmetis
/share/apps/bin/pometis
/share/apps/bin/ptest
/share/apps/include/parmetis.h
/share/apps/lib/libparmetis.so
/share/apps/bin/cmpfillin
/share/apps/bin/gpmetis
/share/apps/bin/graphchk
/share/apps/bin/m2gmetis
/share/apps/bin/mpmetis
/share/apps/bin/ndmetis
/share/apps/include/metis.h
/share/apps/lib/libmetis.so


%changelog

