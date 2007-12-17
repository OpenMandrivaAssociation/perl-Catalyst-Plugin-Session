%define realname Catalyst-Plugin-Session
%define name	perl-%{realname}
%define	modprefix Catalyst

%define version	0.19
%define release	%mkrel 1

Summary:	Generic Session plugin for Catalyst
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Digest)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Object::Signature)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::MockObject) >= 1.01
BuildRequires:	perl(Test::More)
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
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%clean
rm -rf %{buildroot}



