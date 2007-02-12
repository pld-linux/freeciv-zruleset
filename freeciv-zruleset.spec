Summary:	Alternate ruleset for FreeCiv
Summary(pl.UTF-8):	Alternatywny zbiór reguł dla FreeCiva
Name:		freeciv-zruleset
Version:	2
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://nbtsc.org/~aredridel/2006/06/03/zruleset-%{version}.zip
# Source0-md5:	f9770483c65f96aa14f1b459408e1071
Requires:	freeciv-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alternate ruleset for FreeCiv.

%description -l pl.UTF-8
Alternatywny zbiór reguł dla FreeCiva.

%prep
%setup -q -n zruleset%{version}

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
