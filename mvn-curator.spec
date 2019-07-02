#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-curator
Version  : 2.6.0
Release  : 2
URL      : https://github.com/apache/curator/archive/apache-curator-2.6.0.tar.gz
Source0  : https://github.com/apache/curator/archive/apache-curator-2.6.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/curator/curator-client/2.6.0/curator-client-2.6.0.jar
Source2  : https://repo1.maven.org/maven2/org/apache/curator/curator-client/2.6.0/curator-client-2.6.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-curator-data = %{version}-%{release}

%description
Apache Curator
--------------
Curator is a set of Java libraries that make using Apache ZooKeeper much easier.

%package data
Summary: data components for the mvn-curator package.
Group: Data

%description data
data components for the mvn-curator package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/curator/curator-client/2.6.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/curator/curator-client/2.6.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/curator/curator-client/2.6.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/curator/curator-client/2.6.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/curator/curator-client/2.6.0/curator-client-2.6.0.jar
/usr/share/java/.m2/repository/org/apache/curator/curator-client/2.6.0/curator-client-2.6.0.pom
