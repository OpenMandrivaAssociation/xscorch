%define	name	xscorch
%define version 0.2.1
%define release -c 
%define	Summary	Clone of Scorched Earth

Summary:	Clone of Scorched Earth
Name:		xscorch
Version:	0.2.1
Release:	%mkrel -c pre2 1
Source0:	http://www.xscorch.org/releases/%{name}-%{version}-pre2.tar.gz
Source11:	xscorch-16x16.png
Source12:	xscorch-32x32.png
Source13:	xscorch-48x48.png
Patch1:		xscorch-0.2.0-non-crazy-scoring--standard.patch
Patch3:		xscorch-0.2.1-gtk2.22.patch
Patch4:		xscorch-0.2.1-link.patch
Url:		https://www.xscorch.org/
License:	GPLv2+
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libmikmod-devel
BuildRequires:	gtk+2-devel

%description 
Xscorch is a clone of the classic DOS game, "Scorched Earth". The basic goal
is to annihilate enemy tanks using overpowered guns :). Basically, you buy
weapons, you target the enemy by adjusting the angle of your turret and firing
power, and you hope to destroy their tank before they destroy yours.

%prep
%setup -qn %{name}-%{version}-pre2
%patch1 -p1
%patch3 -p0 -b .gtk
%patch4 -p0 -b .link

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=XScorch
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(755,root,root,755)
%{_gamesbindir}/*
%defattr(644,root,root,755)
%{_mandir}/*/*
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/*
%doc AUTHORS ChangeLog NEWS README TODO doc/AI doc/NETWORK doc/NOTES



%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 0.2.1-0.pre2.1mdv2011.0
+ Revision: 634976
- New version 0.2.1 pre2
- fix linkage and build with newer gtk2.22
- rediff 64bit patch

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.2.0-7mdv2010.0
+ Revision: 435277
- rebuild

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 0.2.0-6mdv2009.0
+ Revision: 271915
- add official patches for 64 bit support and for stability
- update home page
- update license
- fix build

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.2.0-5mdv2008.1
+ Revision: 140994
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import xscorch


* Fri Aug 25 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.2.0-5mdv2007.0
- fix summary macro used in menu item
- don't archive/bzip2 icons
- fix macro-in-%%changelog
- cleanups

* Fri Jul  7 2006 Pixel <pixel@mandriva.com> 0.2.0-4mdv2007.0
- switch to XDG menu

* Sun Jan 08 2006 Anssi Hannula <anssi@mandriva.org> 0.2.0-3mdk
- %%mkrel
- fix menu section
- fix buildrequires for lib64

* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.0-2mdk
- Rebuild

* Fri Apr  2 2004 Pixel <pixel@mandrakesoft.com> 0.2.0-1mdk
- new release
- bzipped manpage patch not needed anymore (AFAIK the text is builtin the binary)
- capitalize menu title

* Fri Apr 25 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.1.15-3mdk
- fixed buildrequires

* Mon Mar 17 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.1.15-2mdk
- drop obsolete Prefix tag
- move from %%{_bindir} to %%{_gamesbindir} and from %%{_datadir} to %%{_gamesdatadir}
- nicer formatting
- quiet setup
- don't use configure macro, somehow it made xscorch fail to compile
- added menuitem and icons
- added buildrequires

* Thu Jun 27 2002 Pixel <pixel@mandrakesoft.com> 0.1.15-1mdk
- new release

* Mon Dec 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1.14-1mdk
- 0.1.14
- refresh crazy-scoring patch

* Tue Jul 24 2001 Pixel <pixel@mandrakesoft.com> 0.1.13-2mdk
- non-crazy-scoring--standard

* Tue Jul 24 2001 Pixel <pixel@mandrakesoft.com> 0.1.13-1mdk
- new version
- fix description-line-too-long

* Sun Jan 21 2001 Pixel <pixel@mandrakesoft.com> 0.1.10-1mdk
- initial spec
