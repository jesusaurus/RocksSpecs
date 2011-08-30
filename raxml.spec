%define name	raxml
%define dist	rocks
%define release	1
%define version git

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/share/apps
BuildRequires:	git
Summary:	RAxML standard & RAxML light

%description
RAxML for a Rocks Cluster.  Not intended for redistribution.


%prep
cd $RPM_BUILD_DIR
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
git clone git://github.com/stamatak/RAxML-Light-1.0.5.git
git clone git://github.com/stamatak/standard-RAxML.git


%build
cd $RPM_BUILD_DIR/%{name}-%{version}
cd RAxML-Light-1.0.5
make -f Makefile.SSE3.MPI

cd ../standard-RAxML
make -f Makefile.SSE3.HYBRID.gcc


%install
ls $RPM_BUILD_DIR

%clean
cd $RPM_BUILD_ROOT
rm -rf %{name}-%{version}


%files
