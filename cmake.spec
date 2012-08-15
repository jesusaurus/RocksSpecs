
%define name	cmake
%define dist	rocks
%define release	1
%define version 2.8.9

Name:           %{name}
Version:        %{version}
Release:        %{dist}.%{release}
Summary:        CMake %{version}
Group:          Rocks
License:        BSD
URL:            http://www.cmake.org/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/share/apps

%description
CMake http://www.cmake.org

%prep
%setup 

%build
./bootstrap --prefix=$RPM_BUILD_ROOT%{prefix}
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT/

%changelog

%files
%defattr(-,root,root,-)
/share/apps/bin/ccmake
/share/apps/bin/cmake
/share/apps/bin/cpack
/share/apps/bin/ctest
/share/apps/share/aclocal/cmake.m4
/share/apps/share/cmake-2.8/
%doc /share/apps/doc/cmake-2.8/
%doc   /share/apps/man/man1/ccmake.1
%doc   /share/apps/man/man1/cmake.1
%doc   /share/apps/man/man1/cmakecommands.1
%doc   /share/apps/man/man1/cmakecompat.1
%doc   /share/apps/man/man1/cmakemodules.1
%doc   /share/apps/man/man1/cmakepolicies.1
%doc   /share/apps/man/man1/cmakeprops.1
%doc   /share/apps/man/man1/cmakevars.1
%doc   /share/apps/man/man1/cpack.1
%doc   /share/apps/man/man1/ctest.1
