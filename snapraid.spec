Name:           snapraid
Summary:        Disk array backup for many large rarely-changed files
Version:        8.1
Release:        2%{?dist}
License:        GPLv3+
Group:          Applications/System
URL:            http://snapraid.sourceforge.net/
Source0:        http://downloads.sourceforge.net/snapraid/snapraid-%{version}.tar.gz

%description
SnapRAID is a backup program for disk arrays. It stores parity
information of your data and it's able to recover from up to six disk
failures. SnapRAID is mainly targeted for a home media center, with a
lot of big files that rarely change.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=%{buildroot}

%files
%doc COPYING AUTHORS HISTORY README
%{_bindir}/snapraid
%{_mandir}/man1/snapraid.1*

%changelog
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 24 2015 Eric Smith <spacewar@gmail.com> - 8.1-1
- Updated to latest upstream.

* Sat Feb 14 2015 Eric Smith <spacewar@gmail.com> - 7.1-1
- Updated to latest upstream.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 Eric Smith <spacewar@gmail.com> - 6.3-1
- Updated to latest upstream.

* Thu Jun 12 2014 Eric Smith <spacewar@gmail.com> - 6.2-1
- Updated to latest upstream.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Eric Smith <spacewar@gmail.com> - 6.1-3
- Revert to using bundled tommyds library, per request of the author
  of both, and bundling exception granted by FPC ticket #423.

* Fri Apr 18 2014 Eric Smith <spacewar@gmail.com> - 6.1-2
- Use separately packaged tommyds library.

* Fri Apr 18 2014 Eric Smith <spacewar@gmail.com> - 6.1-1
- Updated to latest upstream.

* Sun Jan 19 2014 Eric Smith <spacewar@gmail.com> - 5.2-1
- Initial build.
