#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rxvt-unicode
Version  : 9.22
Release  : 1
URL      : http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-9.22.tar.bz2
Source0  : http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-9.22.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: rxvt-unicode-bin
Requires: rxvt-unicode-doc
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(x11)

%description
RXVT-UNICODE/URXVT FREQUENTLY ASKED QUESTIONS
Meta, Features & Commandline Issues
My question isn't answered here, can I ask a human?
Before sending me mail, you could go to IRC: "irc.freenode.net", channel
"#rxvt-unicode" has some rxvt-unicode enthusiasts that might be
interested in learning about new and exciting problems (but not FAQs :).

%package bin
Summary: bin components for the rxvt-unicode package.
Group: Binaries

%description bin
bin components for the rxvt-unicode package.


%package doc
Summary: doc components for the rxvt-unicode package.
Group: Documentation

%description doc
doc components for the rxvt-unicode package.


%prep
%setup -q -n rxvt-unicode-9.22

%build
export LANG=C
%configure --disable-static --disable-static --enable-256color --disable-perl
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/urxvt
/usr/bin/urxvtc
/usr/bin/urxvtd

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man7/*
