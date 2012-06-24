Summary:	Solving "harmonic inversion" problem
Summary(pl.UTF-8):	Rozwiązywanie problemu "inwersji harmonicznych"
Name:		harminv
Version:	1.3.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://ab-initio.mit.edu/harminv/%{name}-%{version}.tar.gz
# Source0-md5:	d3f49f1c90856b3b2e8b77dc4a99c37a
URL:		http://ab-initio.mit.edu/harminv/
BuildRequires:	blas-devel
BuildRequires:	lapack-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Harminv is a free program (and accompanying library) to solve the
problem of "harmonic inversion". Given a discrete, finite-length
signal that consists of a sum of finitely-many sinusoids (possibly
exponentially decaying), it determines the frequencies, decay
constants, amplitudes, and phases of those sinusoids.

%description -l pl.UTF-8
Harminv jest darmowym programem do rozwiązywania problemu "inwersji
harmonicznych". Mając zadany dyskretny, skończonej długości sygnał
składający się z sumy skończonej liczby sinusoid (które mogą wygasać
wykładniczo), określa częstotliwości, stałe wygasania, amplitudy i
fazy tych sinusoid.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%attr(755,root,root) %{_bindir}/harminv
# XXX: shared, static?
%{_libdir}/libharminv.*
%{_includedir}/harminv.h
%{_mandir}/man1/harminv*
%{_pkgconfigdir}/harminv.pc
