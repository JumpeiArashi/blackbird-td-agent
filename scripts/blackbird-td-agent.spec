%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define name blackbird-td-agent
%define version 0.2.1
%define unmangled_version %{version}
%define release 1%{dist}
%define include_dir /etc/blackbird/conf.d
%define plugins_dir /opt/blackbird/plugins

Summary: Get td-agent monitor_plugin result.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: WTFPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: ARASHI, Jumpei <jumpei.arashi@arashike.com>
Packager: ARASHI, Jumpei <jumpei.arashi@arashike.com>
Requires: blackbird
Url: https://github.com/Vagrants/blackbird-td-agent
BuildRequires:  python-setuptools

%description
UNKNOWN

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

install -dm 0755 $RPM_BUILD_ROOT%{include_dir}
install -dm 0755 $RPM_BUILD_ROOT%{plugins_dir}
install -p -m 0644 scripts/td-agent.cfg $RPM_BUILD_ROOT%{include_dir}/td-agent.cfg
install -p -m 0644 td_agent.py $RPM_BUILD_ROOT%{plugins_dir}/td_agent.py

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%config(noreplace) %{include_dir}/td-agent.cfg
%{plugins_dir}/td_agent.*

%changelog
* Wed Feb 4 2015 ARASHI, Jumpei <jumpei.arashi@arashike.com> - 0.2.1-1
- Remove deprecated validation `ipaddress`

* Wed Dec 24 2014 ARASHI, Jumpei <jumpei.arashi@arashike.com> - 0.2.0-1
- Handle no "buffer_queue_length" key error
- Effiency to sending LLD items

* Fri Jul 4 2014 ARASHI, Jumpei <jumpei.arashi@arashike.com> - 0.1.0-2
- Remove include_dir and plugins_dir from %dir

* Fri Jul 4 2014 ARASHI, Jumpei <jumpei.arashi@arashike.com> - 0.1.0-1
- Initial package
