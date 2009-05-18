%define real_name	loggerhead
%define bzr_revno	352

Name:           bzr-loggerhead
Version:        1.11
Release:        %mkrel 0.1
Summary:        A web view for Bazaar

Group:          Development/Other
License:        GPL
URL:            https://launchpad.net/loggerhead
Source0:        https://launchpad.net/%{name}/stable/%{version}/+download/%{real_name}-%{version}-r%{bzr_revno}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

BuildArch:      noarch
BuildRequires:  python-devel bzr
Requires:       python >= 2.4
Requires:       bzr >= 1.11
Requires:	python-paste
Requires:	python-pygments
Requires:	python-simpletal

%description
Loggerhead is a web viewer for projects in bazaar. 
It can be used to navigate a branch history, annotate files, view patches, 
perform searches, etc. It's originally based on bazaar-webserve, which is 
itself based on hgweb for Mercurial.

%prep
%setup -q -n %{real_name}-%{version}-r%{bzr_revno}


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%py_puresitedir/bzrlib/plugins/loggerhead
cp -Rp * $RPM_BUILD_ROOT/%py_puresitedir/bzrlib/plugins/loggerhead

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%dir %py_puresitedir/bzrlib/plugins/loggerhead
%py_puresitedir/bzrlib/plugins/loggerhead/*
%doc README.txt NEWS COPYING.txt
