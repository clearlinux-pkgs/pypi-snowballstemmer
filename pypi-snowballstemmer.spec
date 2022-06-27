#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6646265B586B83CB (mitya57@gmail.com)
#
Name     : pypi-snowballstemmer
Version  : 2.2.0
Release  : 52
URL      : https://files.pythonhosted.org/packages/44/7b/af302bebf22c749c56c9c3e8ae13190b5b5db37a33d9068652e8f73b7089/snowballstemmer-2.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/44/7b/af302bebf22c749c56c9c3e8ae13190b5b5db37a33d9068652e8f73b7089/snowballstemmer-2.2.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/44/7b/af302bebf22c749c56c9c3e8ae13190b5b5db37a33d9068652e8f73b7089/snowballstemmer-2.2.0.tar.gz.asc
Summary  : This package provides 29 stemmers for 28 languages generated from Snowball algorithms.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-snowballstemmer-license = %{version}-%{release}
Requires: pypi-snowballstemmer-python = %{version}-%{release}
Requires: pypi-snowballstemmer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Snowball stemming library collection for Python
===============================================

%package license
Summary: license components for the pypi-snowballstemmer package.
Group: Default

%description license
license components for the pypi-snowballstemmer package.


%package python
Summary: python components for the pypi-snowballstemmer package.
Group: Default
Requires: pypi-snowballstemmer-python3 = %{version}-%{release}

%description python
python components for the pypi-snowballstemmer package.


%package python3
Summary: python3 components for the pypi-snowballstemmer package.
Group: Default
Requires: python3-core
Provides: pypi(snowballstemmer)

%description python3
python3 components for the pypi-snowballstemmer package.


%prep
%setup -q -n snowballstemmer-2.2.0
cd %{_builddir}/snowballstemmer-2.2.0
pushd ..
cp -a snowballstemmer-2.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656372598
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-snowballstemmer
cp %{_builddir}/snowballstemmer-2.2.0/COPYING %{buildroot}/usr/share/package-licenses/pypi-snowballstemmer/f8d2c0ec1880e550ce455b2c660493b9d81f496d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-snowballstemmer/f8d2c0ec1880e550ce455b2c660493b9d81f496d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*