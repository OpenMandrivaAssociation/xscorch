%define	name	xscorch
%define version 0.2.0
%define release 5
%define	Summary	Clone of Scorched Earth

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	%{name}-%{version}.tar.bz2
Source11:	xscorch-16x16.png
Source12:	xscorch-32x32.png
Source13:	xscorch-48x48.png
Patch1:		xscorch-0.2.0-non-crazy-scoring--standard.patch.bz2
Url:		http://chaos2.org/xscorch/
License:	GPL
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
%patch1 -p1

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -d %{buildroot}%{_menudir}
cat <<EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		icon=%{name}.png \
		needs="x11" \
		section="More Applications/Games/Arcade" \
		title="XScorch"\
		longtitle="%{Summary}" \
		xdg="true"
EOF

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

%post
%{update_menus}

%postun
%{clean_menus}

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
%{_menudir}/%{name}
%doc AUTHORS ChangeLog NEWS README TODO doc/AI doc/NETWORK doc/NOTES

