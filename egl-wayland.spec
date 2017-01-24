Name:           egl-wayland
Version:        1.1.7
Release:        1%{?dist}
Summary:        Wayland EGL External Platform library

License:        MIT
URL:            https://github.com/NVIDIA/%{name}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        10_nvidia_wayland.json

BuildRequires:  meson
BuildRequires:  libtool
BuildRequires:  eglexternalplatform-devel
BuildRequires:  cmake3
BuildRequires:  mesa-libEGL-devel
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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
install -p -m 0644 -D %{SOURCE1} %{buildroot}%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json
find %{buildroot} -name '*.la' -delete

%{?ldconfig_scriptlets}

%files
%doc README.md
%license COPYING
%{_libdir}/*.so.*
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json

%files devel
%{_libdir}/libnvidia-egl-wayland.so
%{_libdir}/pkgconfig/wayland-eglstream.pc
%{_datadir}/pkgconfig/wayland-eglstream-protocols.pc
%{_datadir}/wayland-eglstream/

%changelog
* Sat Feb 05 2022 Simone Caronni <negativo17@gmail.com> - 1.1.7-1
- First build.
