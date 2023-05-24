# https://fedoraproject.org/wiki/PackagingDrafts/SELinux_Independent_Policy
%global selinuxtype targeted
%global moduletype contrib
%global modulename %{name}

Summary:        SELinux lost label reproducer
Name:           lostlabel
Version:        0.1
Release:        1
License:        libselinux-1.0
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
%{?selinux_requires}


%description
%{summary}.


%prep
%autosetup


%build
make -f /usr/share/selinux/devel/Makefile %{name}.pp


%install
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
mkdir -p %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -pm 644 %{name}.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}


%files
%{_sharedstatedir}/%{name}
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp
%ghost %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}


%pre
%selinux_relabel_pre -s %{selinuxtype}


%post
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp


%postun
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi


%posttrans
%selinux_relabel_post -s %{selinuxtype}


%changelog
* Wed May 24 2023 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 0.1-1
- Initial packaging from Fedora guidelines
