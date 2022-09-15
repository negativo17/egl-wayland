%global commit0 885f0a5e91fe9cfbfbcd98ff01f6b83503decef3
%global date 20220806
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:           egl-wayland
Version:        1.1.11
Release:        1%{?dist}
Summary:        Wayland EGL External Platform library
License:        MIT
URL:            https://github.com/NVIDIA/%{name}

%if 0%{?tag:1}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %url/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

Source1:        10_nvidia_wayland.json
Source2:        15_nvidia_gbm.json

BuildRequires:  meson
BuildRequires:  libtool
BuildRequires:  eglexternalplatform-devel
BuildRequires:  cmake
BuildRequires:  libdrm-devel
BuildRequires:  libglvnd-devel >= 1.3.4
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

# Required for directory ownership
Requires:       libglvnd-egl%{?_isa}

%description
Wayland EGL External Platform library

%package devel
Summary:        Wayland EGL External Platform library development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Wayland EGL External Platform library development package

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
* Thu Sep 15 2022 Simone Caronni <negativo17@gmail.com> - 1.1.11-1
- Update to 1.1.11.

* Wed Aug 10 2022 Simone Caronni <negativo17@gmail.com> - 1.1.10-4.20220806git885f0a5
- Update to latest snapshot.

* Wed Jun 29 2022 Simone Caronni <negativo17@gmail.com> - 1.1.10-3.20220626gitd0febee
- Update to latest snapshot:
  https://forums.developer.nvidia.com/t/properties-and-filters-windows-make-obs-hang-on-wayland-when-closed/213009/12

* Mon Jun 13 2022 Simone Caronni <negativo17@gmail.com> - 1.1.10-2
- Update to official 1.1.10 release.

* Thu Jun 09 2022 Simone Caronni <negativo17@gmail.com> - 1.1.10-1.20220601git247335d
- Update to latest 1.10 snapshot
  (https://github.com/negativo17/nvidia-driver/issues/131).

* Sat Feb 05 2022 Simone Caronni <negativo17@gmail.com> - 1.1.7-1
- First build.
