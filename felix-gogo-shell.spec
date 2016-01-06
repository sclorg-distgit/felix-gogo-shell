%global project   felix
%global bundle    org.apache.felix.gogo.shell
%global groupId org.apache.felix
%global artifactId %{bundle}

%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package %{project}-gogo-shell}
%{?java_common_find_provides_and_requires}

Name:             %{?scl_prefix}%{project}-gogo-shell
Version:          0.10.0
Release:          8%{?dist}
Summary:          Community OSGi R4 Service Platform Implementation - Basic Commands
Group:            Development/Tools
License:          ASL 2.0
URL:              http://felix.apache.org/site/apache-felix-gogo.html

Source0:          http://mirror.catn.com/pub/apache//felix/org.apache.felix.gogo.shell-0.10.0-project.tar.gz
  
# Changed GroupID from osgi to felix
Patch0:           %{pkg_name}-groupid.patch

Patch1:           ignoreActivatorException.patch

BuildArch:        noarch

BuildRequires:    java-1.7.0-openjdk-devel >= 1.7.0
BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    %{?scl_prefix}felix-gogo-parent
BuildRequires:    %{?scl_prefix}felix-gogo-runtime

%description
Apache Felix is a community effort to implement the OSGi R4 Service Platform
and other interesting OSGi-related technologies under the Apache license. The
OSGi specifications originally targeted embedded devices and home services
gateways, but they are ideally suited for any project interested in the
principles of modularity, component-orientation, and/or service-orientation.
OSGi technology combines aspects of these aforementioned principles to define a
dynamic service deployment framework that is amenable to remote management.

%package javadoc
Group:            Documentation
Summary:          Javadoc for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p1 -F3
%patch1

%build
scl enable %{scl_maven} %{scl} - <<"EOF"
%mvn_build
EOF

%install
# jars
scl enable %{scl_maven} %{scl} - <<"EOF"
%mvn_install
EOF

%files -f .mfiles
%dir %{_javadir}/felix-gogo-shell
%dir %{_mavenpomdir}/felix-gogo-shell
%doc DEPENDENCIES LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Jan 16 2015 Mat Booth <mat.booth@redhat.com> - 0.10.0-8
- Related: rhbz#1175105 - Rebuilt to regenerate requires/provides
- Fix unowned directories

* Sat May 17 2014 Sami Wagiaalla <swagiaal@redhat.com> 0.10.0-7
- Build for DTS 3.
- Install javadoc manually
- Remvoe mockito BR.

* Fri May 16 2014 Sami Wagiaalla <swagiaal@redhat.com> 0.10.0-7
- Copy mvn_rpmbuild fix from RAWHIDE
- Use maven scl deps.
- enable maven scl for mvn_* macros

* Wed Feb 13 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.10.0-6
- Make noarch again.

* Wed Nov 21 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.10.0-5
- Add Exclusive arch.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Initial contribution to scl.
