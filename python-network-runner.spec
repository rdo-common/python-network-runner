# Created by pyp2rpm-3.2.2
%global pypi_name network-runner
%global ansible_role network-runner

Name:           python-%{pypi_name}
Version:        0.1.7
Release:        1%{?dist}
Summary:        Abstraction and Python API for Ansible Networking

License:        ASL 2.0
URL:            https://github.com/ansible-network/%{pypi_name}
Source0:        https://github.com/ansible-network/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: ansible >= 2.6
BuildRequires:  python3-devel
BuildRequires:  python3dist(ansible-runner)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)

%description
Network Runner is a set of ansible roles and python library that
abstracts Ansible Networking operations. It interfaces
programatically through ansible-runner.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(ansible-runner)
# Python code cannot work without the ansible roles
Requires:  ansible-role-%{ansible_role} = %{version}-%{release}

%description -n python3-%{pypi_name}
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
%py3_build

%install
%py3_install

%check
LANG=C.utf-8 %{__python3} -m pytest --ignore=build

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/network_runner
%{python3_sitelib}/network_runner-%{version}-py?.?.egg-info

%files -n ansible-role-%{ansible_role}
%license LICENSE
%doc %{_sysconfdir}/ansible/roles/%{ansible_role}/README.md
%{_sysconfdir}/ansible/roles/%{ansible_role}/

%changelog
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
