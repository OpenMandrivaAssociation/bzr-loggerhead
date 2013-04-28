%define real_name	loggerhead

Name:           bzr-loggerhead
Version:        1.18.2
Release:        1
Summary:        A web view for Bazaar

Group:          Development/Other
License:        GPL
URL:            https://launchpad.net/loggerhead
Source0:        https://launchpad.net/%{name}/stable/%{version}/+download/%{real_name}-%{version}.tar.gz
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
%setup -q -n %{real_name}-%{version}

%build

%install
python setup.py install --prefix=%{buildroot}/%_prefix

%files 
%defattr(-,root,root,-)
%dir %py_puresitedir/bzrlib/plugins/loggerhead
%py_puresitedir/bzrlib/plugins/loggerhead/*
%dir %py_puresitedir/loggerhead
%py_puresitedir/loggerhead/*
%py_puresitedir/loggerhead-%{version}-*.egg-info
%{_bindir}/serve-branches
%{_bindir}/loggerhead.wsgi
%{_docdir}/loggerhead
%_mandir/man1/*
%doc README NEWS COPYING.txt



%changelog
* Sat Aug 13 2011 Crispin Boylan <crisb@mandriva.org> 1.18.1-2mdv2012.0
+ Revision: 694358
- Mark as compatible with bzr 2.4.0

* Mon Apr 11 2011 Crispin Boylan <crisb@mandriva.org> 1.18.1-1
+ Revision: 652485
- New release

* Thu Nov 11 2010 Crispin Boylan <crisb@mandriva.org> 1.18-1mdv2011.0
+ Revision: 596130
- Add new binaries
- New release, drop applied patch

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 1.17-4mdv2011.0
+ Revision: 591910
- Fix file list for py2.7
- Rebuild

* Sun Aug 08 2010 Crispin Boylan <crisb@mandriva.org> 1.17-3mdv2011.0
+ Revision: 567639
- Compatible with bzr 2.2

* Tue Feb 23 2010 Crispin Boylan <crisb@mandriva.org> 1.17-2mdv2010.1
+ Revision: 510372
- Patch 0 - mark as compatible with bzr 2.1

* Fri Aug 21 2009 Crispin Boylan <crisb@mandriva.org> 1.17-1mdv2010.0
+ Revision: 418975
- Release 1.17

* Wed Jul 29 2009 Crispin Boylan <crisb@mandriva.org> 1.11-0.5mdv2010.0
+ Revision: 403964
- Update to rev 381 (bzr1.17 compat)

* Sun Jun 28 2009 Crispin Boylan <crisb@mandriva.org> 1.11-0.4mdv2010.0
+ Revision: 390175
- Update to bzr rev 378 (shows tags now)

* Sat Jun 13 2009 Crispin Boylan <crisb@mandriva.org> 1.11-0.3mdv2010.0
+ Revision: 385672
- BuildRequires: python-paste
- BuildRequires python-pkg-resources
- Update binary
- Update to bzr revision 366
- Use setup.py as now installs as plugin by default
- Minimum version is bzr 1.13

* Mon May 18 2009 Crispin Boylan <crisb@mandriva.org> 1.11-0.2mdv2010.0
+ Revision: 376846
- Provides loggerhead
- Bump release
- Add to description, this is the plugin version
- Initial package for mandriva
- create bzr-loggerhead

