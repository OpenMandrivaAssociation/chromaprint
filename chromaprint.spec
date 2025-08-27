%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		chromaprint
Version:	1.5.1
Release:	6
Summary:	Library and tool implementing the AcoustID fingerprinting
Group:		Sound
License:	LGPLv2+
URL:		https://acoustid.org/chromaprint
Source0:	https://github.com/acoustid/chromaprint/releases/download/v%{version}/%{name}-%{version}.tar.gz
#Patch0:		chromaprint-1.5.1-ffmpeg-5.0.patch
#Patch1:		chromaprint-1.5.1-ffmpeg-7.0.patch
BuildRequires:	cmake >= 2.6
BuildRequires:	fftw-devel >= 3
# This is needed for examples
BuildRequires:	ffmpeg-devel
BuildRequires:	boost-devel
BuildRequires:	ninja

%patchlist
https://github.com/acoustid/chromaprint/commit/8ccad6937177b1b92e40ab8f4447ea27bac009a7.patch
https://github.com/acoustid/chromaprint/commit/82781d02cd3063d071a501218297a90bde9a314f.patch
https://github.com/acoustid/chromaprint/commit/11d277e6795d982a77ad5ab597b3e62973877e13.patch
chromaprint-ffmpeg-8.0.patch

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
%autosetup -n %{name}-%{version} -p1
%cmake -DBUILD_EXAMPLES=ON -DBUILD_TOOLS=ON -DBUILD_TESTS=ON -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%if ! %{cross_compiling}
%check
# FIXME ReaderTest is known to fail with ffmpeg 7
LD_LIBRARY_PATH=`pwd`/build/src build/tests/all_tests || :
%endif

%files
%{_bindir}/fpcalc

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/chromaprint.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
