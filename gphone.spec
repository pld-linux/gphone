Summary:	Internet phone with a GTK+ interface
Summary(pl.UTF-8):	Internetowy telefon z interfejsem GTK+
Name:		gphone
Version:	0.5.2
Release:	4
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/gphone/%{name}-%{version}.tar.gz
# Source0-md5:	4d6623a6866653a612d3358028555643
Source1:	%{name}.desktop
Patch0:		%{name}-am_fixes.patch
URL:		http://gphone.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libgsm-devel
BuildRequires:	popt-devel
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gphone is an "internet phone" - it lets you talk (out loud, not by
typing) over a network connection.

%description -l pl.UTF-8
gphone jest "telefonem internetowym": pozwala rozmawiać (dosłownie,
nie stukając w klawiaturę) użytkownikom połączonym siecią.

%prep
%setup -q
%patch -P0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
