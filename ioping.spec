Summary:	simple disk I/O latency measuring tool
Summary(pl.UTF-8):	proste narzędzie do badania opóźnień I/O dysku
Name:		ioping
Version:	1.2
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	https://github.com/koct9i/ioping/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	725a974e9be8a78c0f61e06463648e53
URL:		https://github.com/koct9i/ioping/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool lets you monitor I/O latency in real time, in a way similar
to how ping(1) does for network latency.

%description -l pl.UTF-8
To narzędzie pozwala na monitorowania opóźnień I/O w czasie
rzeczywistym w sposób zbliżony do programu ping(1) mierzącego
opóźnienia w sieci.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -std=c99" \
	LDFLAGS="%{rpmldflags} -lm" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX="%{_prefix}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ioping
%{_mandir}/man1/ioping.1*
