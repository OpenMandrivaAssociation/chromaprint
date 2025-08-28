%define major 1
%define oldlibname %mklibname %{name} 1
%define libname %mklibname %{name}
%define develname %mklibname -d %{name}

# FIXME As of LLVM 21.1, the test suite takes up
# all RAM while linking at -O3, so make
# sure we don't use -O3
%global optflags %{optflags} -O2

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
BuildRequires:	fftw-devel >= 3
# This is needed for examples
BuildRequires:	ffmpeg-devel
BuildRequires:	boost-devel
BuildSystem:	cmake
BuildOption:	-DBUILD_EXAMPLES:BOOL=ON
BuildOption:	-DBUILD_TOOLS:BOOL=ON
BuildOption:	-DBUILD_TESTS:BOOL=ON

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
# Renamed after 6.0 2025-08-27
%rename %{oldlibname}

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
