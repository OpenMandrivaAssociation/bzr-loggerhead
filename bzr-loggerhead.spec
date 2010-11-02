%define real_name	loggerhead

Name:           bzr-loggerhead
Version:        1.17
Release:        %mkrel 4
Summary:        A web view for Bazaar

Group:          Development/Other
License:        GPL
URL:            https://launchpad.net/loggerhead
Source0:        https://launchpad.net/%{name}/stable/%{version}/+download/%{real_name}-%{version}.tar.gz
Patch0:		bzr-compat.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

BuildArch:      noarch
BuildRequires:  python-devel 
BuildRequires:  bzr
BuildRequires:  python-pkg-resources
BuildRequires:	python-paste
Requires:       python >= 2.4
Requires:       bzr >= 1.17
Requires:	python-paste
Requires:	python-pygments
Requires:	python-simpletal
Provides:	loggerhead

%description
Loggerhead is a web viewer for projects in bazaar. 
It can be used to navigate a branch history, annotate files, view patches, 
perform searches, etc. It's originally based on bazaar-webserve, which is 
itself based on hgweb for Mercurial.

This package installs loggerhead as a plugin so that it can be run with:
bzr serve --http [--port=8080] [--directory=.].

%prep
%setup -q -n %{real_name}

%patch0 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=%{buildroot}/%_prefix

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%dir %py_puresitedir/bzrlib/plugins/loggerhead
%py_puresitedir/bzrlib/plugins/loggerhead/*
%dir %py_puresitedir/loggerhead
%py_puresitedir/loggerhead/*
%py_puresitedir/loggerhead-%{version}-*.egg-info
%{_bindir}/serve-branches
%{_bindir}/start-loggerhead
%{_bindir}/stop-loggerhead
%{_docdir}/loggerhead
%_mandir/man1/*
%doc README NEWS COPYING.txt

