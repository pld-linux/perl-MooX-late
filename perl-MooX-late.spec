#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MooX
%define		pnam	late
Summary:	MooX::late - easily translate Moose code to Moo
Name:		perl-MooX-late
Version:	0.015
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2807107636e4a40903f1e2caff5fe529
URL:		http://search.cpan.org/dist/MooX-late/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Type::Utils) >= 1.000001
BuildRequires:	perl-Moo >= 1.006000
BuildRequires:	perl-Test-Fatal >= 0.010
BuildRequires:	perl-Test-Requires >= 0.06
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moo is a light-weight object oriented programming framework which aims
to be compatible with Moose. It does this by detecting when Moose has
been loaded, and automatically "inflating" its classes and roles to
full Moose classes and roles. This way, Moo classes can consume Moose
roles, Moose classes can extend Moo classes, and so forth.

However, the surface syntax of Moo differs somewhat from Moose. For
example the isa option when defining attributes in Moose must be
either a string or a blessed Moose::Meta::TypeConstraint object; but
in Moo must be a coderef. These differences in surface syntax make
porting code from Moose to Moo potentially tricky. MooX::late provides
some assistance by enabling a slightly more Moosey surface syntax.

MooX::late does the following:

Five features. It is not the aim of MooX::late to make every aspect of
Moo behave exactly identically to Moose. It's just going after the
low-hanging fruit. So it does five things right now, and I promise
that future versions will never do more than seven.

Previous releases of MooX::late added support for coerce => 1 and
default => $nonref. These features have now been added to Moo itself,
so MooX::late no longer has to deal with them.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes CREDITS INSTALL README TODO
%{perl_vendorlib}/MooX/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
