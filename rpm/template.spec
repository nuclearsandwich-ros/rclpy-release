%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-rclpy
Version:        1.9.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rclpy package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-ament-index-python
Requires:       ros-galactic-builtin-interfaces
Requires:       ros-galactic-rcl
Requires:       ros-galactic-rcl-action
Requires:       ros-galactic-rcl-interfaces
Requires:       ros-galactic-rcl-logging-interface
Requires:       ros-galactic-rcl-yaml-param-parser
Requires:       ros-galactic-rmw-implementation
Requires:       ros-galactic-rosgraph-msgs
Requires:       ros-galactic-rpyutils
Requires:       ros-galactic-unique-identifier-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-ament-cmake-gtest
BuildRequires:  ros-galactic-ament-cmake-pytest
BuildRequires:  ros-galactic-ament-lint-auto
BuildRequires:  ros-galactic-ament-lint-common
BuildRequires:  ros-galactic-pybind11-vendor
BuildRequires:  ros-galactic-python-cmake-module
BuildRequires:  ros-galactic-rcl
BuildRequires:  ros-galactic-rcl-action
BuildRequires:  ros-galactic-rcl-logging-interface
BuildRequires:  ros-galactic-rcl-yaml-param-parser
BuildRequires:  ros-galactic-rcpputils
BuildRequires:  ros-galactic-rcutils
BuildRequires:  ros-galactic-rmw-implementation
BuildRequires:  ros-galactic-rmw-implementation-cmake
BuildRequires:  ros-galactic-rosidl-generator-py
BuildRequires:  ros-galactic-test-msgs
BuildRequires:  ros-galactic-unique-identifier-msgs
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Package containing the Python client.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Thu May 20 2021 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 1.9.0-1
- Autogenerated by Bloom

* Mon May 10 2021 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 1.8.2-1
- Autogenerated by Bloom

* Tue Apr 20 2021 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 1.8.1-2
- Autogenerated by Bloom

* Mon Apr 12 2021 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 1.8.1-1
- Autogenerated by Bloom

* Tue Apr 06 2021 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 1.8.0-1
- Autogenerated by Bloom

* Thu Mar 25 2021 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 1.7.0-1
- Autogenerated by Bloom

* Thu Mar 18 2021 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 1.6.0-1
- Autogenerated by Bloom

* Mon Mar 08 2021 Claire Wang <clairewang@openrobotics.org> - 1.5.0-1
- Autogenerated by Bloom

