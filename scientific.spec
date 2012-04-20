%define name	python-scientific
%define dist	rocks
%define release	1
%define version 2.8
%define prefix	/share/apps

Name:		%{name}
Version:	%{version}
Release:	%{dist}.%{release}
Group:		Rocks
License:        Other
URL:		http://dirac.cnrs-orleans.fr/plone/software/scientificpython/
Source:		https://sourcesup.renater.fr/frs/download.php/2309/ScientificPython-2.8.tar.gz
Patch:          scientific.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		%{prefix}
BuildRequires:	python26
BuildRequires:	python26-numpy
Requires:	python26
Requires:	python26-numpy
Summary:	Python Scientific

%description
Python Scientific for a Rocks Cluster.  Not intended for redistribution.


%prep
%setup -n ScientificPython-%{version}

# setup.py can't handle numpy in a non-standard location
#vim setup.py
%patch

%build
export PYTHONPATH=/share/apps/lib/python2.6/site-packages/:share/apps/lib64/python2.6/site-packages/:$PYTHONPATH
python26 setup.py build

%install
python26 setup.py install --prefix=$RPM_BUILD_ROOT/%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files

