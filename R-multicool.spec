#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-multicool
Version  : 0.1.10
Release  : 9
URL      : https://cran.r-project.org/src/contrib/multicool_0.1-10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/multicool_0.1-10.tar.gz
Summary  : Permutations of Multisets in Cool-Lex Order
Group    : Development/Tools
License  : GPL-2.0
Requires: R-multicool-lib = %{version}-%{release}
BuildRequires : R-Rcpp
BuildRequires : buildreq-R

%description
multicool
=========

%package lib
Summary: lib components for the R-multicool package.
Group: Libraries

%description lib
lib components for the R-multicool package.


%prep
%setup -q -c -n multicool

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552948515

%install
export SOURCE_DATE_EPOCH=1552948515
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library multicool
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library multicool
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library multicool
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  multicool || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/multicool/DESCRIPTION
/usr/lib64/R/library/multicool/INDEX
/usr/lib64/R/library/multicool/Meta/Rd.rds
/usr/lib64/R/library/multicool/Meta/features.rds
/usr/lib64/R/library/multicool/Meta/hsearch.rds
/usr/lib64/R/library/multicool/Meta/links.rds
/usr/lib64/R/library/multicool/Meta/nsInfo.rds
/usr/lib64/R/library/multicool/Meta/package.rds
/usr/lib64/R/library/multicool/NAMESPACE
/usr/lib64/R/library/multicool/R/multicool
/usr/lib64/R/library/multicool/R/multicool.rdb
/usr/lib64/R/library/multicool/R/multicool.rdx
/usr/lib64/R/library/multicool/help/AnIndex
/usr/lib64/R/library/multicool/help/aliases.rds
/usr/lib64/R/library/multicool/help/multicool.rdb
/usr/lib64/R/library/multicool/help/multicool.rdx
/usr/lib64/R/library/multicool/help/paths.rds
/usr/lib64/R/library/multicool/html/00Index.html
/usr/lib64/R/library/multicool/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/multicool/libs/multicool.so
