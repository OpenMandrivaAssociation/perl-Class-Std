%define module  Class-Std
%define name    perl-%{module}
%define release %mkrel 1
%define version v0.0.8

Name:               %{name}
Version:            %{version}
Release:            %{release}
Summary:            Support for creating standard "inside-out" classes
License:            GPL or Artistic
Group:              Development/Perl
Url:                http://search.cpan.org/dist/%{module}/
Source:             http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.bz2
BuildRequires:      perl perl-Module-Build
BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:          noarch

%description
Support for creating standard "inside-out" classes

%prep
%setup -q -n %{module}-%{version}

%build
# only when building from CVS (version 1.51-3mdk)
#CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
#make docs -i
# only when building from CVS (version 1.51-3mdk)
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/Std*
%{_mandir}/*/*
