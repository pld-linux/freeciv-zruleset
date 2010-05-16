Summary:	Alternate ruleset for FreeCiv
Summary(pl.UTF-8):	Alternatywny zbiór reguł dla FreeCiva
Name:		freeciv-zruleset
Version:	3a
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://dinhe.net/~aredridel/2007/02/19/zruleset-%{version}.zip
# Source0-md5:	da7231f4343e11cc56e5ed1fb1d41673
BuildRequires:	unzip
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
install -d $RPM_BUILD_ROOT%{_datadir}/freeciv
cp -a * $RPM_BUILD_ROOT%{_datadir}/freeciv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/freeciv/zruleset
%{_datadir}/freeciv/zruleset/*.ruleset
%{_datadir}/freeciv/flags/*.png
%{_datadir}/freeciv/nation/*.ruleset
