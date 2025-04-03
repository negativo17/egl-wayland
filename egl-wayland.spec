%global commit0 f1fd51456710b567717a970dd4e1b2347792ac13
%global date 20250313
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:           egl-wayland
Version:        1.1.19%{!?tag:~%{date}git%{shortcommit0}}
Release:        1%{?dist}
Summary:        EGLStream-based Wayland external platform
License:        MIT
URL:            https://github.com/NVIDIA/%{name}

%if 0%{?tag:1}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
%endif
# Explicit synchronization is in since 1.34:
Patch0:         %{name}-linux-drm-syncobj.patch

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  libtool
BuildRequires:  pkgconfig(egl) >= 1.5
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.1
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)

# Required for directory ownership
Requires:       libglvnd-egl%{?_isa}

%description
EGL External Platform library to add client-side Wayland support to EGL on top
of EGLDevice and EGLStream families of extensions.

This library implements an EGL External Platform interface to work along with
EGL drivers that support the external platform mechanism.

%package devel
Summary:        EGLStream-based Wayland external platform development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
EGL External Platform library to add client-side Wayland support to EGL on top
of EGLDevice and EGLStream families of extensions.

This library implements an EGL External Platform interface to work along with
EGL drivers that support the external platform mechanism.

This package contains development files.

%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -delete

%files
%doc README.md
%license COPYING
%{_libdir}/libnvidia-egl-wayland.so.1
%{_libdir}/libnvidia-egl-wayland.so.1.1.19
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json

%files devel
%{_datadir}/pkgconfig/wayland-eglstream-protocols.pc
%{_datadir}/wayland-eglstream/
%{_libdir}/libnvidia-egl-wayland.so
%{_libdir}/pkgconfig/wayland-eglstream.pc

%changelog
* Mon Mar 17 2025 Simone Caronni <negativo17@gmail.com> - 1.1.19~20250313gitf1fd514-1
- Update to latest snapshot.
- Trim changelog.
- Use a downloaded copy of the DRM syncobj protocol definition.

* Thu Sep 26 2024 Simone Caronni <negativo17@gmail.com> - 1.1.13.1-3
- Drop gbm ICD loader that went in egl-gbm (#163).

* Wed Aug 07 2024 Simone Caronni <negativo17@gmail.com> - 1.1.13.1-2
- Update build requirements.

* Mon Aug 05 2024 Simone Caronni <negativo17@gmail.com> - 1.1.13.1-1
- Update to 1.1.13.1 which includes the backported patch for driver 560+.

* Wed May 29 2024 Simone Caronni <negativo17@gmail.com> - 1.1.13-2
- Backport upstream patch.
