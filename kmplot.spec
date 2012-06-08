Name: kmplot
Summary: A mathematical function plotter
Version: 4.8.4
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 GFDL
URL: http://edu.kde.org/kmplot
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.xz
BuildRequires: kdelibs4-devel >= 2:%{version}
Conflicts: kdeedu4-devel < 4.6.90

%description
KmPlot is a mathematical function plotter for the KDE-Desktop.

It has built in a powerfull parser. You can plot different functions
simultaneously and combine their function terms to build new functions.
KmPlot supports functions with parameters and functions in polar
coordinates. Several grid modes are possible. Plots may be printed with
high precision in correct scale.

%files
%doc COPYING COPYING.DOC TODO
%_kde_appsdir/kmplot
%_kde_bindir/kmplot
%_kde_libdir/kde4/libkmplotpart.so
%_kde_iconsdir/*/*/apps/kmplot.*
%_kde_datadir/applications/kde4/kmplot.desktop
%_kde_datadir/config.kcfg/kmplot.kcfg
%_kde_services/kmplot_part.desktop
%_kde_docdir/HTML/*/kmplot
%_kde_mandir/man1/kmplot.1.*
%_datadir/dbus-1/interfaces/org.kde.kmplot.KmPlot.xml
%_datadir/dbus-1/interfaces/org.kde.kmplot.MainDlg.xml
%_datadir/dbus-1/interfaces/org.kde.kmplot.Parser.xml
%_datadir/dbus-1/interfaces/org.kde.kmplot.View.xml

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4	
%make

%install
%makeinstall_std -C build

