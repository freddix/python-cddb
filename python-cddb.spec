Summary:	Module for accessing CDDB and FreeDB
Name:		python-cddb
Version:	1.4
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://cddb-py.sourceforge.net/CDDB-%{version}.tar.gz
# Source0-md5:	254698082bafe3030d07d88fb7e13fe2
URL:		http://cddb-py.sourceforge.net/
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of three modules to access the CDDB and FreeDB online
databases of audio CD track titles and information. It includes a C
extension module to fetch track lengths under Linux, FreeBSD, OpenBSD,
Mac OS X, Solaris, and Win32, which is easily ported to other
operating systems.

%prep
%setup -qn CDDB-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/cdrom.so

