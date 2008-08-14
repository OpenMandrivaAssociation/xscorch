%define	name	xscorch
%define version 0.2.0
%define release 6
%define	Summary	Clone of Scorched Earth

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	%{name}-%{version}.tar.bz2
Source11:	xscorch-16x16.png
Source12:	xscorch-32x32.png
Source13:	xscorch-48x48.png
Patch:		xscorch-0.2.0-64bit.patch
Patch1:		xscorch-0.2.0-non-crazy-scoring--standard.patch
Patch2:		xscorch-0.2.0-stack-smash.patch
Url:		http://www.xscorch.org/
License:	GPLv2+
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libmikmod-devel gtk+1.2-devel X11-devel libglib-devel libxpm-devel

%description 
Xscorch is a clone of the classic DOS game, "Scorched Earth". The basic goal
is to annihilate enemy tanks using overpowered guns :). Basically, you buy
weapons, you target the enemy by adjusting the angle of your turret and firing
power, and you hope to destroy their tank before they destroy yours.

%prep
%setup -q
%patch
%patch1 -p1
%patch2

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}

%make LIBS="-lmikmod -lgtk -lm"

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

