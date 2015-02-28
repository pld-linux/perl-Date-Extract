#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Date
%define		pnam	Extract
%include	/usr/lib/rpm/macros.perl
Summary:	Date::Extract - extract probable dates from strings
Name:		perl-Date-Extract
Version:	0.05
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	045879fe373f8e99c215b3a466103445
URL:		http://search.cpan.org/dist/Date-Extract/
BuildRequires:	perl-DateTime-Format-Natural
BuildRequires:	perl-Test-MockTime
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
