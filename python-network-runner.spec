# Created by pyp2rpm-3.2.2
%global pypi_name network-runner
%global ansible_role network-runner

Name:           python-%{pypi_name}
Version:        0.1.1
Release:        1%{?dist}
Summary:        Abstraction and Python API for Ansible Networking

License:        ASL 2.0
URL:            https://github.com/ansible-network/%{pypi_name}
Source0:        https://github.com/ansible-network/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: ansible >= 2.6
BuildRequires:  python3-devel
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(ansible-runner)

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

# Move ansible role to proper location
install -d -m 755 %{buildroot}%{_sysconfdir}/ansible/roles
mv etc/ansible/roles/%{ansible_role} %{buildroot}%{_sysconfdir}/ansible/roles

# %%check
# No tests yet exist upstream

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
* Wed Mar 20 2019 Dan Radez <dradez@redhat.com> - 0.1.1-1
- Initial package.