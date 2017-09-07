%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	A mathematical function plotter
Name:		kmplot
Version:	17.08.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kmplot
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDELibs4Support)
Conflicts:	kdeedu4-devel < 4.6.90

%description
KmPlot is a mathematical function plotter for the KDE-Desktop.

It has built in a powerfull parser. You can plot different functions
simultaneously and combine their function terms to build new functions.
KmPlot supports functions with parameters and functions in polar
coordinates. Several grid modes are possible. Plots may be printed with
high precision in correct scale.

%files -f %{name}.lang
%doc COPYING COPYING.DOC TODO
%{_bindir}/kmplot
%{_datadir}/metainfo/*
%{_datadir}/config.kcfg/*
%{_datadir}/icons/*/*/*/kmplot.*
%{_datadir}/kservices5/kmplot_part.desktop
%{_datadir}/kxmlgui5/*
%{_mandir}/man1/*
%{_libdir}/qt5/plugins/*.so
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/interfaces/*.xml

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
DESTDIR="%{buildroot}" %ninja install -C build
%find_lang %{name} --with-html --with-man
