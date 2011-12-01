%global base_name exec
%global short_name commons-%{base_name}

Name:           apache-commons-exec
Version:        1.1
Release:        5
Summary:        Java library to reliably execute external processes from within the JVM

Group:          Development/Java
License:        ASL 2.0
URL:            http://commons.apache.org/exec/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  iputils
BuildRequires:  java-devel >= 0:1.6.0
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-idea-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-release-plugin
Requires:       java >= 0:1.6.0
Requires:       jpackage-utils
Requires(post): jpackage-utils
Requires(postun):jpackage-utils
BuildArch:      noarch

%description
Commons Exec is a library for dealing with external process execution and
environment management in Java.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src

# Shell scripts used for unit tests must be executable (see
# http://commons.apache.org/exec/faq.html#environment-testing)
chmod a+x src/test/scripts/*.sh


%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
mvn-jpp \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    install javadoc:javadoc


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_javadir}
cp -p target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}
ln -s %{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p pom.xml %{buildroot}/%{_datadir}/maven2/poms/JPP-%{name}.pom

%add_to_maven_depmap org.apache.maven %{name} %{version} JPP %{name}


%clean
rm -rf %{buildroot}


%post
%update_maven_depmap


%postun
%update_maven_depmap


%files
%defattr(-,root,root,-)
%doc LICENSE.txt NOTICE.txt STATUS
%{_mavenpomdir}/*
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*


%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


