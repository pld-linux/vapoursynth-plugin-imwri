Summary:	Image reader/writer plugin for VapourSynth
Summary(pl.UTF-8):	Wtyczka VapourSynth odczytująca i zapisują obrazy
Name:		vapoursynth-plugin-imwri
Version:	2
Release:	1
# it was vapoursynth.spec subpackage up to 38/optionally 54
Epoch:		1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/vapoursynth/vs-imwri/archive/R%{version}/vs-imwri-R%{version}.tar.gz
# Source0-md5:	0991a8b6910b6890e27bfcbf81dd6779
URL:		https://github.com/vapoursynth/vs-imwri
# built with HDRI support
BuildRequires:	ImageMagick-c++-devel >= 1:7
BuildRequires:	libheif-devel
BuildRequires:	libjxl-devel
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtiff-devel >= 4
BuildRequires:	meson >= 0.51
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	vapoursynth-devel >= 55
Requires:	vapoursynth >= 55
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ImageMagick Writer-Reader (IMWRI) is a plugin that can read and write
many image formats.

%description -l pl.UTF-8
ImageMagick Writer-Reader (IMWRI) to wtyczka potrafiąca czytać i
zapisywać wiele formatów obrazów.

%prep
%setup -q -n vs-imwri-R%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/imwri.rst
%attr(755,root,root) %{_libdir}/vapoursynth/libimwri.so
