Name:		apache-commons-exec
Version:	1.6.0
Release:	1
Summary:	Runs external processes from Java
Group:		Development/Java
License:	ASL 2.0
URL:		https://commons.apache.org/proper/commons-exec/
Source0:	https://archive.apache.org/dist/commons/exec/source/commons-exec-%{version}-src.tar.gz

BuildArch:	noarch
BuildRequires:	mvn(org.apache.commons:commons-parent:pom::)
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption(install):	--file-name commons-exec --link %{name} --alias commons-exec:commons-exec

%description
Apache Commons Exec runs external processes and manages their
environment. 1.6.0 is the current release and needs Java 8.
Tests are skipped.

%prep
%setup -q -n commons-exec-%{version}-src

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
