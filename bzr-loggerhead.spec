%define real_name	loggerhead
%define bzr_revno	366

Name:           bzr-loggerhead
Version:        1.11
Release:        %mkrel 0.3
Summary:        A web view for Bazaar

Group:          Development/Other
License:        GPL
URL:            https://launchpad.net/loggerhead
Source0:        https://launchpad.net/%{name}/stable/%{version}/+download/%{real_name}-%{version}-r%{bzr_revno}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

BuildArch:      noarch
BuildRequires:  python-devel 
BuildRequires:  bzr
BuildRequires:  python-pkg-resources
BuildRequires:	python-paste
Requires:       python >= 2.4
Requires:       bzr >= 1.13
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
%setup -q -n %{real_name}-%{version}-r%{bzr_revno}


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
%py_puresitedir/loggerhead-1.10-py2.6.egg-info
%{_bindir}/serve-branches
%{_bindir}/start-loggerhead
%{_bindir}/stop-loggerhead
%{_docdir}/loggerhead
%_mandir/man1/serve-branches.1.lzma
%_mandir/man1/start-loggerhead.1.lzma
%_mandir/man1/stop-loggerhead.1.lzma
%doc README NEWS COPYING.txt

