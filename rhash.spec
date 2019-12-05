Name:           rhash
Version:        1.3.5
Release:        5
Summary:        Great utility for computing hash sums
License:        MIT
URL:            https://github.com/rhash/RHash
Source0:        https://github.com/rhash/RHash/archive/v%{version}/rhash-%{version}.tar.gz

%description
RHash is designed to calculate  and verificate magnet links and hash sums.
It supports a wide range of hash sums such as CRC32,  MD4, MD5,  SHA1, SHA256,
SHA512, SHA3, AICH, ED2K, Tiger, DC++ TTH, BitTorrent BTIH, GOST R 34.11-94,
RIPEMD-160, HAS-160, EDON-R, Whirlpool and Snefru. The features include processing
directories recursively, independent to platform and output in a user-defined format.
This package also provides a professional,  portable,  thread-safe  C library. It's
small and easy to learn.

%package        devel
Summary:        Headers for rhash
Requires:       rhash = %{version}-%{release}

%description    devel
This package contains header files for developing applications with rhash APIs.

%package        help
Summary:        Documentation for rhash
%description    help
Documentation for rhash

%prep
%autosetup -n RHash-%{version}
sed -i -e '/^INSTALL_SHARED/s/644/755/' librhash/Makefile


%build
%make_build OPTFLAGS="%{optflags}" OPTLDFLAGS="-g %{?__global_ldflags}" build-shared

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} install-shared install-lib-shared
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} -C librhash install-so-link install-headers


%check
make test-shared

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/rhashrc
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files help
%doc README
%{_mandir}/man1/*.1*



%changelog
* Sat Dec 4 2019 lihao <lihao129@huawei.com> - 1.3.5-5
- Bump release for updating binary package in OBS

* Sat Nov 30 2019 lihao <lihao129@huawei.com> - 1.3.5-4
- Package Init

