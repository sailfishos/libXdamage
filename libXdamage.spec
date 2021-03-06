# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       libXdamage
Summary:    X.Org X11 libXdamage runtime library
Version:    1.1.3
Release:    0
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source100:  libXdamage.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(damageproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xextproto)


%description
%{summary}.



%package devel
Summary:    X.Org X11 libXdamage development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%doc COPYING
%{_libdir}/libXdamage.so.1
%{_libdir}/libXdamage.so.1.1.0
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%doc AUTHORS README ChangeLog
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/Xdamage.h
%{_libdir}/libXdamage.so
%{_libdir}/pkgconfig/xdamage.pc
# << files devel

