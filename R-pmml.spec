#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pmml
Version  : 1.5.4
Release  : 7
URL      : https://cran.r-project.org/src/contrib/pmml_1.5.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pmml_1.5.4.tar.gz
Summary  : Generate PMML for Various Models
Group    : Development/Tools
License  : GPL-2.0
Requires: R-XML
BuildRequires : R-XML
BuildRequires : clr-R-helpers

%description
language which provides a way for applications to define statistical and
    data mining models and to share models between PMML compliant applications.

%prep
%setup -q -c -n pmml

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521211653

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521211653
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pmml
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pmml
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pmml
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library pmml|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pmml/ChangeLog
/usr/lib64/R/library/pmml/DESCRIPTION
/usr/lib64/R/library/pmml/INDEX
/usr/lib64/R/library/pmml/Meta/Rd.rds
/usr/lib64/R/library/pmml/Meta/data.rds
/usr/lib64/R/library/pmml/Meta/features.rds
/usr/lib64/R/library/pmml/Meta/hsearch.rds
/usr/lib64/R/library/pmml/Meta/links.rds
/usr/lib64/R/library/pmml/Meta/nsInfo.rds
/usr/lib64/R/library/pmml/Meta/package.rds
/usr/lib64/R/library/pmml/NAMESPACE
/usr/lib64/R/library/pmml/R/pmml
/usr/lib64/R/library/pmml/R/pmml.rdb
/usr/lib64/R/library/pmml/R/pmml.rdx
/usr/lib64/R/library/pmml/data/audit.RData
/usr/lib64/R/library/pmml/data/houseVotes84.rda
/usr/lib64/R/library/pmml/help/AnIndex
/usr/lib64/R/library/pmml/help/aliases.rds
/usr/lib64/R/library/pmml/help/paths.rds
/usr/lib64/R/library/pmml/help/pmml.rdb
/usr/lib64/R/library/pmml/help/pmml.rdx
/usr/lib64/R/library/pmml/html/00Index.html
/usr/lib64/R/library/pmml/html/R.css
