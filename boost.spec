%define name	boost
%define dist	rocks
%define release	2
%define version 1.48.0
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:	unknown
URL:		http://www.boost.org/
Source:		http://sourceforge.net/projects/boost/files/boost/1.48.0/boost_1_48_0.tar.gz
Source1:	boost-user-config.jam
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	python26-devel
Requires:	python26
Summary:	Boost %{version}

%description
Boost %{version} for a Rocks Cluster.  Not intedended for distribution.

%prep
%setup -n boost_1_48_0

%build
./bootstrap.sh --prefix=$RPM_BUILD_ROOT%{prefix}

%install
#You need to put info about python26 in $HOME/user-config.jam
if [ -e $HOME/user-config.jam ]
then
	mv $HOME/user-config.jam /tmp/user-config.jam
fi
cp $RPM_SOURCE_DIR/boost-user-config.jam $HOME/user-config.jam

./b2 --with-mpi --with-math --with-python --with-filesystem --with-system --with-thread --with-iostreams --with-program_options --debug-configuration python=2.6 install

%clean
#Clean up user-config.jam
if [ -e /tmp/user-config.jam ]
then
	mv /tmp/user-config.jam $HOME
else
	rm $HOME/user-config.jam
fi


%files
   /share/apps/include/boost
   /share/apps/lib/libboost_*
   /share/apps/lib/mpi.so

