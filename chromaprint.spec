%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		chromaprint
Version:	1.5.1
Release:	2
Summary:	Library and tool implementing the AcoustID fingerprinting
Group:		Sound
License:	LGPLv2+
URL:		https://acoustid.org/chromaprint
Source0:	https://github.com/acoustid/chromaprint/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:		chromaprint-1.5.1-ffmpeg-5.0.patch
BuildRequires:	cmake >= 2.6
BuildRequires:	fftw-devel >= 3
# This is needed for examples
BuildRequires:	ffmpeg-devel
BuildRequires:	boost-devel
BuildRequires:	ninja

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

%check
LD_LIBRARY_PATH=`pwd`/build/src build/tests/all_tests

%files
%{_bindir}/fpcalc

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/chromaprint.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
