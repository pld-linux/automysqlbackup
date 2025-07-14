%define		subver	rc6
%define		rel		1
Summary:	Automatic MySQL Backup
Name:		automysqlbackup
Version:	3.0
Release:	0.%{subver}.%{rel}
License:	GPL v2+
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/automysqlbackup/%{name}-v%{version}_%{subver}.tar.gz
# Source0-md5:	33db887176f8480a9a9c324f5b718b88
Patch2:		%{name}-du.patch
Patch3:		%{name}-silent.patch
URL:		http://sourceforge.net/projects/automysqlbackup/
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoMySQLBackup with a basic configuration will create Daily, Weekly
and Monthly backups of one or more of your MySQL databases from one or
more of your MySQL servers.

Other Features include:
- Email notification of backups
- Backup Compression and Encryption
- Configurable backup rotation
- Incremental database backups

%prep
%setup -q -n %{name}-v%{version}_%{subver}
%patch -P2 -p1
%patch -P3 -p1

%{__sed} -i -e '1s,#!/usr/bin/env bash,#!/bin/bash,' %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{_bindir}}
cp -p %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}
