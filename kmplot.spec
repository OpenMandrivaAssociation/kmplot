%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	A mathematical function plotter
Name:		kmplot
Version:	21.03.80
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kmplot
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5DBusAddons)
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
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
DESTDIR="%{buildroot}" %ninja install -C build
%find_lang %{name} --with-html --with-man
