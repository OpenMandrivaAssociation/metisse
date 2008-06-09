# export CVSROOT=:pserver:anonymous@cvs.lri.fr:/users/asspro/ihm/metisse-cvs
# DATE=$(date +%Y%m%d)
# cvs login # no password
# cvs co fvwm-insitu
# tar cvjf fvwm-insitu-$DATE.tar.bz2 fvwm-insitu
# cvs co -d metisse-$DATE metisse
# tar cvjf metisse-$DATE.tar.bz2 metisse-$DATE

%define name metisse
%define metisse_version 0.4.0
%define metisse_cvs rc4
%define fvwm_cvs rc4
%define rel 10
%define release %mkrel 1.%{metisse_cvs}.%{rel}
%define distname %{name}-%{metisse_version}-%{metisse_cvs}
%define fvwm_name fvwm-insitu-%{fvwm_cvs}
%define fvwm_version 2.5.20

%define lib_major 1

%define lib_name %mklibname %{name} %{lib_major}

%define common_description Metisse is an experimental X desktop with some OpenGL capacity.  It consists of a virtual X server called Xmetisse, a special version of FVWM, and a FVWM module FvwmCompositor.

#workaround buggy perl.req
%define _requires_exceptions perl(Gtk)

Summary: X-based window system 
Name: %{name}
Version: %{metisse_version}
Release: %{release}
Source0: %{distname}.tar.bz2
#Source1: %{fvwm_name}.tar.bz2
Source2: Xmetisse.defaults
Source3: metisse-start-fvwm.defaults
Source4: 29metisse

# (fc) 0.4-0.20061130.1mdv force cursor to be handled by FvwmCompositor (workaround ARGB cursor bad rendering)
Patch0: metisse-20061130-fixcursor.patch
# (fc) 0.4-0.20061130.1mdv use blue background as default background
Patch1: metisse-20061130-background.patch
# (fc) 0.4-0.20061201.1mdv enable accessibility by default
Patch2: metisse-20061201-a11y.patch
# (fc) 0.4.0-20061208.1mdv change defaults (Ia Ora theme, only pager, 1 workspace)
Patch3: metisse-defaults.patch
# (gb) 64-bit + other smaller fixes
Patch4: metisse-20070112-64bit-fixes.patch
# (fc) 0.4.0-1.rc4.1mdv fix build with glx enabled
Patch5: metisse-0.4.0-rc4-fixglx.patch
# (fc) 0.4.0-1.rc4.1mdv fix kde tray icon support
Patch6: fvwm-insitu-20070117-fixkdetray.patch
# (fc) 0.4.0-1.rc4.2mdv fix pager mode border color (CVS)
Patch7: metisse-0.4.0-rc4-fixpagerborder.patch
# (fc) 0.4.0-1.rc4.3mdv fix utf8 encoding for titlebar font (Mdv bug #29019) (CVS)
Patch8: metisse-0.4.0-rc4-fixutf8title.patch
# (fc) 0.4.0-1.rc4.5mdv kill Xmetisse when exiting from a session, hide restart when running in a session manager (CVS)
Patch9: metisse-0.4.0-rc4-restart.patch
# (fc) 0.4.0-1.rc4.6mdv add gray and free color theme
Patch10: metisse-0.4.0-rc4-addcolors.patch
# (fc) 0.4.0-1.rc4.7mdv rename locale file 
Patch11: metisse-0.4.0-rc4-textdomain.patch
# (fc) 0.4.0-1.rc4.8mdv fix build with gcc 4.2
Patch12: metisse-0.4.0-rc4-fixgcc42.patch
# (fc) 0.4.0-1.rc4.9mdv don't bind Alt-F1/F2 when running under GNOME/KDE (Mdv bug #29444)
Patch13: metisse-0.4.0-rc4-keybindings.patch

License: MIT
Group: Graphical desktop/Other
Url: http://insitu.lri.fr/metisse/ 
BuildRoot: %{_tmppath}/%{name}-%{metisse_version}-%{release}-buildroot
BuildRequires: automake
BuildRequires: mesaglu-devel jpeg-devel libexif-devel freetype2-devel
BuildRequires: nucleo-devel at-spi-devel libxt-devel 
BuildRequires: readline-devel termcap-devel libstroke-devel
BuildRequires: libxpm-devel libpng-devel fribidi-devel
BuildRequires: fribidi-devel
# not enabled gnome-libs-devel librplay-devel
BuildRequires: python
Requires: x11-server-xmetisse
Requires: %{name}-fvwm
Requires: gnome-python-bonobo
Requires: compositing-wm-common

%description
%{common_description}

Xmetisse is a mix of Xvnc and XDarwin. It draws nothing on your screen; 
everything is drawn into pixmaps. Similarly to Xvnc, but with a different 
protocol, Xmetisse can send these pixmaps (and other information) to a 
"viewer". FvwmCompositor is such a viewer; it uses OpenGL for rendering 
the X desktop into a window of a "regular" 3D accelerated X server.

%package -n x11-server-xmetisse
Summary: Mix of Xvnc and XDarwin with improved protocol
Group: System/X11
Requires: compositing-server-common
Provides: compositing-server

%description -n x11-server-xmetisse
It draws nothing on your screen, every things is drawn into pixmaps. Similarly
as Xvnc, but with a different protocol, Xmetisse can send these pixmaps (and
others information) to a "viewer". FvwmCompositor is such a viewer, it uses
OpenGL (via nucleo) for rendering the X desktop into a window of a "regular"
3D accelerated X server.
%description
%{common_description}

%package -n	%{lib_name}
Summary:	Library for metisse
Group:		System/Libraries

%description -n	%{lib_name}
%{common_description}

This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{lib_name}-devel
Summary:	Development tools for programs using %{name}
Group:		Development/C
Requires:	%{lib_name} = %{metisse_version}
Provides:	%{name}-devel = %{metisse_version}-%{release}

%description -n	%{lib_name}-devel
%{common_description}

This package contains the header files and libraries needed for
developing programs using the %{name} library.

%package fvwm
Summary: Modified version of the FVWM window manager to be used with metisse
Group: Graphical desktop/FVWM based
Version: %{fvwm_version}
Obsoletes: metisse-fvwm-i18n-ar
Obsoletes: metisse-fvwm-i18n-de
Obsoletes: metisse-fvwm-i18n-de
Obsoletes: metisse-fvwm-i18n-sv_SE
Obsoletes: metisse-fvwm-i18n-zh_CN

%description fvwm
A modified version of the FVWM window manager to be used with metisse

%prep
%setup -q -n %{distname} 
#%patch0 -p1 -b .fixcursor
%patch1 -p1 -b .blueblackground
%patch2 -p1 -b .a11y
%patch3 -p1 -b .defaults
%patch4 -p1 -b .64bit-fixes
%patch5 -p1 -b .fixglx
%patch6 -p1 -b .fixkdetray
%patch7 -p1 -b .fixpagerborder
%patch8 -p1 -b .fixutf8title
%patch9 -p1 -b .restart
%patch10 -p1 -b .addcolors
%patch11 -p1 -b .textdomain
%patch12 -p1 -b .fixgcc42
%patch13 -p1 -b .keybindings

#needed by patches5 and 10
autoreconf

%build
%configure2_5x  --enable-mmx --with-gtk-prefix=/ --with-imlib-prefix=/ \
 --without-rplay-library --enable-bidi --enable-xinerama \
 --with-fontdir=%_datadir/fonts --enable-freetype \
%ifarch %ix86
 --enable-glx-x86
%endif


%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -d %{buildroot}%{_datadir}/compositing-server %{buildroot}%{_datadir}/compositing-wm %{buildroot}%{_sysconfdir}/X11/xinit.d/
install -m644 %{SOURCE2} -t %{buildroot}%{_datadir}/compositing-server/
install -m644 %{SOURCE3} -t %{buildroot}%{_datadir}/compositing-wm/
install -m755 %{SOURCE4} -t %{buildroot}%{_sysconfdir}/X11/xinit.d/

#remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/FvwmGtkDebug $RPM_BUILD_ROOT%{_libdir}/fvwm-insitu/2.5.20/FvwmGtkDebug

for i in `find $RPM_BUILD_ROOT%{_datadir}/locale -name '*.mo'` ; do
 mv $i "`dirname $i`/`basename $i .mo`-insitu.mo"
done

%find_lang fvwm-insitu
%find_lang FvwmScript-insitu
%find_lang FvwmTaskBar-insitu

cat FvwmScript-insitu.lang >> fvwm-insitu.lang
cat FvwmTaskBar-insitu.lang >> fvwm-insitu.lang

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_bindir}/metisse-combo2radio
%{_bindir}/metisse-combo2radio-edit
%{_bindir}/metisse-demo-address-app
%{_bindir}/metisse-dummy-win
%{_bindir}/metisse-start-fvwm
%{_bindir}/metisse-xlib
%{_sysconfdir}/X11/xinit.d/29metisse
%dir %{_datadir}/metisse
%{_datadir}/metisse/*
%{_datadir}/compositing-wm/metisse-start-fvwm.defaults

%files -n x11-server-xmetisse
%defattr(-,root,root)
%{_bindir}/Xmetisse
%{_bindir}/Xwnc
%{_datadir}/compositing-server/Xmetisse.defaults

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/libmetisse
%{_libdir}/pkgconfig/*.pc

%files fvwm -f fvwm-insitu.lang
%defattr(-,root,root)
%{_sysconfdir}/X11/dm/Sessions/fvwmi.desktop
%{_sysconfdir}/X11/dm/Sessions/mini-fvwmi.desktop
%{_sysconfdir}/X11/dm/Sessions/opale.desktop
%{_bindir}/FvwmCommand
%{_bindir}/facade-holder
%{_bindir}/fvwm-bug
%{_bindir}/fvwm-convert-2.4
%{_bindir}/fvwm-convert-2.6
%{_bindir}/fvwm-menu-desktop
%{_bindir}/fvwm-menu-directory
%{_bindir}/fvwm-menu-headlines
%{_bindir}/fvwm-menu-xlock
%{_bindir}/fvwm-perllib
%{_bindir}/fvwm-root
%{_bindir}/fvwmi
%{_bindir}/fvwmi-config
%{_bindir}/opale-start-fvwmi
%dir %{_libdir}/fvwm-insitu/%{fvwm_version}
%{_libdir}/fvwm-insitu/%{fvwm_version}/*
%{py_sitedir}/facade_setup.py*
%dir %{_datadir}/fvwm-insitu
%{_datadir}/fvwm-insitu/*
%{_mandir}/man1/Fvwm*
%{_mandir}/man1/fvwm*



