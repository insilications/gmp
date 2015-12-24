Name:           gmp
Version:        6.0.0
Release:        18
License:        LGPL-3.0 GPL-3.0
Summary:        GNU multiprecision arithmetic library
Url:            http://gmplib.org/
Group:          devel
Source0:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}a.tar.xz
BuildRequires:  grep
BuildRequires:  libstdc++-dev

%description
GNU multiprecision arithmetic library.

%package -n libgmpxx4
License:        LGPL-3.0 and GPL-3.0
Summary:        GNU multiprecision arithmetic library
Group:          devel

%description -n libgmpxx4
GNU multiprecision arithmetic library.


%package dev
License:        LGPL-3.0 and GPL-3.0
Summary:        GNU multiprecision arithmetic library
Group:          devel
Requires:       gmp-lib 
Requires:       libgmpxx4

%description  dev
GNU multiprecision arithmetic library.

%package doc
License:        LGPL-3.0 and GPL-3.0
Summary:        GNU multiprecision arithmetic library
Group:          doc

%description  doc
GNU multiprecision arithmetic library.

%package lib
License:        LGPL-3.0 and GPL-3.0
Summary:        GNU multiprecision arithmetic library
Group:          devel

%description lib
GNU multiprecision arithmetic library.

%prep
%setup -q

%build
# gmp fails to compile with PIE
export CFLAGS="-O2  -g2 "
export CXXFLAGS="-O2 -g2"

./configure --host=%{_arch}-unknown-linux-gnu --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/bin --sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 --libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/usr/com --mandir=/usr/share/man --infodir=/usr/share/info --enable-cxx=detect --disable-static --enable-shared

make %{?_smp_mflags}
make check

%install
%make_install

%files

%files -n libgmpxx4
%{_libdir}/libgmpxx.so.4
%{_libdir}/libgmpxx.so.4.4.0

%files dev
%{_includedir}/gmp.h
%{_includedir}/gmpxx.h
%{_libdir}/libgmp.so
%{_libdir}/libgmpxx.so

%files doc
%{_infodir}/gmp.info
%{_infodir}/gmp.info-2
%{_infodir}/gmp.info-1

%files lib
%{_libdir}/libgmp.so.10
%{_libdir}/libgmp.so.10.2.0


