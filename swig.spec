%define name	swig
%define dist	rocks
%define release	2
%define version 2.0.4
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
URL:		http://www.swig.org/
Source:		http://prdownloads.sourceforge.net/swig/swig-2.0.4.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
Summary:	SWIG

%description
SWIG for a Rocks Cluster.  Not intedended for distribution.


%prep
%setup -n swig-%{version}


%build
./configure --prefix=%{prefix}
make


%install
DESTDIR=$RPM_BUILD_ROOT make install


%clean
rm -r $RPM_BUILD_ROOT
rm -r $RPM_BUILD_DIR


%files
   /share/apps/bin/ccache-swig
   /share/apps/bin/swig
   /share/apps/share/swig/2.0.4/
%doc /share/apps/share/man/man1/ccache-swig.1
