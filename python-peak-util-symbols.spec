%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define packagename SymbolType

Name:           python-peak-util-symbols
Version:        1.0
Release:        4.1%{?dist}
Summary:        Simple "symbol" type, useful for enumerations or sentinels

Group:          Development/Languages
License:        Python or ZPLv2.1
URL:            http://peak.telecommunity.com/DevCenter/%{packagename}
Source0:        http://pypi.python.org/packages/source/S/%{packagename}/%{packagename}-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel
BuildRequires:  python-nose

%description
SymbolType gives you access to the peak.util.symbols module, previously
available only by installing the full PEAK toolkit. peak.util.symbols provides
a Symbol type and two built-in symbols that are used by PEAK: NOT_FOUND and
NOT_GIVEN.

%prep
%setup -q -n %{packagename}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%check
nosetests

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0-2
- Rebuild for Python 2.6

* Sun Aug  3 2008 Luke Macken <lmacken@redhat.com> - 1.0-1
- Initial package for Fedora
