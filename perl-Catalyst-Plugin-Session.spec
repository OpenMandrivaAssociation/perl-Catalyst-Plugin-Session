%define upstream_name    Catalyst-Plugin-Session
%define upstream_version 0.30

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Generic Session plugin for Catalyst
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRequires:	perl-namespace-clean
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*
