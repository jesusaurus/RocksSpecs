
%define name	cmake
%define dist	rocks
%define release	1
%define version 2.8.5

Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        CMake 2.8.5

Group:          Rocks
License:        BSD
URL:            http://www.cmake.org/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
CMake http://www.cmake.org

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog
