# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
# Created by pyp2rpm-3.2.2
%global pypi_name network-runner
%global ansible_role network-runner

Name:           python-%{pypi_name}
Version:        0.1.7
Release:        3%{?dist}
Summary:        Abstraction and Python API for Ansible Networking

License:        ASL 2.0
URL:            https://github.com/ansible-network/%{pypi_name}
Source0:        https://github.com/ansible-network/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: ansible >= 2.6
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-ansible-runner
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-pytest

%description
Network Runner is a set of ansible roles and python library that
abstracts Ansible Networking operations. It interfaces
programatically through ansible-runner.

%package -n     python%{pyver}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}

Requires:       python%{pyver}-ansible-runner
# Python code cannot work without the ansible roles
Requires:  ansible-role-%{ansible_role} = %{version}-%{release}

%description -n python%{pyver}-%{pypi_name}
Network Runner is a set of ansible roles and python library that
abstracts Ansible Networking operations. It interfaces
programatically through ansible-runner.

%package -n ansible-role-%{ansible_role}
Summary:   Role for Python Network Runner Library

Requires: ansible >= 2.6
# No cross sub-package dependency.
# Can be installed and used without python package.

%description -n ansible-role-%{ansible_role}
Role for Python Network Runner Library

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{pyver_build}

%install
%{pyver_install}

%check
LANG=C.utf-8 %{pyver_bin} -m pytest --ignore=build

%files -n python%{pyver}-%{pypi_name}
%license LICENSE
%doc README.rst
%{pyver_sitelib}/network_runner
%{pyver_sitelib}/network_runner-%{version}-py?.?.egg-info

%files -n ansible-role-%{ansible_role}
%license LICENSE
%doc %{_sysconfdir}/ansible/roles/%{ansible_role}/README.md
%{_sysconfdir}/ansible/roles/%{ansible_role}/

%changelog
* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Dan Radez <dradez@redhat.com> - 0.1.7-1
- Updated to 0.1.7

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Dan Radez <dradez@redhat.com> - 0.1.6-1
- Updated to 0.1.6

* Tue Apr 02 2019 Dan Radez <dradez@redhat.com> - 0.1.5-1
- Updated to 0.1.5
- added %check

* Wed Mar 20 2019 Dan Radez <dradez@redhat.com> - 0.1.1-1
- Initial package.
