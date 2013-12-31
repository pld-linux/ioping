Summary:	simple disk I/O latency measuring tool
Summary(pl.UTF-8):	proste narzędzie do badania opóźnień I/O dysku
Name:		ioping
Version:	0.8
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	http://ioping.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	7c91be09eef8c91199d7abfd1f4e673c
URL:		http://code.google.com/p/ioping/
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
