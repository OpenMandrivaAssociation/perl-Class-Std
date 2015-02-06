%define upstream_name    Class-Std
%define upstream_version 0.011

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    Support for creating standard "inside-out" classes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:      perl(Module::Build)

BuildArch:          noarch
BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}

%description
Support for creating standard "inside-out" classes

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.11.0-2mdv2011.0
+ Revision: 680827
- mass rebuild

* Mon Dec 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.11.0-1mdv2011.0
+ Revision: 483036
- update to 0.011

* Thu Dec 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.11.0-1mdv2010.1
+ Revision: 482081
- update to 0.011
- update to 0.010

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0.9-3mdv2010.0
+ Revision: 430333
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.0.9-2mdv2009.0
+ Revision: 268400
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.9-1mdv2009.0
+ Revision: 195213
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 26 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> v0.0.8-1mdv2008.0
+ Revision: 31539
- add perl-version to BuildRequires to avoid tests to fail
- Import perl-Class-Std



* Tue May 22 2007 Shlomi Fish <shlomif@iglu.org.il> v0.0.8-1mdv2007.1
- Initial release.
