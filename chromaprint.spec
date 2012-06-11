%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name
Name:           chromaprint
Version:        0.6
Release:        %mkrel 1
Summary:        Library and tool implementing the AcoustID fingerprinting

Group:          Sound
License:        LGPLv2+
URL:            http://www.acoustid.org/chromaprint/
Source:         https://github.com/downloads/lalinsky/chromaprint/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fftw-devel >= 3
BuildRequires:  ffmpeg-devel
BuildRequires:  boost-devel
BuildRoot: %_tmppath/%name-%version-%release-root
%description
Chromaprint library is the core component of the AcoustID project. It's a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n %libname
Summary:        Library implementing the AcoustID fingerprinting
Group:          System/Libraries

%description -n %libname
Chromaprint library is the core component of the AcoustID project. It's a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n %develname
Summary:        Headers for developing programs that will use %{name} 
Group:          Development/C++
Requires:       %libname = %{version}-%{release}

%description -n %develname
This package contains the headers that programmers will need to develop
applications which will use %{name}. 


%prep
%setup -q


%build
%{cmake} -DBUILD_EXAMPLES=ON
make %{?_smp_mflags}


%install
rm -rf %buildroot
cd build
make install DESTDIR=%{buildroot}
rm  -f %{buildroot}%{_libdir}/lib*.la


%files
%doc README.txt
%_bindir/fpcalc

%files -n %libname
%doc CHANGES.txt COPYING.txt NEWS.txt
%{_libdir}/lib*.so.%{major}*

%files -n %develname
%{_includedir}/chromaprint.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

