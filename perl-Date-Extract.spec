#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Date
%define		pnam	Extract
Summary:	Date::Extract - extract probable dates from strings
Name:		perl-Date-Extract
Version:	0.06
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	21fd316d2b6b0a6ab40f381f9e978cdc
URL:		http://search.cpan.org/dist/Date-Extract/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Data-Inheritable
BuildRequires:	perl-DateTime-Format-Natural
BuildRequires:	perl-DateTime-Locale
BuildRequires:	perl-Test-MockTime
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date::Extract is a Perl module for extracting date from strings.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Date/Extract.pm
%{_mandir}/man3/*
