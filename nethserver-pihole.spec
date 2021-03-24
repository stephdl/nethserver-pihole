Summary: nethserver-pihole  is A module to install pihole as docker
%define name nethserver-pihole
Name: %{name}
%define version 1.0.1
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: nethserver-docker >= 1.0.6
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
A module to install pihole as docker

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{__mkdir_p} -p $RPM_BUILD_ROOT/var/lib/pihole/php-conf.d/

rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%changelog
* Wed Mar 24 2021 stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.1
- Pihole can run on aqua

* Tue Dec 29 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.0
- Pihole restart is a valid action
- CGI php memory limit is customisable

* Thu Aug 6 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.6
- Upgrade the docker image
* Sat Jun 27 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.5
- Add #53 to dns IP
* Tue Jun 23 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.4
- require docker >= 1.0.6
* Thu Jun 22 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.3
- First release
