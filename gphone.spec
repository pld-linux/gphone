# $Id: gphone.spec,v 1.5 2000-04-04 07:03:17 arturs Exp $

# This spec file is incomplete, has never been tested and WILL NOT WORK!

Summary: internet phone with a gtk interface
Name: gphone
Version: .1
Release: 1
Copyright: GPL
Group: Applications
Source: http://www.penguinpowered.com/~gphone/gphone-0.1.tar.gz
URL: http://www.penguinpowered.com/~gphone/gphone.html
Packager: Roland Dreier <dreier@linuxfreak.com>

%description
gphone is an "internet phone" -- it lets you talk (out loud, not by
typing) over a network connection.

%description -l pl
gphone jest "telefonem internetowym": pozwala rozmawiaæ (dos³ownie, nie
stukaj±c w klawiaturê) u¿ytkownikom po³±czonym sieci±.

%prep
%setup

%build
./configure --prefix=/usr
make

%install
make install

%files
