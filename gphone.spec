Summary:	internet phone with a gtk interface
Summary(pl):	Internetowy telefon z interfejsem GTK
Name:		gphone
Version:	0.5.2
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://download.sourceforge.net/pub/sourceforge/gphone/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fixes.patch
URL:		http://gphone.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libgsm-devel
BuildRequires:	popt-devel
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
gphone is an "internet phone" -- it lets you talk (out loud, not by
typing) over a network connection.

%description -l pl
gphone jest "telefonem internetowym": pozwala rozmawia� (dos�ownie,
nie stukaj�c w klawiatur�) u�ytkownikom po��czonym sieci�.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
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
%attr(755,root,root) %{_bindir}/*