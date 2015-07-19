Summary:	A mathematical function plotter
Name:		kmplot
Version:	15.04.3
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kmplot
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
Conflicts:	kdeedu4-devel < 4.6.90

%description
KmPlot is a mathematical function plotter for the KDE-Desktop.

It has built in a powerfull parser. You can plot different functions
simultaneously and combine their function terms to build new functions.
KmPlot supports functions with parameters and functions in polar
coordinates. Several grid modes are possible. Plots may be printed with
high precision in correct scale.

%files
%doc COPYING COPYING.DOC TODO
%doc %{_kde_docdir}/HTML/*/kmplot
%{_kde_applicationsdir}/kmplot.desktop
%{_kde_appsdir}/kmplot
%{_kde_bindir}/kmplot
%{_kde_datadir}/appdata/kmplot.appdata.xml
%{_kde_datadir}/config.kcfg/kmplot.kcfg
%{_kde_iconsdir}/*/*/apps/kmplot.*
%{_kde_libdir}/kde4/libkmplotpart.so
%{_kde_mandir}/man1/kmplot.1.*
%{_kde_services}/kmplot_part.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.KmPlot.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.MainDlg.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.Parser.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.View.xml

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install_std -C build
