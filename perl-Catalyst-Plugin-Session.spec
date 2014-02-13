%define upstream_name    Catalyst-Plugin-Session
%define upstream_version 0.39
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Generic Session plugin for Catalyst
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-Session-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Digest)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Object::Signature)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::MockObject) >= 1.01
BuildRequires:	perl(Test::More)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
The Session plugin is the base of two related parts of functionality required
for session management in web applications. The first part, the State, is
getting the browser to repeat back a session key, so that the web
application can identify the client and logically string several requests
together into a session. The second part, the Store, deals with the actual
storage of information about the client. This data is stored so that the it
may be revived for every request made by the same client. This plugin links
the two pieces together.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.320.0-1mdv2011.0
+ Revision: 684737
- update to new version 0.32

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.310.0-2
+ Revision: 680760
- mass rebuild

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 595082
- update to new version 0.31

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2011.0
+ Revision: 554164
- update to 0.30

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.290.0-1mdv2010.1
+ Revision: 460831
- update to 0.29

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.0
+ Revision: 418654
- update to 0.26

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.0
+ Revision: 406296
- rebuild using %%perl_convert_version

* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2010.0
+ Revision: 393775
- update to new version 0.25

* Thu Jun 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2010.0
+ Revision: 389093
- update to new version 0.24

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2010.0
+ Revision: 387000
- update to new version 0.23

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2010.0
+ Revision: 378165
- new version

  + Jérôme Quelin <jquelin@mandriva.org>
    - update to 0.22

* Mon Feb 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2009.1
+ Revision: 340782
- update to new version 0.20

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.19-3mdv2009.0
+ Revision: 255562
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2008.1
+ Revision: 97372
- update to new version 0.19

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2008.0
+ Revision: 69205
- update to new version 0.18

* Fri Jul 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2008.0
+ Revision: 56247
- update to new version 0.17

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2008.0
+ Revision: 47029
- update to new version 0.15

* Sun Apr 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.13-1mdv2008.0
+ Revision: 19303
- New version


* Thu Aug 10 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-10 19:29:01 (55447)
- Version 0.11

* Thu Aug 10 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-10 19:25:53 (55444)
- import perl-Catalyst-Plugin-Session-0.10-1mdv2007.0

* Wed Aug 02 2006 Scott karns <scottk@mandriva.org> 0.10-1mdv2007.0
- 0.10

* Thu May 04 2006 Scott karns <scottk@mandriva.org> 0.05-2mdk
- Adjusted BuildRequires

* Tue Jan 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.05-1mdk
- 0.05

* Fri Dec 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.02-1mdk
- Initial MDV RPM




