%define	major		0
%define	libname		%mklibname %{name} %{major}
%define	develname	%mklibname -d %{name}
Name:		chromaprint
Version:		0.7
Release:		1
Summary:		Library and tool implementing the AcoustID fingerprinting
Group:		Sound
License:		LGPLv2+
URL:		http://www.acoustid.org/chromaprint/
Source:		https://github.com/downloads/lalinsky/chromaprint/%{name}-%{version}.tar.gz
BuildRequires:	cmake >= 2.6
BuildRequires:	fftw-devel >= 3
# This is needed for examples
BuildRequires:	ffmpeg-devel
BuildRequires:	boost-devel

%description
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.
The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n %{libname}
Summary:		Library implementing the AcoustID fingerprinting
Group:		System/Libraries

%description -n %{libname}
Chromaprint library is the core component of the AcoustID project. It's a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.
The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n %{develname}
Summary:        Headers for developing programs that will use %{name} 
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}. 


%prep
%setup -q
%apply_patches


%build
%cmake -DBUILD_EXAMPLES=ON -DBUILD_TESTS=off
%make
#make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C build
rm  -f %{buildroot}%{_libdir}/lib*.la


%files
%doc README.txt
%{_bindir}/fpcalc

%files -n %{libname}
%doc CHANGES.txt COPYING.txt NEWS.txt README.txt
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/chromaprint.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc



%changelog
* Wed Oct 10 2012 Giovanni Mariani <mc2374@mclink.it> 0.7-1
- New release 0.7
- Dropped P0-P1 (applied upstream)
- Dropped BuildRoot and %%mkrel
- Added README.txt to doc list

* Mon Jun 11 2012 Götz Waschk <waschk@mandriva.org> 0.6-1
+ Revision: 804384
- add git patches for ffmpeg 0.11
- import chromaprint

* Mon Jun 11 2012 Goetz Waschk <goetz@mandriva.org> 0.6-1
- build on Mandriva

* Tue Feb 7 2012 Ismael Olea <ismael@olea.org> - 0.6-4
- moved the obsoletes python-chromaprint to libchromaprint

* Mon Feb 6 2012 Ismael Olea <ismael@olea.org> - 0.6-3
- cosmetic SPEC changes
- obsoleting python-chromaprint (see #786946)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 27 2011 Ismael Olea <ismael@olea.org> - 0.6-1
- update to 0.6
- python bindings removed
- python not a requirment now

* Wed Dec 07 2011 Ismael Olea <ismael@olea.org> - 0.5-4
- minor spec enhancements

* Mon Dec 05 2011 Ismael Olea <ismael@olea.org> - 0.5-3
- Macro cleaning at spec

* Thu Nov 18 2011 Ismael Olea <ismael@olea.org> - 0.5-2
- first version for Fedora

* Thu Nov 10 2011 Ismael Olea <ismael@olea.org> - 0.5-1
- update to 0.5
- subpackage for fpcalc 

* Sat Aug 06 2011 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.4-1
- Initial package
