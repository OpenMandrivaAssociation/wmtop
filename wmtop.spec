%define version 0.84	
%define name wmtop
%define release 12

Summary:	WindowMaker dock applet for top
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
Source:		%{name}-%{version}.tar.bz2
Patch0:		mkfile.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		https://wmtop.sourceforge.net/
Buildrequires:	libxpm-devel
Buildrequires:	libxext-devel
Buildrequires:	libxau-devel
Buildrequires:	libxdmcp-devel

%description
Wmtop is a WindowMaker dockapp that is a mini graphical version of the 
cpu monitoring utility top. Themes are included.

%prep

%setup -q
%patch0

%build
%ifarch x86_64
perl -pi -e "s|lib|lib64|g" Makefile
%endif

%make linux

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 wmtop $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 wmtop.1 $RPM_BUILD_ROOT%{_mandir}/man1/
chmod 644 BUGS CHANGES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%{_bindir}/wmtop
%{_mandir}/man1/*
%doc BUGS CHANGES README TODO


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.84-11mdv2010.0
+ Revision: 434935
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.84-10mdv2009.0
+ Revision: 262094
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.84-9mdv2009.0
+ Revision: 256268
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Nov 30 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.84-7mdv2008.1
+ Revision: 114203
- finer Buildrequires



* Thu Jan 26 2006 Lenny Cartier <lenny@mandriva.com> 0.84-6mdk
- x86_64 fix

* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.84-5mdk
- Rebuild

* Sun Dec 07 2003 Franck Villaume <fvill@freesurf.fr> 0.84-4mdk
- add BuildRequires : XFree86-devel
- add support to RPM_OPT_FLAGS
- support 64 bits : libxpm-devel -> xpm-devel

* Mon Aug 25 2003 Michael Scherer <scherer.michael@free.fr> 0.84-3mdk
- BuildRequires (  libxpm-devel )
- rm $RPM_BUILD_ROOT in %%install

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.84-2mdk
- rebuild

* Tue May 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.84-1mdk
- added by Matthias Debus <psic4t@netbands.de>
