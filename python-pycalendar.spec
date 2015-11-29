%define 	module	pycalendar
Summary:	iCalendar/vCard Library
Summary(pl.UTF-8):	Biblioteka iCalendar/vCard
Name:		python-%{module}
Version:	2.0
Release:	0.1
License:	Apache v2.0
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/pycalendar/%{module}-%{version}.tar.gz
# Source0-md5:	2ada6ce8314715a264b45f4e158909ae
URL:		http://pypi.python.org/pypi/pycalendar/2.0
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
#Requires:		python-libs
Requires:		python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iCalendar/vCard Library.

%description -l pl.UTF-8
Biblioteka iCalendar/vCard.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/pycalendar
%{py_sitescriptdir}/pycalendar/*.py[co]
%dir %{py_sitescriptdir}/pycalendar/icalendar
%{py_sitescriptdir}/pycalendar/icalendar/*.py[co]
%dir %{py_sitescriptdir}/pycalendar/vcard
%{py_sitescriptdir}/pycalendar/vcard/*.py[co]

%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pycalendar-*.egg-info
%endif
