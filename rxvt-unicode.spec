#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rxvt-unicode
Version  : 9.26
Release  : 12
URL      : http://dist.schmorp.de/rxvt-unicode/Attic/rxvt-unicode-9.26.tar.bz2
Source0  : http://dist.schmorp.de/rxvt-unicode/Attic/rxvt-unicode-9.26.tar.bz2
Summary  : A customizable terminal emulator forked from rxvt
Group    : Development/Tools
License  : GPL-3.0
Requires: rxvt-unicode-bin = %{version}-%{release}
Requires: rxvt-unicode-data = %{version}-%{release}
Requires: rxvt-unicode-license = %{version}-%{release}
Requires: rxvt-unicode-man = %{version}-%{release}
BuildRequires : libXft
BuildRequires : libXft-dev
BuildRequires : ncurses
BuildRequires : pkgconfig(xt)
Patch1: 0001-Treat-unknown-capabilities-as-user-defined.patch

%description
Features of rxvt-unicode include international language support through
Unicode, transparency, the ability to display multiple font types and support
for Perl extensions.

%package bin
Summary: bin components for the rxvt-unicode package.
Group: Binaries
Requires: rxvt-unicode-data = %{version}-%{release}
Requires: rxvt-unicode-license = %{version}-%{release}

%description bin
bin components for the rxvt-unicode package.


%package data
Summary: data components for the rxvt-unicode package.
Group: Data

%description data
data components for the rxvt-unicode package.


%package license
Summary: license components for the rxvt-unicode package.
Group: Default

%description license
license components for the rxvt-unicode package.


%package man
Summary: man components for the rxvt-unicode package.
Group: Default

%description man
man components for the rxvt-unicode package.


%prep
%setup -q -n rxvt-unicode-9.26
cd %{_builddir}/rxvt-unicode-9.26
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658206826
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --disable-static --enable-256color --disable-perl --enable-xft
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1658206826
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rxvt-unicode
cp %{_builddir}/rxvt-unicode-9.26/COPYING %{buildroot}/usr/share/package-licenses/rxvt-unicode/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/terminfo
mv $HOME/.terminfo/* %{buildroot}/usr/share/terminfo/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/urclock
/usr/bin/urxvt
/usr/bin/urxvtc
/usr/bin/urxvtd

%files data
%defattr(-,root,root,-)
/usr/share/terminfo/r/rxvt-unicode
/usr/share/terminfo/r/rxvt-unicode-256color

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rxvt-unicode/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/urxvt.1
/usr/share/man/man1/urxvtc.1
/usr/share/man/man1/urxvtd.1
/usr/share/man/man7/urxvt.7
