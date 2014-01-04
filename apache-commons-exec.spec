%{?_javapackages_macros:%_javapackages_macros}
%global base_name exec
%global short_name commons-%{base_name}

Name:           apache-commons-exec
Version:        1.1
Release:        11.0%{?dist}
Summary:        Java library to reliably execute external processes from within the JVM


License:        ASL 2.0
URL:            http://commons.apache.org/exec/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  iputils
BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-install-plugin
BuildRequires:  maven-invoker-plugin
Requires:       java >= 1:1.6.0
Requires:       jpackage-utils
BuildArch:      noarch

%description
Commons Exec is a library for dealing with external process execution and
environment management in Java.


%package javadoc
Summary:        Javadocs for %{name}

Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src

# Shell scripts used for unit tests must be executable (see
# http://commons.apache.org/exec/faq.html#environment-testing)
chmod a+x src/test/scripts/*.sh


%build
mvn-rpmbuild install javadoc:aggregate


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{short_name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp -p pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%doc LICENSE.txt NOTICE.txt STATUS
%{_mavenpomdir}/*
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}


%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Mat Booth <fedora@matbooth.co.uk> - 1.1-10
- Add missing BRs

* Mon Jul 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-9
- Install NOTICE file with javadoc package
- Resolves: rhbz#984417

* Mon Feb 18 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.1-4
- Build with maven 3.
- Adapt to current guidelines.

* Mon Mar 07 2011 Tom Callaway <spot@fedoraproject.org> - 1.1-3
- fix maven fragment

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1.1-1
- Update to 1.1

* Wed Sep 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0.1-4
- BR iputils. Needed by tests.

* Wed Sep 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0.1-3
- Change maven plugin names to the new ones.

* Wed Feb  3 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 1.0.1-2
- Add missing %%post/%%postun Requires
- Use macro %%{_mavendepmapfragdir} instead of %%{_datadir}/maven2/pom
- Unown directories %%{_mavenpomdir} and %%{_mavendepmapfragdir}

* Mon Jan 18 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 1.0.1-1
- Initial RPM release
