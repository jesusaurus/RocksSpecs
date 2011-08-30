
%define name	cmake
%define dist	rocks
%define release	2
%define version 2.8.5

Name:           %{name}
Version:        %{version}
Release:        %{dist}.%{release}
Summary:        CMake 2.8.5

Group:          Rocks
License:        BSD
URL:            http://www.cmake.org/
Source0:        %{name}-%{version}-Linux-i386.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/share/apps

%description
CMake http://www.cmake.org

%prep
%setup -q -n %{name}-%{version}-Linux-i386

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/share/apps/
mv $RPM_BUILD_DIR/%{name}-%{version}-Linux-i386/* $RPM_BUILD_ROOT/share/apps/

%clean
rm -rf $RPM_BUILD_ROOT/

%changelog

%files
%defattr(-,root,root,-)
/share/apps/bin/ccmake
/share/apps/bin/cmake
/share/apps/bin/cmake-gui
/share/apps/bin/cpack
/share/apps/bin/ctest
/share/apps/share/
%doc /share/apps/doc/
%doc /share/apps/man/man1/
