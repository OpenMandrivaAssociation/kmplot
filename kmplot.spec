#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	A mathematical function plotter
Name:		kmplot
Version:	25.08.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/kmplot
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/kmplot/-/archive/%{gitbranch}/kmplot-%{gitbranchd}.tar.bz2#/kmplot-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kmplot-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6TextWidgets)
Conflicts:	kdeedu4-devel < 4.6.90

%rename plasma6-kmplot

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KmPlot is a mathematical function plotter for the KDE-Desktop.

It has built in a powerfull parser. You can plot different functions
simultaneously and combine their function terms to build new functions.
KmPlot supports functions with parameters and functions in polar
coordinates. Several grid modes are possible. Plots may be printed with
high precision in correct scale.

%files -f %{name}.lang
%doc TODO
%{_bindir}/kmplot
%{_datadir}/metainfo/*
%{_datadir}/config.kcfg/*
%{_datadir}/icons/*/*/*/kmplot.*
%{_mandir}/man1/*
%{_libdir}/qt6/plugins/kf6/parts/*.so
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/interfaces/*.xml
