# $Id: gphone.spec,v 1.4 2000-03-28 16:54:22 baggins Exp $

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

%prep
%setup

%build
./configure --prefix=/usr
make

%install
make install

%files
