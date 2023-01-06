Name:           rhash
Version:        1.4.2
Release:        5
Summary:        Great utility for computing hash sums
License:        MIT
URL:            https://github.com/rhash/RHash
Source0:        https://github.com/rhash/RHash/archive/v%{version}/rhash-%{version}.tar.gz

#References: https://github.com/rhash/RHash/commit/79a1a0b3d267893c40ac31192b20e20969a3a79c
Patch0: Fix-bug-with-hash-options-in-check-mode.patch
Patch1: RHash-1.4.2-sw.patch
Patch2: 0001-fix-incorrect-total-message-in-check-embedded-mode.patch
Patch3: 0001-Fix-install-gmo-target-to-recompile-gmo-files-only-i.patch

BuildRequires:	gcc

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
%setup -n RHash-%{version} 
%patch0 -p1
%ifarch sw_64
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
sed -i -e '/^INSTALL_SHARED/s/644/755/' librhash/Makefile

%build
./configure --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --sysconfdir=%{_sysconfdir} --libdir=%{_libdir} --mandir=%{_mandir} --enable-lib-shared --enable-gettext
%make_build OPTFLAGS="%{optflags}" OPTLDFLAGS="-g %{?__global_ldflags}" build-shared

%install
%make_install
make DESTDIR=%{buildroot} -C librhash install-so-link install-lib-headers

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
%doc ChangeLog README.md
%{_mandir}/man1/*.1*

%changelog
* Fri Jan 6 2023 caofei <caofei@xfusion.com> - 1.4.2-5
-   Fix install-gmo target to recompile gmo files only if needed

* Fri Jan 6 2023 caofei<caofei@xfusion.com> - 1.4.2-4
- fix incorrect total message in check-embedded mode

* Tue Oct 25 2022 wuzx<wuzx1226@qq.com> - 1.4.2-3
- Add sw64 architecture

* Fri Oct 21 2022 zhangruifang <zhangruifang1@h-partners.com> - 1.4.2-2
- Fix bug with hash options in check mode

* Tue Nov 30 2021 zoulin <zoulin13@huawei.com> - 1.4.2-1
- Upgrade to 1.4.2

* Thu Apr 8 2021 shenyangyang <shenyangyang4@huawei.com> - 1.4.0-2
- Delete unneeded build requires

* Wed Aug 19 2020 shixuantong <shixuantong@huawei.com> - 1.4.0-1
- Upgrade to 1.4.0

* Sat Dec 4 2019 lihao <lihao129@huawei.com> - 1.3.5-5
- Bump release for updating binary package in OBS

* Sat Nov 30 2019 lihao <lihao129@huawei.com> - 1.3.5-4
- Package Init

