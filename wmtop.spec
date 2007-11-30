%define version 0.84	
%define name wmtop
%define release %mkrel 7

Summary:	WindowMaker dock applet for top
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
Source:		%{name}-%{version}.tar.bz2
Patch0:		mkfile.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://wmtop.sourceforge.net/
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
