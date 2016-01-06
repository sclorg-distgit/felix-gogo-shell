%{?scl:%scl_package felix-gogo-shell}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}felix-gogo-shell
Version:        0.10.0
Release:        15.3%{?dist}
Summary:        Community OSGi R4 Service Platform Implementation - Basic Commands
License:        ASL 2.0
URL:            http://felix.apache.org/site/apache-felix-gogo.html
BuildArch:      noarch

Source0:        http://mirror.catn.com/pub/apache//felix/org.apache.felix.gogo.shell-0.10.0-project.tar.gz
  
# Changed GroupID from osgi to felix
Patch0:         %{pkg_name}-groupid.patch

Patch1:         ignoreActivatorException.patch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.felix:gogo-parent:pom:)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.felix:org.apache.felix.gogo.runtime)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.felix:org.osgi.compendium)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.felix:org.osgi.core)
BuildRequires:  %{?scl_prefix}mvn(org.mockito:mockito-all)

%description
Apache Felix is a community effort to implement the OSGi R4 Service Platform
and other interesting OSGi-related technologies under the Apache license. The
OSGi specifications originally targeted embedded devices and home services
gateways, but they are ideally suited for any project interested in the
principles of modularity, component-orientation, and/or service-orientation.
OSGi technology combines aspects of these aforementioned principles to define a
dynamic service deployment framework that is amenable to remote management.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -q -n org.apache.felix.gogo.shell-%{version}
%patch0 -p1 -F3
%patch1
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE NOTICE
%dir %{_javadir}/felix-gogo-shell
%dir %{_mavenpomdir}/felix-gogo-shell

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Jul 10 2015 Mat Booth <mat.booth@redhat.com> - 0.10.0-15.3
- Fix unowned directories

* Tue Jun 30 2015 Roland Grunberg <rgrunber@redhat.com> - 0.10.0-15.2
- Change %%license to %%doc (for RHEL 6 builds).

* Mon Jun 29 2015 Mat Booth <mat.booth@redhat.com> - 0.10.0-15.1
- Import latest from Fedora

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.10.0-14
- Cleanup spec file

* Wed Jul 16 2014 Mat Booth <mat.booth@redhat.com> - 0.10.0-13
- Fix unowned directory.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Alexander Kurtakov <akurtako@redhat.com> 0.10.0-11
- Start using mvn_build/install.

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.10.0-10
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 5 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.10.0-9
- Fix FTBFS.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.10.0-7
- Initial SCLization.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.10.0-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.10.0-3
- Temporary fix for bug 786041

* Wed Jan 18 2012 Tomas Radej <tradej@redhat.com> - 0.10.0-2
- Changed jar path

* Mon Jan 09 2012 Tomas Radej <tradej@redhat.com> - 0.10.0-1
- Initial packaging
