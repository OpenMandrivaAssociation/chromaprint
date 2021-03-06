%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		chromaprint
Version:	1.5.0
Release:	1
Summary:	Library and tool implementing the AcoustID fingerprinting
Group:		Sound
License:	LGPLv2+
URL:		https://acoustid.org/chromaprint
Source0:	https://github.com/acoustid/chromaprint/releases/download/v%{version}/%{name}-%{version}.tar.gz
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
%setup -qn %{name}-v%{version}
%autopatch -p1


%build
%cmake -DBUILD_EXAMPLES=ON -DBUILD_TOOLS=ON -DBUILD_TESTS=off -G Ninja
%ninja


%install
%ninja_install -C build


%files
%{_bindir}/fpcalc

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/chromaprint.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
