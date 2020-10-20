#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pmml
Version  : 2.3.1
Release  : 38
URL      : https://cran.r-project.org/src/contrib/pmml_2.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pmml_2.3.1.tar.gz
Summary  : Generate PMML for Various Models
Group    : Development/Tools
License  : GPL-3.0
Requires: R-XML
Requires: R-stringr
BuildRequires : R-XML
BuildRequires : R-stringr
BuildRequires : buildreq-R

%description
# pmml <a href='https://CRAN.R-project.org/package=pmml'><img src='man/figures/logo3.png' align="right" height="139" /></a>

%prep
%setup -q -c -n pmml
cd %{_builddir}/pmml

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589584157

%install
export SOURCE_DATE_EPOCH=1589584157
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pmml || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pmml/DESCRIPTION
/usr/lib64/R/library/pmml/INDEX
/usr/lib64/R/library/pmml/LICENSE
/usr/lib64/R/library/pmml/Meta/Rd.rds
/usr/lib64/R/library/pmml/Meta/data.rds
/usr/lib64/R/library/pmml/Meta/features.rds
/usr/lib64/R/library/pmml/Meta/hsearch.rds
/usr/lib64/R/library/pmml/Meta/links.rds
/usr/lib64/R/library/pmml/Meta/nsInfo.rds
/usr/lib64/R/library/pmml/Meta/package.rds
/usr/lib64/R/library/pmml/Meta/vignette.rds
/usr/lib64/R/library/pmml/NAMESPACE
/usr/lib64/R/library/pmml/NEWS.md
/usr/lib64/R/library/pmml/R/pmml
/usr/lib64/R/library/pmml/R/pmml.rdb
/usr/lib64/R/library/pmml/R/pmml.rdx
/usr/lib64/R/library/pmml/WORDLIST
/usr/lib64/R/library/pmml/data/audit.RData
/usr/lib64/R/library/pmml/data/houseVotes84.rda
/usr/lib64/R/library/pmml/doc/index.html
/usr/lib64/R/library/pmml/doc/packages_and_functions.R
/usr/lib64/R/library/pmml/doc/packages_and_functions.Rmd
/usr/lib64/R/library/pmml/doc/packages_and_functions.html
/usr/lib64/R/library/pmml/doc/xform_function.R
/usr/lib64/R/library/pmml/doc/xform_function.Rmd
/usr/lib64/R/library/pmml/doc/xform_function.html
/usr/lib64/R/library/pmml/help/AnIndex
/usr/lib64/R/library/pmml/help/aliases.rds
/usr/lib64/R/library/pmml/help/figures/logo3.png
/usr/lib64/R/library/pmml/help/paths.rds
/usr/lib64/R/library/pmml/help/pmml.rdb
/usr/lib64/R/library/pmml/help/pmml.rdx
/usr/lib64/R/library/pmml/html/00Index.html
/usr/lib64/R/library/pmml/html/R.css
/usr/lib64/R/library/pmml/tests/testthat.R
/usr/lib64/R/library/pmml/tests/testthat/audit.csv
/usr/lib64/R/library/pmml/tests/testthat/audit_3to1_table.csv
/usr/lib64/R/library/pmml/tests/testthat/audit_marital_table.csv
/usr/lib64/R/library/pmml/tests/testthat/audit_nor.csv
/usr/lib64/R/library/pmml/tests/testthat/audit_nor_fake_logical.csv
/usr/lib64/R/library/pmml/tests/testthat/audit_nor_logical.csv
/usr/lib64/R/library/pmml/tests/testthat/audit_r_build_in.csv
/usr/lib64/R/library/pmml/tests/testthat/bank.csv
/usr/lib64/R/library/pmml/tests/testthat/covtype2.csv
/usr/lib64/R/library/pmml/tests/testthat/credit.csv
/usr/lib64/R/library/pmml/tests/testthat/credit_class.csv
/usr/lib64/R/library/pmml/tests/testthat/credit_class_01.csv
/usr/lib64/R/library/pmml/tests/testthat/elnino.csv
/usr/lib64/R/library/pmml/tests/testthat/factor_10k.csv
/usr/lib64/R/library/pmml/tests/testthat/factor_40k.csv
/usr/lib64/R/library/pmml/tests/testthat/glm_issue3543_data.csv
/usr/lib64/R/library/pmml/tests/testthat/heart.csv
/usr/lib64/R/library/pmml/tests/testthat/house_votes_84.csv
/usr/lib64/R/library/pmml/tests/testthat/insurance.csv
/usr/lib64/R/library/pmml/tests/testthat/iris.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_bin.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_class_full_name_table.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_class_index_table.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_class_table.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_discretize_bool_sw.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_discretize_pl.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_discretize_pw.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_discretize_sl.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_discretize_sw.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_mini_dot.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_nor.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_nor_logical.csv
/usr/lib64/R/library/pmml/tests/testthat/iris_p_class_table.csv
/usr/lib64/R/library/pmml/tests/testthat/job_cat.csv
/usr/lib64/R/library/pmml/tests/testthat/job_cat_index.csv
/usr/lib64/R/library/pmml/tests/testthat/map_factor_400.csv
/usr/lib64/R/library/pmml/tests/testthat/numeric_10k.csv
/usr/lib64/R/library/pmml/tests/testthat/numeric_discretize_var.csv
/usr/lib64/R/library/pmml/tests/testthat/numeric_no_na_10k.csv
/usr/lib64/R/library/pmml/tests/testthat/petfood.csv
/usr/lib64/R/library/pmml/tests/testthat/pmml-4-4.xsd
/usr/lib64/R/library/pmml/tests/testthat/pmml-4-4_statespace.xsd
/usr/lib64/R/library/pmml/tests/testthat/random_data_small.csv
/usr/lib64/R/library/pmml/tests/testthat/test_add_attributes.R
/usr/lib64/R/library/pmml/tests/testthat/test_add_data_field_attributes.R
/usr/lib64/R/library/pmml/tests/testthat/test_add_data_field_children.R
/usr/lib64/R/library/pmml/tests/testthat/test_add_mining_field_attributes.R
/usr/lib64/R/library/pmml/tests/testthat/test_add_output_field.R
/usr/lib64/R/library/pmml/tests/testthat/test_datadictionary.R
/usr/lib64/R/library/pmml/tests/testthat/test_defunct.R
/usr/lib64/R/library/pmml/tests/testthat/test_file_to_xml_node.R
/usr/lib64/R/library/pmml/tests/testthat/test_function_to_pmml.R
/usr/lib64/R/library/pmml/tests/testthat/test_make_output_nodes.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.ARIMA.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.coxph.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.cv.glmnet.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.gbm.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.hclust.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.iForest.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.ksvm.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.lm.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.miningschema.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.naiveBayes.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.neighbr.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.nnet.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.randomForest.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.rfsrc.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.svm.R
/usr/lib64/R/library/pmml/tests/testthat/test_pmml.xgb.Booster.R
/usr/lib64/R/library/pmml/tests/testthat/test_presence_of_nodes.R
/usr/lib64/R/library/pmml/tests/testthat/test_save_pmml.R
/usr/lib64/R/library/pmml/tests/testthat/test_schema_validation.R
/usr/lib64/R/library/pmml/tests/testthat/test_transformations.R
