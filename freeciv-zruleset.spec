Summary:	Alternate ruleset for FreeCiv
Summary(pl):	Alternatywny zbiór regu³ dla FreeCiva
Name:		freeciv-zruleset
Version:	1
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	zruleset-1.tar.gz
# Source0-md5:	c7be696f96cc9ea5b1f61d0a4664111d
Requires:	freeciv-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alternate ruleset for FreeCiv.

%description -l pl
Alternatywny zbiór regu³ dla FreeCiva.

%prep
%setup -q -n zruleset-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/freeciv/zruleset
install * $RPM_BUILD_ROOT%{_datadir}/freeciv/zruleset

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/freeciv/zruleset
%{_datadir}/freeciv/zruleset/*.ruleset
