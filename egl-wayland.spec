%global commit0 6355c1605a0b0ccfdc1963170c5564b291ad0eb0
%global date 20240910
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:           egl-wayland
Version:        1.1.17%{!?tag:^%{date}git%{shortcommit0}}
Release:        1%{?dist}
Summary:        EGLStream-based Wayland external platform
License:        MIT
URL:            https://github.com/NVIDIA/%{name}

%if 0%{?tag:1}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

Source1:        10_nvidia_wayland.json
Source2:        15_nvidia_gbm.json

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  libtool
BuildRequires:  pkgconfig(egl) >= 1.5
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.1
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
# Explicit synchronization since 1.34:
BuildRequires:  pkgconfig(wayland-protocols) >= 1.34
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
install -m 0755 -d %{buildroot}%{_datadir}/egl/egl_external_platform.d/
install -pm 0644 %{SOURCE1} %{SOURCE2} %{buildroot}%{_datadir}/egl/egl_external_platform.d/
find %{buildroot} -name '*.la' -delete

%files
%doc README.md
%license COPYING
%{_libdir}/*.so.*
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json
%{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json

%files devel
%{_libdir}/libnvidia-egl-wayland.so
%{_libdir}/pkgconfig/wayland-eglstream.pc
%{_datadir}/pkgconfig/wayland-eglstream-protocols.pc
%{_datadir}/wayland-eglstream/

%changelog
* Thu Sep 12 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20240910git6355c16-1
- Update to latest snapshot.
- Trim changelog.
- Use updated packaging lines for snapshot versions.

* Fri Aug 30 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17-1.20240828git2d5ecff
- Update to latest snapshot.

* Wed Aug 21 2024 Simone Caronni <negativo17@gmail.com> - 1.1.15-3.20240819git8188db9
- Update to latest snapshot.

* Thu Aug 15 2024 Simone Caronni <negativo17@gmail.com> - 1.1.15-2.20240814gitf30cb0e
- Update to latest snapshot, fixes Qt6 webengine.

* Fri Aug 09 2024 Simone Caronni <negativo17@gmail.com> - 1.1.15-1
- Update to 1.1.15 final.

* Wed Aug 07 2024 Simone Caronni <negativo17@gmail.com> - 1.1.14-3.20240805gitc439cd5
- Update build requirements.

* Tue Aug 06 2024 Simone Caronni <negativo17@gmail.com> - 1.1.14-2.20240805gitc439cd5
- Update to latest snapshot.

* Mon Aug 05 2024 Simone Caronni <negativo17@gmail.com> - 1.1.14-1.20240801gite1216b5
- Update to latest 1.1.14 snapshot.

* Wed May 29 2024 Simone Caronni <negativo17@gmail.com> - 1.1.13-3.20240419git067e43d
- Update to latest snapshot.

* Wed Mar 06 2024 Simone Caronni <negativo17@gmail.com> - 1.1.13-2.20240119git369b337
- Update to the latest snapshot.

* Sat Oct 21 2023 Simone Caronni <negativo17@gmail.com> - 1.1.13-1
- Update to 1.1.13.

* Thu Jul 20 2023 Simone Caronni <negativo17@gmail.com> - 1.1.12-2.20230718gitea70449
- Update to latest snapshot.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 1.1.12-1
- Update to 1.1.12.
